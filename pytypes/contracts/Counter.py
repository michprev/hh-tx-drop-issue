from __future__ import annotations

import random 
from dataclasses import dataclass 
from typing import List, NewType, Optional, overload, Union
from typing_extensions import Literal

from woke.testing.core import Contract, Library, Address, Wei, Account, ChainInterface
from woke.testing.internal import TransactionRevertedError
from woke.testing.transactions import LegacyTransaction

from woke.testing.pytypes_generator import RequestType
from enum import IntEnum



class Counter(Contract):
    _abi = {b'\x06f\x1a\xbd': {'inputs': [], 'name': 'count', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd0\x9d\xe0\x8a': {'inputs': [], 'name': 'increment', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _bytecode = "608060405234801561001057600080fd5b50610151806100206000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c806306661abd1461003b578063d09de08a14610059575b600080fd5b610043610063565b604051610050919061009d565b60405180910390f35b610061610069565b005b60005481565b600160008082825461007b91906100e7565b92505081905550565b6000819050919050565b61009781610084565b82525050565b60006020820190506100b2600083018461008e565b92915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b60006100f282610084565b91506100fd83610084565b9250828201905080821115610115576101146100b8565b5b9291505056fea2646970667358221220293b9d43b376e779b63ff7b51d0e484f49ef626806e1132c5c38b635dc6d161e64736f6c63430008110033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, chain: Optional[ChainInterface] = None) -> Counter:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, chain: Optional[ChainInterface] = None) -> LegacyTransaction[Counter]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, chain: Optional[ChainInterface] = None) -> Union[Counter, LegacyTransaction[Counter]]:
        return cls._deploy([], return_tx, Counter, from_, value, gas_limit, {}, chain)

    @classmethod
    def bytecode(cls) -> bytes:
        return cls._get_bytecode({})

    @overload
    def count(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> int:
        ...

    @overload
    def count(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[int]:
        ...

    def count(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='call') -> Union[int, LegacyTransaction[int]]:
        """
        Returns:
            uint256
        """
        return self._transact("06661abd", [], return_tx, request_type, int, from_, to, value, gas_limit) if not request_type == 'call' else self._call("06661abd", [], return_tx, int, from_, to, value, gas_limit)

    @overload
    def increment(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> None:
        ...

    @overload
    def increment(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[None]:
        ...

    def increment(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='default') -> Union[None, LegacyTransaction[None]]:
        return self._transact("d09de08a", [], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("d09de08a", [], return_tx, type(None), from_, to, value, gas_limit)

