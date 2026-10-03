from .core import Block, Chain, Transaction, Validator
from .agents import AgentMessage, Evidence, EvidenceStatus, Role

def main() -> None:
    tx = Transaction("alice", "bob", 100, 1)
    genesis = Block(0, "0" * 64, (tx,))
    chain = Chain([genesis])
    chain.append(Block(1, genesis.hash(), (tx,), nonce=1))
    assert Validator.validate(chain)
    msg = AgentMessage(Role.RESEARCHER, "demo-001", "funding candidate", [
        Evidence("candidate exists", "public-source", EvidenceStatus.VERIFIED)
    ])
    print("AURELIS Open Core demo OK")
    print("blocks:", len(chain.blocks), "verified evidence:", len(msg.verified_evidence()))

if __name__ == "__main__":
    main()
