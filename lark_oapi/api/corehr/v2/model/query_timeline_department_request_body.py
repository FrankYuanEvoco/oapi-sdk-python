# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class QueryTimelineDepartmentRequestBody(object):
    _types = {
        "department_ids": List[str],
        "effective_date": str,
        "fields": List[str],
    }

    def __init__(self, d=None):
        self.department_ids: Optional[List[str]] = None
        self.effective_date: Optional[str] = None
        self.fields: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryTimelineDepartmentRequestBodyBuilder":
        return QueryTimelineDepartmentRequestBodyBuilder()


class QueryTimelineDepartmentRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._query_timeline_department_request_body = QueryTimelineDepartmentRequestBody()

    def department_ids(self, department_ids: List[str]) -> "QueryTimelineDepartmentRequestBodyBuilder":
        self._query_timeline_department_request_body.department_ids = department_ids
        return self

    def effective_date(self, effective_date: str) -> "QueryTimelineDepartmentRequestBodyBuilder":
        self._query_timeline_department_request_body.effective_date = effective_date
        return self

    def fields(self, fields: List[str]) -> "QueryTimelineDepartmentRequestBodyBuilder":
        self._query_timeline_department_request_body.fields = fields
        return self

    def build(self) -> "QueryTimelineDepartmentRequestBody":
        return self._query_timeline_department_request_body