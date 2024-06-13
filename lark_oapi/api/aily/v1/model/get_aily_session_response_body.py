# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .aily_session import AilySession


class GetAilySessionResponseBody(object):
    _types = {
        "session": AilySession,
    }

    def __init__(self, d=None):
        self.session: Optional[AilySession] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetAilySessionResponseBodyBuilder":
        return GetAilySessionResponseBodyBuilder()


class GetAilySessionResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_aily_session_response_body = GetAilySessionResponseBody()

    def session(self, session: AilySession) -> "GetAilySessionResponseBodyBuilder":
        self._get_aily_session_response_body.session = session
        return self

    def build(self) -> "GetAilySessionResponseBody":
        return self._get_aily_session_response_body