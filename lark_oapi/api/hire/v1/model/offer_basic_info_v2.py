# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .basic_user_info import BasicUserInfo
from .id_name_object import IdNameObject
from .basic_department_info import BasicDepartmentInfo
from .id_name_object import IdNameObject
from .id_name_object import IdNameObject
from .id_name_object import IdNameObject
from .contract_period_info import ContractPeriodInfo
from .basic_user_info import BasicUserInfo
from .base_address_v2 import BaseAddressV2
from .base_address_v2 import BaseAddressV2
from .offer_attachment_info import OfferAttachmentInfo
from .application_offer_custom_value import ApplicationOfferCustomValue


class OfferBasicInfoV2(object):
    _types = {
        "id": str,
        "offer_type": int,
        "offer_status": int,
        "leader": BasicUserInfo,
        "employee_type": IdNameObject,
        "department": BasicDepartmentInfo,
        "sequence": IdNameObject,
        "level": IdNameObject,
        "company_main_body": IdNameObject,
        "job_requirement_id": str,
        "probation_month": int,
        "contract_period": ContractPeriodInfo,
        "onboard_date": str,
        "owner": BasicUserInfo,
        "onboard_address": BaseAddressV2,
        "work_address": BaseAddressV2,
        "remark": str,
        "attachment_list": List[OfferAttachmentInfo],
        "customize_info_list": List[ApplicationOfferCustomValue],
        "create_time": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.offer_type: Optional[int] = None
        self.offer_status: Optional[int] = None
        self.leader: Optional[BasicUserInfo] = None
        self.employee_type: Optional[IdNameObject] = None
        self.department: Optional[BasicDepartmentInfo] = None
        self.sequence: Optional[IdNameObject] = None
        self.level: Optional[IdNameObject] = None
        self.company_main_body: Optional[IdNameObject] = None
        self.job_requirement_id: Optional[str] = None
        self.probation_month: Optional[int] = None
        self.contract_period: Optional[ContractPeriodInfo] = None
        self.onboard_date: Optional[str] = None
        self.owner: Optional[BasicUserInfo] = None
        self.onboard_address: Optional[BaseAddressV2] = None
        self.work_address: Optional[BaseAddressV2] = None
        self.remark: Optional[str] = None
        self.attachment_list: Optional[List[OfferAttachmentInfo]] = None
        self.customize_info_list: Optional[List[ApplicationOfferCustomValue]] = None
        self.create_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OfferBasicInfoV2Builder":
        return OfferBasicInfoV2Builder()


class OfferBasicInfoV2Builder(object):
    def __init__(self) -> None:
        self._offer_basic_info_v2 = OfferBasicInfoV2()

    def id(self, id: str) -> "OfferBasicInfoV2Builder":
        self._offer_basic_info_v2.id = id
        return self

    def offer_type(self, offer_type: int) -> "OfferBasicInfoV2Builder":
        self._offer_basic_info_v2.offer_type = offer_type
        return self

    def offer_status(self, offer_status: int) -> "OfferBasicInfoV2Builder":
        self._offer_basic_info_v2.offer_status = offer_status
        return self

    def leader(self, leader: BasicUserInfo) -> "OfferBasicInfoV2Builder":
        self._offer_basic_info_v2.leader = leader
        return self

    def employee_type(self, employee_type: IdNameObject) -> "OfferBasicInfoV2Builder":
        self._offer_basic_info_v2.employee_type = employee_type
        return self

    def department(self, department: BasicDepartmentInfo) -> "OfferBasicInfoV2Builder":
        self._offer_basic_info_v2.department = department
        return self

    def sequence(self, sequence: IdNameObject) -> "OfferBasicInfoV2Builder":
        self._offer_basic_info_v2.sequence = sequence
        return self

    def level(self, level: IdNameObject) -> "OfferBasicInfoV2Builder":
        self._offer_basic_info_v2.level = level
        return self

    def company_main_body(self, company_main_body: IdNameObject) -> "OfferBasicInfoV2Builder":
        self._offer_basic_info_v2.company_main_body = company_main_body
        return self

    def job_requirement_id(self, job_requirement_id: str) -> "OfferBasicInfoV2Builder":
        self._offer_basic_info_v2.job_requirement_id = job_requirement_id
        return self

    def probation_month(self, probation_month: int) -> "OfferBasicInfoV2Builder":
        self._offer_basic_info_v2.probation_month = probation_month
        return self

    def contract_period(self, contract_period: ContractPeriodInfo) -> "OfferBasicInfoV2Builder":
        self._offer_basic_info_v2.contract_period = contract_period
        return self

    def onboard_date(self, onboard_date: str) -> "OfferBasicInfoV2Builder":
        self._offer_basic_info_v2.onboard_date = onboard_date
        return self

    def owner(self, owner: BasicUserInfo) -> "OfferBasicInfoV2Builder":
        self._offer_basic_info_v2.owner = owner
        return self

    def onboard_address(self, onboard_address: BaseAddressV2) -> "OfferBasicInfoV2Builder":
        self._offer_basic_info_v2.onboard_address = onboard_address
        return self

    def work_address(self, work_address: BaseAddressV2) -> "OfferBasicInfoV2Builder":
        self._offer_basic_info_v2.work_address = work_address
        return self

    def remark(self, remark: str) -> "OfferBasicInfoV2Builder":
        self._offer_basic_info_v2.remark = remark
        return self

    def attachment_list(self, attachment_list: List[OfferAttachmentInfo]) -> "OfferBasicInfoV2Builder":
        self._offer_basic_info_v2.attachment_list = attachment_list
        return self

    def customize_info_list(self, customize_info_list: List[ApplicationOfferCustomValue]) -> "OfferBasicInfoV2Builder":
        self._offer_basic_info_v2.customize_info_list = customize_info_list
        return self

    def create_time(self, create_time: str) -> "OfferBasicInfoV2Builder":
        self._offer_basic_info_v2.create_time = create_time
        return self

    def build(self) -> "OfferBasicInfoV2":
        return self._offer_basic_info_v2
