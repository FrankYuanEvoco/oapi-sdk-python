# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .member import Member


class ListSpaceMemberResponseBody(object):
    _types = {
        "members": List[Member],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.members: Optional[List[Member]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListSpaceMemberResponseBodyBuilder":
        return ListSpaceMemberResponseBodyBuilder()


class ListSpaceMemberResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_space_member_response_body = ListSpaceMemberResponseBody()

    def members(self, members: List[Member]) -> "ListSpaceMemberResponseBodyBuilder":
        self._list_space_member_response_body.members = members
        return self

    def page_token(self, page_token: str) -> "ListSpaceMemberResponseBodyBuilder":
        self._list_space_member_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListSpaceMemberResponseBodyBuilder":
        self._list_space_member_response_body.has_more = has_more
        return self

    def build(self) -> "ListSpaceMemberResponseBody":
        return self._list_space_member_response_body