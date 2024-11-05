# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class DeleteLocationAddressRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.location_id: Optional[str] = None
        self.address_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteLocationAddressRequestBuilder":
        return DeleteLocationAddressRequestBuilder()


class DeleteLocationAddressRequestBuilder(object):

    def __init__(self) -> None:
        delete_location_address_request = DeleteLocationAddressRequest()
        delete_location_address_request.http_method = HttpMethod.DELETE
        delete_location_address_request.uri = "/open-apis/corehr/v2/locations/:location_id/addresses/:address_id"
        delete_location_address_request.token_types = {AccessTokenType.TENANT}
        self._delete_location_address_request: DeleteLocationAddressRequest = delete_location_address_request

    def location_id(self, location_id: str) -> "DeleteLocationAddressRequestBuilder":
        self._delete_location_address_request.location_id = location_id
        self._delete_location_address_request.paths["location_id"] = str(location_id)
        return self

    def address_id(self, address_id: str) -> "DeleteLocationAddressRequestBuilder":
        self._delete_location_address_request.address_id = address_id
        self._delete_location_address_request.paths["address_id"] = str(address_id)
        return self

    def build(self) -> DeleteLocationAddressRequest:
        return self._delete_location_address_request