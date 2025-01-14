# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Member(object):
    _types = {
        "member_type": str,
        "member_id": str,
        "perm": str,
        "perm_type": str,
        "type": str,
        "name": str,
        "avatar": str,
        "external_label": bool,
    }

    def __init__(self, d=None):
        self.member_type: Optional[str] = None
        self.member_id: Optional[str] = None
        self.perm: Optional[str] = None
        self.perm_type: Optional[str] = None
        self.type: Optional[str] = None
        self.name: Optional[str] = None
        self.avatar: Optional[str] = None
        self.external_label: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MemberBuilder":
        return MemberBuilder()


class MemberBuilder(object):
    def __init__(self) -> None:
        self._member = Member()

    def member_type(self, member_type: str) -> "MemberBuilder":
        self._member.member_type = member_type
        return self

    def member_id(self, member_id: str) -> "MemberBuilder":
        self._member.member_id = member_id
        return self

    def perm(self, perm: str) -> "MemberBuilder":
        self._member.perm = perm
        return self

    def perm_type(self, perm_type: str) -> "MemberBuilder":
        self._member.perm_type = perm_type
        return self

    def type(self, type: str) -> "MemberBuilder":
        self._member.type = type
        return self

    def name(self, name: str) -> "MemberBuilder":
        self._member.name = name
        return self

    def avatar(self, avatar: str) -> "MemberBuilder":
        self._member.avatar = avatar
        return self

    def external_label(self, external_label: bool) -> "MemberBuilder":
        self._member.external_label = external_label
        return self

    def build(self) -> "Member":
        return self._member
