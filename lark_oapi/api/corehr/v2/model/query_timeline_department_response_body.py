# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .department_timeline import DepartmentTimeline


class QueryTimelineDepartmentResponseBody(object):
    _types = {
        "items": List[DepartmentTimeline],
    }

    def __init__(self, d=None):
        self.items: Optional[List[DepartmentTimeline]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryTimelineDepartmentResponseBodyBuilder":
        return QueryTimelineDepartmentResponseBodyBuilder()


class QueryTimelineDepartmentResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._query_timeline_department_response_body = QueryTimelineDepartmentResponseBody()

    def items(self, items: List[DepartmentTimeline]) -> "QueryTimelineDepartmentResponseBodyBuilder":
        self._query_timeline_department_response_body.items = items
        return self

    def build(self) -> "QueryTimelineDepartmentResponseBody":
        return self._query_timeline_department_response_body
