# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .active_company_request_body import ActiveCompanyRequestBody


class ActiveCompanyRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[ActiveCompanyRequestBody] = None

    @staticmethod
    def builder() -> "ActiveCompanyRequestBuilder":
        return ActiveCompanyRequestBuilder()


class ActiveCompanyRequestBuilder(object):

    def __init__(self) -> None:
        active_company_request = ActiveCompanyRequest()
        active_company_request.http_method = HttpMethod.POST
        active_company_request.uri = "/open-apis/corehr/v2/companies/active"
        active_company_request.token_types = {AccessTokenType.TENANT}
        self._active_company_request: ActiveCompanyRequest = active_company_request

    def request_body(self, request_body: ActiveCompanyRequestBody) -> "ActiveCompanyRequestBuilder":
        self._active_company_request.request_body = request_body
        self._active_company_request.body = request_body
        return self

    def build(self) -> ActiveCompanyRequest:
        return self._active_company_request