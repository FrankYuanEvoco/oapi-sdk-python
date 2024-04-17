# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DeletePermissionMemberRequestBody(object):
    _types = {
        "type": str,
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeletePermissionMemberRequestBodyBuilder":
        return DeletePermissionMemberRequestBodyBuilder()


class DeletePermissionMemberRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_permission_member_request_body = DeletePermissionMemberRequestBody()

    def type(self, type: str) -> "DeletePermissionMemberRequestBodyBuilder":
        self._delete_permission_member_request_body.type = type
        return self

    def build(self) -> "DeletePermissionMemberRequestBody":
        return self._delete_permission_member_request_body