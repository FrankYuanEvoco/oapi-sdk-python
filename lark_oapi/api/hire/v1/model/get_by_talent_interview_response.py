# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_by_talent_interview_response_body import GetByTalentInterviewResponseBody


class GetByTalentInterviewResponse(BaseResponse):
    _types = {
        "data": GetByTalentInterviewResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetByTalentInterviewResponseBody] = None
        init(self, d, self._types)