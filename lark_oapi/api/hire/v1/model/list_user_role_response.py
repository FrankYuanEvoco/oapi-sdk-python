# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_user_role_response_body import ListUserRoleResponseBody


class ListUserRoleResponse(BaseResponse):
    _types = {
        "data": ListUserRoleResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListUserRoleResponseBody] = None
        init(self, d, self._types)
