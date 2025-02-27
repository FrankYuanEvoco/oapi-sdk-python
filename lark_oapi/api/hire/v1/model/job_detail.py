# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .job_detail_basic_info import JobDetailBasicInfo
from .job_user_info import JobUserInfo
from .job_user_info import JobUserInfo
from .job_user_info import JobUserInfo
from .job_requirement_simple import JobRequirementSimple
from .common_address import CommonAddress
from .job_config_detail import JobConfigDetail
from .job_storefront import JobStorefront
from .job_detail_tag import JobDetailTag


class JobDetail(object):
    _types = {
        "basic_info": JobDetailBasicInfo,
        "recruiter": JobUserInfo,
        "assistant_list": List[JobUserInfo],
        "hiring_manager_list": List[JobUserInfo],
        "job_requirement_list": List[JobRequirementSimple],
        "address_list": List[CommonAddress],
        "job_config": JobConfigDetail,
        "storefront_list": List[JobStorefront],
        "tag_list": List[JobDetailTag],
    }

    def __init__(self, d=None):
        self.basic_info: Optional[JobDetailBasicInfo] = None
        self.recruiter: Optional[JobUserInfo] = None
        self.assistant_list: Optional[List[JobUserInfo]] = None
        self.hiring_manager_list: Optional[List[JobUserInfo]] = None
        self.job_requirement_list: Optional[List[JobRequirementSimple]] = None
        self.address_list: Optional[List[CommonAddress]] = None
        self.job_config: Optional[JobConfigDetail] = None
        self.storefront_list: Optional[List[JobStorefront]] = None
        self.tag_list: Optional[List[JobDetailTag]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobDetailBuilder":
        return JobDetailBuilder()


class JobDetailBuilder(object):
    def __init__(self) -> None:
        self._job_detail = JobDetail()

    def basic_info(self, basic_info: JobDetailBasicInfo) -> "JobDetailBuilder":
        self._job_detail.basic_info = basic_info
        return self

    def recruiter(self, recruiter: JobUserInfo) -> "JobDetailBuilder":
        self._job_detail.recruiter = recruiter
        return self

    def assistant_list(self, assistant_list: List[JobUserInfo]) -> "JobDetailBuilder":
        self._job_detail.assistant_list = assistant_list
        return self

    def hiring_manager_list(self, hiring_manager_list: List[JobUserInfo]) -> "JobDetailBuilder":
        self._job_detail.hiring_manager_list = hiring_manager_list
        return self

    def job_requirement_list(self, job_requirement_list: List[JobRequirementSimple]) -> "JobDetailBuilder":
        self._job_detail.job_requirement_list = job_requirement_list
        return self

    def address_list(self, address_list: List[CommonAddress]) -> "JobDetailBuilder":
        self._job_detail.address_list = address_list
        return self

    def job_config(self, job_config: JobConfigDetail) -> "JobDetailBuilder":
        self._job_detail.job_config = job_config
        return self

    def storefront_list(self, storefront_list: List[JobStorefront]) -> "JobDetailBuilder":
        self._job_detail.storefront_list = storefront_list
        return self

    def tag_list(self, tag_list: List[JobDetailTag]) -> "JobDetailBuilder":
        self._job_detail.tag_list = tag_list
        return self

    def build(self) -> "JobDetail":
        return self._job_detail
