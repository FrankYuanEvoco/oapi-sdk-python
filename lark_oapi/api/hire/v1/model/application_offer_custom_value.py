# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class ApplicationOfferCustomValue(object):
    _types = {
        "object_id": str,
        "customize_value": str,
    }

    def __init__(self, d):
        self.object_id: Optional[str] = None
        self.customize_value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationOfferCustomValueBuilder":
        return ApplicationOfferCustomValueBuilder()


class ApplicationOfferCustomValueBuilder(object):
    def __init__(self, application_offer_custom_value: ApplicationOfferCustomValue = ApplicationOfferCustomValue({})) -> None:
        self._application_offer_custom_value: ApplicationOfferCustomValue = application_offer_custom_value
    
    def object_id(self, object_id: str) -> "ApplicationOfferCustomValueBuilder":
        self._application_offer_custom_value.object_id = object_id
        return self
    
    def customize_value(self, customize_value: str) -> "ApplicationOfferCustomValueBuilder":
        self._application_offer_custom_value.customize_value = customize_value
        return self
    
    def build(self) -> "ApplicationOfferCustomValue":
        return self._application_offer_custom_value