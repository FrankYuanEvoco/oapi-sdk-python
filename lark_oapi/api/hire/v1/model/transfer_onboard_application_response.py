# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .transfer_onboard_application_response_body import TransferOnboardApplicationResponseBody


class TransferOnboardApplicationResponse(BaseResponse):
    _types = {
        "data": TransferOnboardApplicationResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[TransferOnboardApplicationResponseBody] = None
        init(self, d, self._types)