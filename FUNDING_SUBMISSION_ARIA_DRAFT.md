# ARIA Scaling Trust — AURELIS Open Core proposal draft

## Track
Scaling Trust — Track 2: Tooling.

## Core proposition
AURELIS Open Core develops open-source, reusable infrastructure for evidence-first coordination and verification between AI agents.

The prototype implements a Researcher -> Critic -> Verifier -> Synthesizer protocol and deterministic verification primitives. The design goal is not autonomous authority: each result carries explicit evidence/status, and verification is separated from generation.

## Relevant capability
- requirement/evidence hand-off between agent roles;
- independent critique and verification;
- reproducible local execution;
- explicit funding/recovery state transitions;
- security boundary excluding secrets, private keys and unauthorized asset recovery.

## Existing proof of work
Repository: C:\AURA\AURELIS-OPEN-CORE
Commit 5455922: Initial AURELIS Open Core proof of work
Commit efdd541: chore: add gitignore

Demo verification:
AURELIS Open Core demo OK
blocks: 2
verified evidence: 1

## Proposed work
Build a reusable coordination layer with:
1. typed agent messages and evidence references;
2. verifier checkpoints and rejection paths;
3. adversarial tests for conflicting or unsupported claims;
4. deterministic audit records;
5. reproducible local test harness;
6. public documentation and reference implementation.

## Expected result
An open-source baseline that other agent systems can reuse to coordinate, critique and verify work in an auditable way, with explicit boundaries between generated claims and verified evidence.

## Risk controls
No private keys, seed phrases or credentials are accepted. The prototype is not a production wallet. Security-sensitive actions require explicit authorization and verification.

## Current publication status
Public repository verified: https://github.com/alexeyzack-design/aurelis-open-core . Code push is still pending authenticated Git transport.
