# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class AddGroupMemberRequestBody(object):
    _types = {
        "member_type": str,
        "member_id_type": str,
        "member_id": str,
    }

    def __init__(self, d):
        self.member_type: Optional[str] = None
        self.member_id_type: Optional[str] = None
        self.member_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AddGroupMemberRequestBodyBuilder":
        return AddGroupMemberRequestBodyBuilder()


class AddGroupMemberRequestBodyBuilder(object):
    def __init__(self, add_group_member_request_body: AddGroupMemberRequestBody = AddGroupMemberRequestBody({})) -> None:
        self._add_group_member_request_body: AddGroupMemberRequestBody = add_group_member_request_body
    
    def member_type(self, member_type: str) -> "AddGroupMemberRequestBodyBuilder":
        self._add_group_member_request_body.member_type = member_type
        return self
    
    def member_id_type(self, member_id_type: str) -> "AddGroupMemberRequestBodyBuilder":
        self._add_group_member_request_body.member_id_type = member_id_type
        return self
    
    def member_id(self, member_id: str) -> "AddGroupMemberRequestBodyBuilder":
        self._add_group_member_request_body.member_id = member_id
        return self
    
    def build(self) -> "AddGroupMemberRequestBody":
        return self._add_group_member_request_body