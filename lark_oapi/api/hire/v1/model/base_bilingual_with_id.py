# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class BaseBilingualWithId(object):
    _types = {
        "id": str,
        "zh_name": str,
        "en_name": str,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.zh_name: Optional[str] = None
        self.en_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BaseBilingualWithIdBuilder":
        return BaseBilingualWithIdBuilder()


class BaseBilingualWithIdBuilder(object):
    def __init__(self, base_bilingual_with_id: BaseBilingualWithId = BaseBilingualWithId({})) -> None:
        self._base_bilingual_with_id: BaseBilingualWithId = base_bilingual_with_id
    
    def id(self, id: str) -> "BaseBilingualWithIdBuilder":
        self._base_bilingual_with_id.id = id
        return self
    
    def zh_name(self, zh_name: str) -> "BaseBilingualWithIdBuilder":
        self._base_bilingual_with_id.zh_name = zh_name
        return self
    
    def en_name(self, en_name: str) -> "BaseBilingualWithIdBuilder":
        self._base_bilingual_with_id.en_name = en_name
        return self
    
    def build(self) -> "BaseBilingualWithId":
        return self._base_bilingual_with_id