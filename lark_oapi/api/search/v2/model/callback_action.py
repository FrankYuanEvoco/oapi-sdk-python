# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .callback_action_value import CallbackActionValue


class CallbackAction(object):
    _types = {
        "tag": str,
        "value": CallbackActionValue,
    }

    def __init__(self, d=None):
        self.tag: Optional[str] = None
        self.value: Optional[CallbackActionValue] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CallbackActionBuilder":
        return CallbackActionBuilder()


class CallbackActionBuilder(object):
    def __init__(self) -> None:
        self._callback_action = CallbackAction()

    def tag(self, tag: str) -> "CallbackActionBuilder":
        self._callback_action.tag = tag
        return self

    def value(self, value: CallbackActionValue) -> "CallbackActionBuilder":
        self._callback_action.value = value
        return self

    def build(self) -> "CallbackAction":
        return self._callback_action