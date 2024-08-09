# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n


class Sentence(object):
    _types = {
        "content": str,
        "speak_time": str,
        "user_type": int,
        "speaker_name": I18n,
    }

    def __init__(self, d=None):
        self.content: Optional[str] = None
        self.speak_time: Optional[str] = None
        self.user_type: Optional[int] = None
        self.speaker_name: Optional[I18n] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SentenceBuilder":
        return SentenceBuilder()


class SentenceBuilder(object):
    def __init__(self) -> None:
        self._sentence = Sentence()

    def content(self, content: str) -> "SentenceBuilder":
        self._sentence.content = content
        return self

    def speak_time(self, speak_time: str) -> "SentenceBuilder":
        self._sentence.speak_time = speak_time
        return self

    def user_type(self, user_type: int) -> "SentenceBuilder":
        self._sentence.user_type = user_type
        return self

    def speaker_name(self, speaker_name: I18n) -> "SentenceBuilder":
        self._sentence.speaker_name = speaker_name
        return self

    def build(self) -> "Sentence":
        return self._sentence
