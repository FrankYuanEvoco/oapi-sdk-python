# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ContractPeriod(object):
    _types = {
        "period_type": int,
        "period": int,
    }

    def __init__(self, d=None):
        self.period_type: Optional[int] = None
        self.period: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ContractPeriodBuilder":
        return ContractPeriodBuilder()


class ContractPeriodBuilder(object):
    def __init__(self) -> None:
        self._contract_period = ContractPeriod()

    def period_type(self, period_type: int) -> "ContractPeriodBuilder":
        self._contract_period.period_type = period_type
        return self

    def period(self, period: int) -> "ContractPeriodBuilder":
        self._contract_period.period = period
        return self

    def build(self) -> "ContractPeriod":
        return self._contract_period