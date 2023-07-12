# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class EcoBackgroundCheckCreateEventMobile(object):
    _types = {
        "code": str,
        "number": str,
    }

    def __init__(self, d):
        self.code: Optional[str] = None
        self.number: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EcoBackgroundCheckCreateEventMobileBuilder":
        return EcoBackgroundCheckCreateEventMobileBuilder()


class EcoBackgroundCheckCreateEventMobileBuilder(object):
    def __init__(self, eco_background_check_create_event_mobile: EcoBackgroundCheckCreateEventMobile = EcoBackgroundCheckCreateEventMobile({})) -> None:
        self._eco_background_check_create_event_mobile: EcoBackgroundCheckCreateEventMobile = eco_background_check_create_event_mobile
    
    def code(self, code: str) -> "EcoBackgroundCheckCreateEventMobileBuilder":
        self._eco_background_check_create_event_mobile.code = code
        return self
    
    def number(self, number: str) -> "EcoBackgroundCheckCreateEventMobileBuilder":
        self._eco_background_check_create_event_mobile.number = number
        return self
    
    def build(self) -> "EcoBackgroundCheckCreateEventMobile":
        return self._eco_background_check_create_event_mobile