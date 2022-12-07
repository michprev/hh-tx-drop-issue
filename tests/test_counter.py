from woke.testing import default_chain, connect, snapshot_and_revert
from woke.testing.random import random_address

from pytypes.contracts.Counter import Counter


@connect(default_chain, "http://localhost:8545")
@snapshot_and_revert(default_chain)
def test_counter():
    default_chain.default_account = default_chain.accounts[0]
    default_chain.gas_price = 0

    counter = Counter.deploy()
    assert counter.count() == 0

    with default_chain.change_automine(False):
        tx1 = counter.increment(return_tx=True)
        tx2 = counter.increment(return_tx=True)

        default_chain.mine()
    
    assert counter.count() == 2
