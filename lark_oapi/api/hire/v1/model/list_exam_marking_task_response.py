# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_exam_marking_task_response_body import ListExamMarkingTaskResponseBody


class ListExamMarkingTaskResponse(BaseResponse):
    _types = {
        "data": ListExamMarkingTaskResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListExamMarkingTaskResponseBody] = None
        init(self, d, self._types)