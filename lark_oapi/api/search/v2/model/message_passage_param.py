# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class MessagePassageParam(object):
    _types = {
        "searchable": bool,
        "chat_ids": List[str],
        "excluded_passage_ids": List[str],
        "excluded_chat_ids": List[str],
        "excluded_message_ids": List[str],
    }

    def __init__(self, d=None):
        self.searchable: Optional[bool] = None
        self.chat_ids: Optional[List[str]] = None
        self.excluded_passage_ids: Optional[List[str]] = None
        self.excluded_chat_ids: Optional[List[str]] = None
        self.excluded_message_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MessagePassageParamBuilder":
        return MessagePassageParamBuilder()


class MessagePassageParamBuilder(object):
    def __init__(self) -> None:
        self._message_passage_param = MessagePassageParam()

    def searchable(self, searchable: bool) -> "MessagePassageParamBuilder":
        self._message_passage_param.searchable = searchable
        return self

    def chat_ids(self, chat_ids: List[str]) -> "MessagePassageParamBuilder":
        self._message_passage_param.chat_ids = chat_ids
        return self

    def excluded_passage_ids(self, excluded_passage_ids: List[str]) -> "MessagePassageParamBuilder":
        self._message_passage_param.excluded_passage_ids = excluded_passage_ids
        return self

    def excluded_chat_ids(self, excluded_chat_ids: List[str]) -> "MessagePassageParamBuilder":
        self._message_passage_param.excluded_chat_ids = excluded_chat_ids
        return self

    def excluded_message_ids(self, excluded_message_ids: List[str]) -> "MessagePassageParamBuilder":
        self._message_passage_param.excluded_message_ids = excluded_message_ids
        return self

    def build(self) -> "MessagePassageParam":
        return self._message_passage_param