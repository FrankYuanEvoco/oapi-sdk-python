# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class SearchGroupRequestBody(object):
    _types = {
        "group_name": str,
    }

    def __init__(self, d):
        self.group_name: Optional[str] = None
        self.exactly_matched: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchGroupRequestBodyBuilder":
        return SearchGroupRequestBodyBuilder()


class SearchGroupRequestBodyBuilder(object):
    def __init__(self, search_group_request_body: SearchGroupRequestBody = SearchGroupRequestBody({})) -> None:
        self._search_group_request_body: SearchGroupRequestBody = search_group_request_body
    
    def group_name(self, group_name: str) -> "SearchGroupRequestBodyBuilder":
        self._search_group_request_body.group_name = group_name
        return self
    
    
    def build(self) -> "SearchGroupRequestBody":
        return self._search_group_request_body