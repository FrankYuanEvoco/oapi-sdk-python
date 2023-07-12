# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .batch_delete_app_table_record_response_body import BatchDeleteAppTableRecordResponseBody


class BatchDeleteAppTableRecordResponse(BaseResponse):
    _types = {
        "data": BatchDeleteAppTableRecordResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[BatchDeleteAppTableRecordResponseBody] = None
        init(self, d, self._types)