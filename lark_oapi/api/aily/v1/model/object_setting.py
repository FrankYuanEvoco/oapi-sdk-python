# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ObjectSetting(object):
    _types = {
        "display_name": str,
        "field_orders": List[str],
    }

    def __init__(self, d=None):
        self.display_name: Optional[str] = None
        self.field_orders: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ObjectSettingBuilder":
        return ObjectSettingBuilder()


class ObjectSettingBuilder(object):
    def __init__(self) -> None:
        self._object_setting = ObjectSetting()

    def display_name(self, display_name: str) -> "ObjectSettingBuilder":
        self._object_setting.display_name = display_name
        return self

    def field_orders(self, field_orders: List[str]) -> "ObjectSettingBuilder":
        self._object_setting.field_orders = field_orders
        return self

    def build(self) -> "ObjectSetting":
        return self._object_setting
