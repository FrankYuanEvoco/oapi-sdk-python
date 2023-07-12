# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class CreateIdentityRequestBody(object):
    _types = {
        "identity_name": str,
        "identity_code": str,
        "mobile": str,
    }

    def __init__(self, d):
        self.identity_name: Optional[str] = None
        self.identity_code: Optional[str] = None
        self.mobile: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateIdentityRequestBodyBuilder":
        return CreateIdentityRequestBodyBuilder()


class CreateIdentityRequestBodyBuilder(object):
    def __init__(self, create_identity_request_body: CreateIdentityRequestBody = CreateIdentityRequestBody({})) -> None:
        self._create_identity_request_body: CreateIdentityRequestBody = create_identity_request_body
    
    def identity_name(self, identity_name: str) -> "CreateIdentityRequestBodyBuilder":
        self._create_identity_request_body.identity_name = identity_name
        return self
    
    def identity_code(self, identity_code: str) -> "CreateIdentityRequestBodyBuilder":
        self._create_identity_request_body.identity_code = identity_code
        return self
    
    def mobile(self, mobile: str) -> "CreateIdentityRequestBodyBuilder":
        self._create_identity_request_body.mobile = mobile
        return self
    
    def build(self) -> "CreateIdentityRequestBody":
        return self._create_identity_request_body