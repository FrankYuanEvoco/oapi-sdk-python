# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .recognized_entities import RecognizedEntities


class RecognizeBusinessCardResponseBody(object):
    _types = {
        "business_cards": List[RecognizedEntities],
    }

    def __init__(self, d=None):
        self.business_cards: Optional[List[RecognizedEntities]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RecognizeBusinessCardResponseBodyBuilder":
        return RecognizeBusinessCardResponseBodyBuilder()


class RecognizeBusinessCardResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._recognize_business_card_response_body = RecognizeBusinessCardResponseBody()

    def business_cards(self, business_cards: List[RecognizedEntities]) -> "RecognizeBusinessCardResponseBodyBuilder":
        self._recognize_business_card_response_body.business_cards = business_cards
        return self

    def build(self) -> "RecognizeBusinessCardResponseBody":
        return self._recognize_business_card_response_body