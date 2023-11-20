# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .recognize_driving_license_response_body import RecognizeDrivingLicenseResponseBody


class RecognizeDrivingLicenseResponse(BaseResponse):
    _types = {
        "data": RecognizeDrivingLicenseResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[RecognizeDrivingLicenseResponseBody] = None
        init(self, d, self._types)