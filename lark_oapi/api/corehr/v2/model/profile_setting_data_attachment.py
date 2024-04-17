# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .profile_setting_personal_record import ProfileSettingPersonalRecord


class ProfileSettingDataAttachment(object):
    _types = {
        "personal_records": List[ProfileSettingPersonalRecord],
    }

    def __init__(self, d=None):
        self.personal_records: Optional[List[ProfileSettingPersonalRecord]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProfileSettingDataAttachmentBuilder":
        return ProfileSettingDataAttachmentBuilder()


class ProfileSettingDataAttachmentBuilder(object):
    def __init__(self) -> None:
        self._profile_setting_data_attachment = ProfileSettingDataAttachment()

    def personal_records(self,
                         personal_records: List[ProfileSettingPersonalRecord]) -> "ProfileSettingDataAttachmentBuilder":
        self._profile_setting_data_attachment.personal_records = personal_records
        return self

    def build(self) -> "ProfileSettingDataAttachment":
        return self._profile_setting_data_attachment