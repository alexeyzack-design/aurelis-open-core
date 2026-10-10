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
1. Maintain the published repository and add reproducible CI tests and release artifacts.
2. Expand deterministic transaction/block/validation test coverage.
3. Define a signed/evidence-bearing agent message schema.
4. Add adversarial verification tests for Researcher/Critic/Verifier/Synthesizer hand-offs.
5. Publish funding/evidence state machine and reproducible demo artifacts.
6. Document limitations, threat model and security boundaries.

## Current status
Early research prototype, now published to https://github.com/alexeyzack-design/aurelis-open-core. Publication verified on 2026-10-10: origin/main resolves to f57127695e102b17583ae7b1069d7f08d521e7b6, and the GitHub Contents API returned README.md, pyproject.toml, and this funding draft. The full pytest suite remains unverified; only the two FundingRunner unittest checks and local demo have passed.

## Funding use
Developer time, testing/compute, documentation, security review and open-source maintenance.

## Transparency
All resulting code and educational materials will remain public under the repository's open-source license. Funding receipt will be recorded separately from proof-of-work; payment will only be marked PAID after independently verifiable settlement evidence.
