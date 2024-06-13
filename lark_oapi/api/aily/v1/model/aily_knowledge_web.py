# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class AilyKnowledgeWeb(object):
    _types = {
        "url": str,
        "title": str,
    }

    def __init__(self, d=None):
        self.url: Optional[str] = None
        self.title: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AilyKnowledgeWebBuilder":
        return AilyKnowledgeWebBuilder()


class AilyKnowledgeWebBuilder(object):
    def __init__(self) -> None:
        self._aily_knowledge_web = AilyKnowledgeWeb()

    def url(self, url: str) -> "AilyKnowledgeWebBuilder":
        self._aily_knowledge_web.url = url
        return self

    def title(self, title: str) -> "AilyKnowledgeWebBuilder":
        self._aily_knowledge_web.title = title
        return self

    def build(self) -> "AilyKnowledgeWeb":
        return self._aily_knowledge_web