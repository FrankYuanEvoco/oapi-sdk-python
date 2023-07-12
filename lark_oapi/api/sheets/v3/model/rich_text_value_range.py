# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .cell_value import CellValue


class RichTextValueRange(object):
    _types = {
        "range": str,
        "values": List[list],
    }

    def __init__(self, d):
        self.range: Optional[str] = None
        self.values: Optional[List[list]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RichTextValueRangeBuilder":
        return RichTextValueRangeBuilder()


class RichTextValueRangeBuilder(object):
    def __init__(self, rich_text_value_range: RichTextValueRange = RichTextValueRange({})) -> None:
        self._rich_text_value_range: RichTextValueRange = rich_text_value_range
    
    def range(self, range: str) -> "RichTextValueRangeBuilder":
        self._rich_text_value_range.range = range
        return self
    
    def values(self, values: List[list]) -> "RichTextValueRangeBuilder":
        self._rich_text_value_range.values = values
        return self
    
    def build(self) -> "RichTextValueRange":
        return self._rich_text_value_range