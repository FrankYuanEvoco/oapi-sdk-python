# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .logout_session_request_body import LogoutSessionRequestBody


class LogoutSessionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[LogoutSessionRequestBody] = None

    @staticmethod
    def builder() -> "LogoutSessionRequestBuilder":
        return LogoutSessionRequestBuilder()


class LogoutSessionRequestBuilder(object):

    def __init__(self) -> None:
        logout_session_request = LogoutSessionRequest()
        logout_session_request.http_method = HttpMethod.POST
        logout_session_request.uri = "/open-apis/passport/v1/sessions/logout"
        logout_session_request.token_types = {AccessTokenType.TENANT}
        self._logout_session_request: LogoutSessionRequest = logout_session_request

    def user_id_type(self, user_id_type: str) -> "LogoutSessionRequestBuilder":
        self._logout_session_request.user_id_type = user_id_type
        self._logout_session_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: LogoutSessionRequestBody) -> "LogoutSessionRequestBuilder":
        self._logout_session_request.request_body = request_body
        self._logout_session_request.body = request_body
        return self

    def build(self) -> LogoutSessionRequest:
        return self._logout_session_request