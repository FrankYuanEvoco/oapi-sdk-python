# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetNodeSpaceRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.token: Optional[str] = None

    @staticmethod
    def builder() -> "GetNodeSpaceRequestBuilder":
        return GetNodeSpaceRequestBuilder()


class GetNodeSpaceRequestBuilder(object):

    def __init__(self, get_node_space_request: GetNodeSpaceRequest = GetNodeSpaceRequest()) -> None:
        get_node_space_request.http_method = HttpMethod.GET
        get_node_space_request.uri = "/open-apis/wiki/v2/spaces/get_node"
        get_node_space_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_node_space_request: GetNodeSpaceRequest = get_node_space_request
    
    def token(self, token: str) -> "GetNodeSpaceRequestBuilder":
        self._get_node_space_request.token = token
        self._get_node_space_request.queries["token"] = str(token)
        return self
    

    def build(self) -> GetNodeSpaceRequest:
        return self._get_node_space_request