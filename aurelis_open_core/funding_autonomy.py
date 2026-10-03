from __future__ import annotations

from dataclasses import dataclass, asdict
from enum import Enum
import json
from pathlib import Path
from typing import Iterable


class FundingState(str, Enum):
    DISCOVERED = "DISCOVERED"
    VERIFIED = "VERIFIED"
    ELIGIBLE = "ELIGIBLE"
    PROPOSED = "PROPOSED"
    HUMAN_APPROVAL = "HUMAN_APPROVAL"
    APPLIED = "APPLIED"
    AWARDED = "AWARDED"
    SETTLEMENT_VERIFY = "SETTLEMENT_VERIFY"
    PAID = "PAID"
    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"


@dataclass(frozen=True)
class Opportunity:
    opportunity_id: str
    name: str
    canonical_url: str
    source: str
    checked_at: str
    deadline: str | None
    payout: str
    eligibility: str
    fit_score: int
    state: FundingState = FundingState.DISCOVERED
    evidence: tuple[str, ...] = ()

    def transition(self, target: FundingState) -> "Opportunity":
        allowed = {
            FundingState.DISCOVERED: {FundingState.VERIFIED, FundingState.REJECTED, FundingState.EXPIRED},
            FundingState.VERIFIED: {FundingState.ELIGIBLE, FundingState.REJECTED, FundingState.EXPIRED},
            FundingState.ELIGIBLE: {FundingState.PROPOSED, FundingState.REJECTED},
            FundingState.PROPOSED: {FundingState.HUMAN_APPROVAL, FundingState.REJECTED},
            FundingState.HUMAN_APPROVAL: {FundingState.APPLIED, FundingState.REJECTED},
            FundingState.APPLIED: {FundingState.AWARDED, FundingState.REJECTED, FundingState.EXPIRED},
            FundingState.AWARDED: {FundingState.SETTLEMENT_VERIFY, FundingState.REJECTED},
            FundingState.SETTLEMENT_VERIFY: {FundingState.PAID, FundingState.REJECTED},
            FundingState.PAID: set(),
            FundingState.REJECTED: set(),
            FundingState.EXPIRED: set(),
        }
        if target not in allowed[self.state]:
            raise ValueError(f"invalid transition: {self.state} -> {target}")
        return Opportunity(**{**asdict(self), "state": target})


class FundingLedger:
    """Deterministic local ledger; it never stores keys or signs transactions."""

    def __init__(self, path: str | Path):
        self.path = Path(path)

    def append(self, opportunity: Opportunity) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        record = asdict(opportunity)
        record["state"] = opportunity.state.value
        record["evidence"] = list(opportunity.evidence)
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")

    @staticmethod
    def rank(opportunities: Iterable[Opportunity]) -> list[Opportunity]:
        return sorted(opportunities, key=lambda x: (-x.fit_score, x.deadline or "9999-12-31", x.name))


def can_autopay(_: Opportunity) -> bool:
    """Always false: custody/signing stays outside the autonomous agent."""
    return False
