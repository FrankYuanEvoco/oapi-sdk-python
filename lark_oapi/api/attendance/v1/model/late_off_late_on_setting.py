# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class LateOffLateOnSetting(object):
    _types = {
        "late_off_base_on_time_type": int,
        "late_on_base_on_time_type": int,
    }

    def __init__(self, d=None):
        self.late_off_base_on_time_type: Optional[int] = None
        self.late_on_base_on_time_type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LateOffLateOnSettingBuilder":
        return LateOffLateOnSettingBuilder()


class LateOffLateOnSettingBuilder(object):
    def __init__(self) -> None:
        self._late_off_late_on_setting = LateOffLateOnSetting()

    def late_off_base_on_time_type(self, late_off_base_on_time_type: int) -> "LateOffLateOnSettingBuilder":
        self._late_off_late_on_setting.late_off_base_on_time_type = late_off_base_on_time_type
        return self

    def late_on_base_on_time_type(self, late_on_base_on_time_type: int) -> "LateOffLateOnSettingBuilder":
        self._late_off_late_on_setting.late_on_base_on_time_type = late_on_base_on_time_type
        return self

    def build(self) -> "LateOffLateOnSetting":
        return self._late_off_late_on_setting
