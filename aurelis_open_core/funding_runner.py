from __future__ import annotations
import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

UTC = timezone.utc

@dataclass(frozen=True)
class FundingTarget:
    id: str
    name: str
    url: str
    payout: str
    deadline: str | None
    fit: int
    evidence_urls: tuple[str, ...]
    next_action: str
    state: str = "VERIFIED"

class FundingRunner:
    """Proof-first funding planner. It prepares executable actions without inventing submissions."""

    def __init__(self, workspace: str | Path):
        self.workspace = Path(workspace)
        self.state_dir = self.workspace / "funding_state"
        self.state_dir.mkdir(parents=True, exist_ok=True)

    def rank(self, targets: Iterable[FundingTarget]) -> list[FundingTarget]:
        return sorted(targets, key=lambda t: (-t.fit, t.deadline or "9999-12-31", t.id))

    def build_execution_plan(self, targets: Iterable[FundingTarget]) -> dict:
        ranked = self.rank(targets)
        now = datetime.now(UTC).isoformat()
        return {
            "generated_at": now,
            "mode": "PROOF_FIRST",
            "targets": [asdict(t) for t in ranked],
            "rules": [
                "Never fabricate identity, eligibility, Claim ID, submission, award or payment.",
                "Never store API keys, passwords, tokens, private keys or seed phrases.",
                "A submission becomes APPLIED only after a canonical external submission record exists.",
                "A payment becomes PAID only after independent settlement evidence exists.",
            ],
        }

    def write_plan(self, targets: Iterable[FundingTarget]) -> Path:
        plan = self.build_execution_plan(targets)
        path = self.state_dir / "execution_plan.json"
        path.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
        return path

    def write_operator_queue(self, targets: Iterable[FundingTarget]) -> Path:
        ranked = self.rank(targets)
        lines = ["# AURELIS Funding Operator Queue", "", f"Generated: {datetime.now(UTC).isoformat()}", ""]
        for i, t in enumerate(ranked, 1):
            lines += [
                f"## {i}. {t.name} [{t.state}]",
                f"- Target: {t.url}",
                f"- Payout: {t.payout}",
                f"- Deadline: {t.deadline or 'open'}",
                f"- Fit: {t.fit}/100",
                f"- Next action: {t.next_action}",
                "- Evidence:",
                *[f"  - {u}" for u in t.evidence_urls],
                "",
            ]
        path = self.state_dir / "OPERATOR_QUEUE.md"
        path.write_text("\n".join(lines), encoding="utf-8")
        return path

if __name__ == "__main__":
    targets = [
        FundingTarget("ANYSEARCH-2026", "AnySearch Open Source Bounty",
                      "https://github.com/anysearch-team/open-source-bounty",
                      "CNY 2,500–7,500 per listed target", "2026-10-31T23:59:00+08:00", 96,
                      ("https://github.com/anysearch-team/open-source-bounty",),
                      "Confirm Claim ID registration slot, then execute target integration."),
        FundingTarget("TETHER-DEV-2026", "Tether Developer Grants", "https://tether.dev/",
                      "Approx. $1,500–$4,000 per defined deliverable", None, 92,
                      ("https://tether.io/news/tether-launches-developer-grants-program-to-fund-local-first-ai-and-payments-infrastructure/",
                       "https://tether.dev/"),
                      "Select one concrete local-first AI / cryptography / tooling deliverable and prepare submission package."),
        FundingTarget("ARIA-SCALING-2026", "ARIA Scaling Trust",
                      "https://aria.org.uk/opportunity-spaces/trust-everything-everywhere/scaling-trust/funding",
                      "Program-specific", "2026-10-31T14:00:00Z", 84,
                      ("https://aria.org.uk/opportunity-spaces/trust-everything-everywhere/scaling-trust/funding",),
                      "Convert AURELIS agent verification architecture into a proposal with measurable research deliverables."),
    ]
    runner = FundingRunner(Path(__file__).resolve().parents[1])
    print(runner.write_plan(targets))
    print(runner.write_operator_queue(targets))
