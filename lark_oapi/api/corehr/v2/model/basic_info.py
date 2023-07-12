# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .name import Name


class BasicInfo(object):
    _types = {
        "name": Name,
        "phone_number": str,
        "international_area_code": str,
        "email": str,
        "date_of_birth": str,
        "personal_id_number": str,
        "date_entered_workforce": str,
        "gender_id": str,
        "nationality_id": str,
        "home_address": str,
        "worker_id": str,
    }

    def __init__(self, d):
        self.name: Optional[Name] = None
        self.phone_number: Optional[str] = None
        self.international_area_code: Optional[str] = None
        self.email: Optional[str] = None
        self.date_of_birth: Optional[str] = None
        self.personal_id_number: Optional[str] = None
        self.date_entered_workforce: Optional[str] = None
        self.gender_id: Optional[str] = None
        self.nationality_id: Optional[str] = None
        self.home_address: Optional[str] = None
        self.worker_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BasicInfoBuilder":
        return BasicInfoBuilder()


class BasicInfoBuilder(object):
    def __init__(self, basic_info: BasicInfo = BasicInfo({})) -> None:
        self._basic_info: BasicInfo = basic_info
    
    def name(self, name: Name) -> "BasicInfoBuilder":
        self._basic_info.name = name
        return self
    
    def phone_number(self, phone_number: str) -> "BasicInfoBuilder":
        self._basic_info.phone_number = phone_number
        return self
    
    def international_area_code(self, international_area_code: str) -> "BasicInfoBuilder":
        self._basic_info.international_area_code = international_area_code
        return self
    
    def email(self, email: str) -> "BasicInfoBuilder":
        self._basic_info.email = email
        return self
    
    def date_of_birth(self, date_of_birth: str) -> "BasicInfoBuilder":
        self._basic_info.date_of_birth = date_of_birth
        return self
    
    def personal_id_number(self, personal_id_number: str) -> "BasicInfoBuilder":
        self._basic_info.personal_id_number = personal_id_number
        return self
    
    def date_entered_workforce(self, date_entered_workforce: str) -> "BasicInfoBuilder":
        self._basic_info.date_entered_workforce = date_entered_workforce
        return self
    
    def gender_id(self, gender_id: str) -> "BasicInfoBuilder":
        self._basic_info.gender_id = gender_id
        return self
    
    def nationality_id(self, nationality_id: str) -> "BasicInfoBuilder":
        self._basic_info.nationality_id = nationality_id
        return self
    
    def home_address(self, home_address: str) -> "BasicInfoBuilder":
        self._basic_info.home_address = home_address
        return self
    
    def worker_id(self, worker_id: str) -> "BasicInfoBuilder":
        self._basic_info.worker_id = worker_id
        return self
    
    def build(self) -> "BasicInfo":
        return self._basic_info