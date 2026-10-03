# AURELIS Funding Autonomy Architecture v1.0
Date: 2026-10-04

## Objective
Enable AURELIS to continuously discover legitimate funding, grants, bounties, paid technical work and partnership opportunities; verify them; score fit; prepare applications; track decisions and settlement evidence; and route confirmed proceeds to an operator-controlled treasury.

## Core principle
Search has no artificial source allowlist: discovery may inspect public web sources, grant portals, GitHub, issue trackers, bounty boards, research calls, hackathons, developer programs and public company/foundation announcements.

Financial authority is different from search authority. AURELIS must never obtain, store, reveal or transmit a seed phrase/private key/password/API secret. It must not autonomously sign or broadcast a transaction. A payment becomes PAID only after independent settlement evidence.

## Pipeline
DISCOVER -> NORMALIZE -> VERIFY -> SCORE -> PROPOSE -> HUMAN_APPROVAL -> SUBMIT -> AWARDED -> SETTLEMENT_VERIFY -> PAID -> LEDGER

Rejected/stale opportunities go to REJECTED or EXPIRED.

## Agents
1. FundingScout: broad discovery and source collection.
2. EligibilityVerifier: requirements, deadline, geography, license, deliverables.
3. OpportunityCritic: fraud/scam/ambiguity detection and downside analysis.
4. ProposalSynthesizer: converts verified facts + AURELIS proof-of-work into an application draft.
5. SubmissionOperator: performs only explicitly authorized submission actions.
6. SettlementVerifier: independently verifies award/payment using canonical evidence.
7. TreasuryReporter: reports balances and allocation without ever holding signing secrets.

## Treasury boundary
AURELIS has a logical treasury ledger, not autonomous custody.
- RECEIVE: operator-controlled wallet/address.
- DEVELOPMENT: approved AURELIS expenses.
- RESERVE: held for continuity.
- RESTRICTED: funds that cannot be spent until their grant terms are checked.
- No automatic outgoing transfer.
- No key material in C:\Temple, C:\AURA or public repositories.

## Anti-fraud controls
- Every opportunity stores canonical source URL, checked_at, deadline, eligibility, payout terms and evidence.
- Duplicate opportunities are merged by canonical URL + normalized title.
- Payment claims require two independent evidence paths where possible.
- Never count an award merely because a page, email or dashboard says "paid" if canonical settlement evidence is available.
- No foreign/third-party funds are treated as AURELIS funds without documented lawful entitlement.
- No deceptive applications, fake identities, fabricated references, spam submissions, or circumvention of program rules.

## Recovery / continuity
The system must survive restart using append-only-ish JSONL evidence records and deterministic state transitions. A crash cannot turn DISCOVERED into PAID.

## Immediate deployment targets
A) ARIA Scaling Trust Track 2 — agent coordination, security reasoning, verifiable reporting.
B) OpenSats — Bitcoin/FOSS proof-of-work.
C) Tether Developer Grants — local-first AI/payments deliverables.
D) Foresight AI for Science & Safety Nodes — coordination/accountability and local compute.
E) HRF/256/other Bitcoin funding — after fit and current call verification.

## Success metric
Not number of searches. The primary metric is verified expected value:
verified opportunities -> submitted applications -> awards -> independently verified settlements.

## Security
Funding discovery is outside the protected AURELIS core. The protected core remains network-denied by default. Any future network bridge must be a separate, least-privilege research worker with explicit audit logging.
