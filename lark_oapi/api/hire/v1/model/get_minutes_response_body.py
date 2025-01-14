# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .minutes import Minutes


class GetMinutesResponseBody(object):
    _types = {
        "minutes": Minutes,
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.minutes: Optional[Minutes] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetMinutesResponseBodyBuilder":
        return GetMinutesResponseBodyBuilder()


class GetMinutesResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_minutes_response_body = GetMinutesResponseBody()

    def minutes(self, minutes: Minutes) -> "GetMinutesResponseBodyBuilder":
        self._get_minutes_response_body.minutes = minutes
        return self

    def page_token(self, page_token: str) -> "GetMinutesResponseBodyBuilder":
        self._get_minutes_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "GetMinutesResponseBodyBuilder":
        self._get_minutes_response_body.has_more = has_more
        return self

    def build(self) -> "GetMinutesResponseBody":
        return self._get_minutes_response_body
