# AURELIS + AnySearch integration

AURELIS Open Core contains a small, testable AnySearch adapter.

Capabilities:
- general search via POST /v1/search
- vertical routing via tag
- parameterized routing via params
- normalized SearchResult objects
- public HTTP(S) URL extraction via POST /v1/extract
- anonymous operation when ANYSEARCH_API_KEY is absent
- optional authenticated operation via ANYSEARCH_API_KEY

The adapter performs no network activity on import and never writes API keys
to logs or the funding ledger.

Bounty packaging note:
The AnySearch Open Source Bounty Program requires integration into an eligible
target project's official interface/documentation and a maintenance Markdown
document. This adapter is a reusable AURELIS component and is NOT a claim that
a bounty has been awarded.

Canonical program: https://github.com/anysearch-team/open-source-bounty
API docs: https://anysearch.com/docs/api-endpoints/v1-search
