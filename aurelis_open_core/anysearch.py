"""Safe AnySearch adapter for AURELIS Open Core."""
from __future__ import annotations
from dataclasses import dataclass
import json, os
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

DEFAULT_BASE_URL = "https://api.anysearch.com"

@dataclass(frozen=True)
class SearchResult:
    title: str
    url: str
    snippet: str = ""
    content: str = ""

class AnySearchError(RuntimeError):
    pass

class AnySearchClient:
    def __init__(self, api_key: str | None = None, base_url: str = DEFAULT_BASE_URL, timeout: float = 20.0):
        self.api_key = api_key if api_key is not None else os.getenv("ANYSEARCH_API_KEY")
        self.base_url, self.timeout = base_url.rstrip("/"), timeout

    def _post(self, path: str, payload: dict) -> dict:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = "Bearer " + self.api_key
        req = Request(self.base_url + path, data=body, headers=headers, method="POST")
        try:
            with urlopen(req, timeout=self.timeout) as response:
                data = json.loads(response.read().decode("utf-8"))
        except HTTPError as exc:
            raise AnySearchError(f"AnySearch HTTP {exc.code}") from exc
        except (URLError, TimeoutError) as exc:
            raise AnySearchError("AnySearch network failure") from exc
        except json.JSONDecodeError as exc:
            raise AnySearchError("AnySearch returned invalid JSON") from exc
        if data.get("code") != 0:
            raise AnySearchError(data.get("message", "AnySearch request failed"))
        return data

    def search(self, query: str, max_results: int = 10, *, tag: str | None = None,
               zone: str | None = None, language: str | None = None,
               params: dict | None = None, format: str = "json") -> list[SearchResult]:
        if not query.strip():
            raise ValueError("query must not be empty")
        if not 1 <= max_results <= 10:
            raise ValueError("max_results must be between 1 and 10")
        if format not in {"json", "markdown"}:
            raise ValueError("format must be json or markdown")
        payload = {"query": query, "max_results": max_results, "format": format}
        for key, value in (("tag", tag), ("zone", zone), ("language", language), ("params", params)):
            if value is not None:
                payload[key] = value
        data = self._post("/v1/search", payload)
        return [SearchResult(item.get("title", ""), item.get("url", ""),
                             item.get("snippet", ""), item.get("content", ""))
                for item in data.get("data", {}).get("results", [])]

    def extract(self, url: str) -> str:
        if not (url.startswith("http://") or url.startswith("https://")):
            raise ValueError("url must be an absolute HTTP(S) URL")
        data = self._post("/v1/extract", {"url": url})
        return data.get("data", {}).get("content", "")
