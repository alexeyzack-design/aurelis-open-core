from __future__ import annotations
from dataclasses import dataclass, field
import hashlib
import json

def canonical(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()

def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

@dataclass(frozen=True)
class Transaction:
    sender: str
    recipient: str
    amount: int
    nonce: int
    signature: str = ""
    def payload(self) -> dict:
        return {"sender": self.sender, "recipient": self.recipient, "amount": self.amount, "nonce": self.nonce}
    def txid(self) -> str:
        return sha256_hex(canonical(self.payload()))

@dataclass(frozen=True)
class Signature:
    signer: str
    digest: str
    def verify(self, payload_digest: str) -> bool:
        return self.digest == payload_digest and bool(self.signer)

@dataclass(frozen=True)
class Block:
    index: int
    previous_hash: str
    transactions: tuple[Transaction, ...]
    nonce: int = 0
    def hash(self) -> str:
        return sha256_hex(canonical({
            "index": self.index,
            "previous_hash": self.previous_hash,
            "transactions": [t.payload() for t in self.transactions],
            "nonce": self.nonce,
        }))

@dataclass
class Chain:
    blocks: list[Block] = field(default_factory=list)
    def append(self, block: Block) -> None:
        if self.blocks and block.previous_hash != self.blocks[-1].hash():
            raise ValueError("previous_hash does not match chain tip")
        self.blocks.append(block)
    @property
    def tip(self) -> Block | None:
        return self.blocks[-1] if self.blocks else None

class Validator:
    @staticmethod
    def validate(chain: Chain) -> bool:
        for i, block in enumerate(chain.blocks):
            if i == 0:
                continue
            if block.previous_hash != chain.blocks[i - 1].hash():
                return False
        return True
