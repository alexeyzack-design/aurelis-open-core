from aurelis_open_core.anysearch import AnySearchClient, AnySearchError

def test_search_payload_and_result_mapping(monkeypatch):
    seen = {}
    def fake_post(self, path, payload):
        seen["path"], seen["payload"] = path, payload
        return {"code": 0, "data": {"results": [{"title": "A", "url": "https://a.example", "snippet": "s", "content": "c"}]}}
    monkeypatch.setattr(AnySearchClient, "_post", fake_post)
    results = AnySearchClient(api_key="SECRET").search("AURELIS", max_results=1, tag="code.doc", language="en")
    assert seen["path"] == "/v1/search"
    assert seen["payload"]["query"] == "AURELIS"
    assert results[0].url == "https://a.example"

def test_validation():
    client = AnySearchClient()
    for bad in ("", "   "):
        try: client.search(bad); assert False
        except ValueError: pass
    try: client.extract("file:///secret"); assert False
    except ValueError: pass

def test_errors_do_not_expose_credentials(monkeypatch):
    def fake_post(self, path, payload): raise AnySearchError("AnySearch HTTP 401")
    monkeypatch.setattr(AnySearchClient, "_post", fake_post)
    try: AnySearchClient(api_key="SECRET").search("test"); assert False
    except AnySearchError as exc: assert "SECRET" not in str(exc)
