# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .patch_external_interview_assessment_response_body import PatchExternalInterviewAssessmentResponseBody


class PatchExternalInterviewAssessmentResponse(BaseResponse):
    _types = {
        "data": PatchExternalInterviewAssessmentResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[PatchExternalInterviewAssessmentResponseBody] = None
        init(self, d, self._types)