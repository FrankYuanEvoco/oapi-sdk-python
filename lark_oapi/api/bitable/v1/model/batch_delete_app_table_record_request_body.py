# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class BatchDeleteAppTableRecordRequestBody(object):
    _types = {
        "records": List[str],
    }

    def __init__(self, d):
        self.records: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchDeleteAppTableRecordRequestBodyBuilder":
        return BatchDeleteAppTableRecordRequestBodyBuilder()


class BatchDeleteAppTableRecordRequestBodyBuilder(object):
    def __init__(self, batch_delete_app_table_record_request_body: BatchDeleteAppTableRecordRequestBody = BatchDeleteAppTableRecordRequestBody({})) -> None:
        self._batch_delete_app_table_record_request_body: BatchDeleteAppTableRecordRequestBody = batch_delete_app_table_record_request_body
    
    def records(self, records: List[str]) -> "BatchDeleteAppTableRecordRequestBodyBuilder":
        self._batch_delete_app_table_record_request_body.records = records
        return self
    
    def build(self) -> "BatchDeleteAppTableRecordRequestBody":
        return self._batch_delete_app_table_record_request_body