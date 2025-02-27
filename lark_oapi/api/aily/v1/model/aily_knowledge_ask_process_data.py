# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class AilyKnowledgeAskProcessData(object):
    _types = {
        "chart_dsls": List[str],
        "chunks": List[str],
        "sql_data": List[str],
    }

    def __init__(self, d=None):
        self.chart_dsls: Optional[List[str]] = None
        self.chunks: Optional[List[str]] = None
        self.sql_data: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AilyKnowledgeAskProcessDataBuilder":
        return AilyKnowledgeAskProcessDataBuilder()


class AilyKnowledgeAskProcessDataBuilder(object):
    def __init__(self) -> None:
        self._aily_knowledge_ask_process_data = AilyKnowledgeAskProcessData()

    def chart_dsls(self, chart_dsls: List[str]) -> "AilyKnowledgeAskProcessDataBuilder":
        self._aily_knowledge_ask_process_data.chart_dsls = chart_dsls
        return self

    def chunks(self, chunks: List[str]) -> "AilyKnowledgeAskProcessDataBuilder":
        self._aily_knowledge_ask_process_data.chunks = chunks
        return self

    def sql_data(self, sql_data: List[str]) -> "AilyKnowledgeAskProcessDataBuilder":
        self._aily_knowledge_ask_process_data.sql_data = sql_data
        return self

    def build(self) -> "AilyKnowledgeAskProcessData":
        return self._aily_knowledge_ask_process_data
