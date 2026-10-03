# OpenSats — AURELIS Open Core funding draft

## Project
AURELIS Open Core — local-first AI-agent coordination + verifiable Bitcoin infrastructure.

## Proof of Work
Local repository: C:\AURA\AURELIS-OPEN-CORE
Verified commits:
- 5455922 — Initial AURELIS Open Core proof of work
- efdd541 — chore: add gitignore

Verified local demo:
AURELIS Open Core demo OK
blocks: 2
verified evidence: 1

## What is being built
A small, auditable open-source foundation combining deterministic Bitcoin-like laboratory primitives (Transaction, Signature, Block, Chain, Validator) with an evidence-first multi-agent coordination protocol:
Researcher -> Critic -> Verifier -> Synthesizer.

Funding records use explicit states:
DISCOVERED -> VERIFIED -> ELIGIBLE -> APPLIED -> AWARDED -> PAID.

## Why it matters
The project is designed to make AI-agent work reproducible and auditable while keeping Bitcoin-related primitives transparent and locally testable. The current prototype does not hold private keys and does not support unauthorized wallet access.

## Proposed 3-month deliverables
1. Public GitHub repository with reproducible setup and tests.
2. Expand deterministic transaction/block/validation test coverage.
3. Define a signed/evidence-bearing agent message schema.
4. Add adversarial verification tests for Researcher/Critic/Verifier/Synthesizer hand-offs.
5. Publish funding/evidence state machine and reproducible demo artifacts.
6. Document limitations, threat model and security boundaries.

## Current status
Early research prototype. Public repository verified: https://github.com/alexeyzack-design/aurelis-open-core . Code push is still pending authenticated Git transport.

## Funding use
Developer time, testing/compute, documentation, security review and open-source maintenance.

## Transparency
All resulting code and educational materials will remain public under the repository's open-source license. Funding receipt will be recorded separately from proof-of-work; payment will only be marked PAID after independently verifiable settlement evidence.
