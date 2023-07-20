# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_work_city_response_body import ListWorkCityResponseBody


class ListWorkCityResponse(BaseResponse):
    _types = {
        "data": ListWorkCityResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ListWorkCityResponseBody] = None
        init(self, d, self._types)