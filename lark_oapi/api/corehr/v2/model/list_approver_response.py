# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_approver_response_body import ListApproverResponseBody


class ListApproverResponse(BaseResponse):
    _types = {
        "data": ListApproverResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListApproverResponseBody] = None
        init(self, d, self._types)
