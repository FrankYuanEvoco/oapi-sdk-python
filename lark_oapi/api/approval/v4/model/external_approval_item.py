# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ExternalApprovalItem(object):
    _types = {
        "approval_code": str,
        "approval_external_id": str,
    }

    def __init__(self, d=None):
        self.approval_code: Optional[str] = None
        self.approval_external_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ExternalApprovalItemBuilder":
        return ExternalApprovalItemBuilder()


class ExternalApprovalItemBuilder(object):
    def __init__(self) -> None:
        self._external_approval_item = ExternalApprovalItem()

    def approval_code(self, approval_code: str) -> "ExternalApprovalItemBuilder":
        self._external_approval_item.approval_code = approval_code
        return self

    def approval_external_id(self, approval_external_id: str) -> "ExternalApprovalItemBuilder":
        self._external_approval_item.approval_external_id = approval_external_id
        return self

    def build(self) -> "ExternalApprovalItem":
        return self._external_approval_item