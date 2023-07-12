# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .patch_contract_response_body import PatchContractResponseBody


class PatchContractResponse(BaseResponse):
    _types = {
        "data": PatchContractResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[PatchContractResponseBody] = None
        init(self, d, self._types)