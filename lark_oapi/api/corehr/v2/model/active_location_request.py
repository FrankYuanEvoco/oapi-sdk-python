# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .active_location_request_body import ActiveLocationRequestBody


class ActiveLocationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[ActiveLocationRequestBody] = None

    @staticmethod
    def builder() -> "ActiveLocationRequestBuilder":
        return ActiveLocationRequestBuilder()


class ActiveLocationRequestBuilder(object):

    def __init__(self) -> None:
        active_location_request = ActiveLocationRequest()
        active_location_request.http_method = HttpMethod.POST
        active_location_request.uri = "/open-apis/corehr/v2/locations/active"
        active_location_request.token_types = {AccessTokenType.TENANT}
        self._active_location_request: ActiveLocationRequest = active_location_request

    def request_body(self, request_body: ActiveLocationRequestBody) -> "ActiveLocationRequestBuilder":
        self._active_location_request.request_body = request_body
        self._active_location_request.body = request_body
        return self

    def build(self) -> ActiveLocationRequest:
        return self._active_location_request