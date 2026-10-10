# OpenSats — AURELIS Open Core funding draft

## Project
AURELIS Open Core — local-first AI-agent coordination + verifiable Bitcoin infrastructure.

## Proof of Work
Local repository: C:\AURA\AURELIS-OPEN-CORE
Commits:
- 5455922 — Initial AURELIS Open Core proof of work
- efdd541 — chore: add gitignore
- 2ee344c — fix: constrain package discovery for installable core

Verified local demo (2026-10-10):
AURELIS Open Core demo OK
blocks: 2
verified evidence: 1

FundingRunner unit tests: 2 passed using unittest.
Full pytest suite not yet verified because pytest is not installed and dependency installation could not complete.

## What is being built
A small, auditable open-source foundation combining deterministic Bitcoin-like laboratory primitives (Transaction, Signature, Block, Chain, Validator) with an evidence-first multi-agent coordination protocol:
Researcher -> Critic -> Verifier -> Synthesizer.

Funding records use explicit states:
DISCOVERED -> VERIFIED -> ELIGIBLE -> APPLIED -> AWARDED -> PAID.

## Why it matters
The project is designed to make AI-agent work reproducible and auditable while keeping Bitcoin-related primitives transparent and locally testable. The current prototype does not hold private keys and does not support unauthorized wallet access.

## Proposed 3-month deliverables
1. Publish the repository on GitHub with reproducible setup and tests.
2. Expand deterministic transaction/block/validation test coverage.
3. Define a signed/evidence-bearing agent message schema.
4. Add adversarial verification tests for Researcher/Critic/Verifier/Synthesizer hand-offs.
5. Publish funding/evidence state machine and reproducible demo artifacts.
6. Document limitations, threat model and security boundaries.

## Current status
Early research prototype. GitHub repository exists at https://github.com/alexeyzack-design/aurelis-open-core but was verified empty on 2026-10-10. The code is currently local; a push attempt failed because no GitHub credential was available to Git in the Windows session. Treat publication as pending until a remote commit is verified.

## Funding use
Developer time, testing/compute, documentation, security review and open-source maintenance.

## Transparency
All resulting code and educational materials will remain public under the repository's open-source license. Funding receipt will be recorded separately from proof-of-work; payment will only be marked PAID after independently verifiable settlement evidence.
