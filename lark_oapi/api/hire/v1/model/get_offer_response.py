# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_offer_response_body import GetOfferResponseBody


class GetOfferResponse(BaseResponse):
    _types = {
        "data": GetOfferResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetOfferResponseBody] = None
        init(self, d, self._types)