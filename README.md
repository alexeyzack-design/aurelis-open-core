# AURELIS Open Core

Proof-of-work repository for AURELIS: deterministic Bitcoin primitives and an evidence-first AI-agent funding/recovery coordination layer.

## Scope
- Pure local Bitcoin-like primitives for laboratory use: Transaction, Signature, Block, Chain, Validator.
- Evidence-first agent protocol: Researcher -> Critic -> Verifier -> Synthesizer.
- Funding opportunity records with explicit verification states.
- Recovery cases restricted to assets with an explicit ownership/authorization claim.
- No private-key collection, seed storage, brute-force wallet cracking, or unauthorized asset recovery.

## Status
Early research prototype. It is not a production wallet and must not hold real private keys.

## Quick start
python -m venv .venv
python -m pip install -e .
python -m pytest -q
python -m aurelis_open_core.demo

See docs/ARCHITECTURE.md and docs/FUNDING.md.
