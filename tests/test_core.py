from aurelis_open_core.core import Block, Chain, Transaction, Validator

def test_chain_validation():
    tx = Transaction("a", "b", 1, 1)
    g = Block(0, "0" * 64, (tx,))
    c = Chain([g])
    c.append(Block(1, g.hash(), (tx,), 7))
    assert Validator.validate(c)

def test_tamper_detection():
    tx = Transaction("a", "b", 1, 1)
    g = Block(0, "0" * 64, (tx,))
    c = Chain([g, Block(1, g.hash(), (tx,))])
    c.blocks[0] = Block(0, "0" * 64, (Transaction("a", "evil", 999, 1),))
    assert not Validator.validate(c)
