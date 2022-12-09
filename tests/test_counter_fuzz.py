from woke.testing import default_chain
from woke.testing.campaign import Campaign
from woke.testing.decorators import flow, weight, invariant
from woke.testing.random import random_address

from pytypes.contracts.Counter import Counter

class Sequence:
    counter: Counter
    value: int

    def __init__(self) -> None:
        self.counter = Counter.deploy()
        self.value = 0
    
    @flow
    def flow_increment(self) -> None:
        self.counter.increment()
        self.value += 1

    @invariant
    def invariant_count(self) -> None:
        assert self.counter.count() == self.value


def test_counter_fuzz(coverage):
    default_chain.default_account = random_address()
    default_chain.gas_price = 0

    campaing = Campaign(Sequence)
    campaing.run(10, 100, coverage=coverage)
