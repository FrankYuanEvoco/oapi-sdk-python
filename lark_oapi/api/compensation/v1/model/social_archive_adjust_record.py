# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .social_archive_detail import SocialArchiveDetail


class SocialArchiveAdjustRecord(object):
    _types = {
        "user_id": str,
        "record_type": str,
        "details": List[SocialArchiveDetail],
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        self.record_type: Optional[str] = None
        self.details: Optional[List[SocialArchiveDetail]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SocialArchiveAdjustRecordBuilder":
        return SocialArchiveAdjustRecordBuilder()


class SocialArchiveAdjustRecordBuilder(object):
    def __init__(self) -> None:
        self._social_archive_adjust_record = SocialArchiveAdjustRecord()

    def user_id(self, user_id: str) -> "SocialArchiveAdjustRecordBuilder":
        self._social_archive_adjust_record.user_id = user_id
        return self

    def record_type(self, record_type: str) -> "SocialArchiveAdjustRecordBuilder":
        self._social_archive_adjust_record.record_type = record_type
        return self

    def details(self, details: List[SocialArchiveDetail]) -> "SocialArchiveAdjustRecordBuilder":
        self._social_archive_adjust_record.details = details
        return self

    def build(self) -> "SocialArchiveAdjustRecord":
        return self._social_archive_adjust_record