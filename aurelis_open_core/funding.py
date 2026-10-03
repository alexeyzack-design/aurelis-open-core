from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

class FundingState(str, Enum):
    DISCOVERED = "DISCOVERED"
    VERIFIED = "VERIFIED"
    ELIGIBLE = "ELIGIBLE"
    APPLIED = "APPLIED"
    AWARDED = "AWARDED"
    PAID = "PAID"
    REJECTED = "REJECTED"

@dataclass(frozen=True)
class FundingOpportunity:
    name: str
    url: str
    payout: str
    requirements: str
    state: FundingState = FundingState.DISCOVERED
    def can_claim(self) -> bool:
        return self.state == FundingState.AWARDED
