# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_app_response_body import GetAppResponseBody


class GetAppResponse(BaseResponse):
    _types = {
        "data": GetAppResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetAppResponseBody] = None
        init(self, d, self._types)