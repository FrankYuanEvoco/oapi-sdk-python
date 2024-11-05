# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .ask_app_knowledge_response_body import AskAppKnowledgeResponseBody


class AskAppKnowledgeResponse(BaseResponse):
    _types = {
        "data": AskAppKnowledgeResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[AskAppKnowledgeResponseBody] = None
        init(self, d, self._types)