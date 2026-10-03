from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime, timezone

class Role(str, Enum):
    RESEARCHER = "researcher"
    CRITIC = "critic"
    VERIFIER = "verifier"
    SYNTHESIZER = "synthesizer"

class EvidenceStatus(str, Enum):
    UNVERIFIED = "UNVERIFIED"
    VERIFIED = "VERIFIED"
    REJECTED = "REJECTED"

@dataclass(frozen=True)
class Evidence:
    claim: str
    source: str
    status: EvidenceStatus = EvidenceStatus.UNVERIFIED
    note: str = ""

@dataclass
class AgentMessage:
    role: Role
    task_id: str
    content: str
    evidence: list[Evidence] = field(default_factory=list)
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    def verified_evidence(self) -> list[Evidence]:
        return [e for e in self.evidence if e.status == EvidenceStatus.VERIFIED]
