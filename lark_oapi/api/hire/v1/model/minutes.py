# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .sentence import Sentence


class Minutes(object):
    _types = {
        "sentences": List[Sentence],
    }

    def __init__(self, d=None):
        self.sentences: Optional[List[Sentence]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MinutesBuilder":
        return MinutesBuilder()


class MinutesBuilder(object):
    def __init__(self) -> None:
        self._minutes = Minutes()

    def sentences(self, sentences: List[Sentence]) -> "MinutesBuilder":
        self._minutes.sentences = sentences
        return self

    def build(self) -> "Minutes":
        return self._minutes
