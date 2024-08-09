# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n
from .i18n import I18n
from .i18n import I18n


class ReportCustomData(object):
    _types = {
        "name": I18n,
        "value": I18n,
        "description": I18n,
    }

    def __init__(self, d=None):
        self.name: Optional[I18n] = None
        self.value: Optional[I18n] = None
        self.description: Optional[I18n] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReportCustomDataBuilder":
        return ReportCustomDataBuilder()


class ReportCustomDataBuilder(object):
    def __init__(self) -> None:
        self._report_custom_data = ReportCustomData()

    def name(self, name: I18n) -> "ReportCustomDataBuilder":
        self._report_custom_data.name = name
        return self

    def value(self, value: I18n) -> "ReportCustomDataBuilder":
        self._report_custom_data.value = value
        return self

    def description(self, description: I18n) -> "ReportCustomDataBuilder":
        self._report_custom_data.description = description
        return self

    def build(self) -> "ReportCustomData":
        return self._report_custom_data
