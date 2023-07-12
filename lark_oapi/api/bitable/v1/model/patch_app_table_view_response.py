# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .patch_app_table_view_response_body import PatchAppTableViewResponseBody


class PatchAppTableViewResponse(BaseResponse):
    _types = {
        "data": PatchAppTableViewResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[PatchAppTableViewResponseBody] = None
        init(self, d, self._types)