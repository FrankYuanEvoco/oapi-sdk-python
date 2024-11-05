# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .application_stage_info import ApplicationStageInfo
from .application_resume_source import ApplicationResumeSource
from .application_website_resume_source import ApplicationWebsiteResumeSource
from .application_stage_time import ApplicationStageTime
from .code_name_object import CodeNameObject
from .termination_reason_info import TerminationReasonInfo


class ApplicationDetailBasicInfo(object):
    _types = {
        "id": str,
        "job_id": str,
        "talent_id": str,
        "stage": ApplicationStageInfo,
        "active_status": int,
        "delivery_type": int,
        "resume_source_info": ApplicationResumeSource,
        "website_resume_source": ApplicationWebsiteResumeSource,
        "talent_attachment_resume_id": str,
        "stage_time_list": List[ApplicationStageTime],
        "onboard_status": int,
        "application_preferred_city_list": List[CodeNameObject],
        "termination_reason": TerminationReasonInfo,
        "creator_id": str,
        "owner_id": str,
        "terminator_id": str,
        "create_time": str,
        "modify_time": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.job_id: Optional[str] = None
        self.talent_id: Optional[str] = None
        self.stage: Optional[ApplicationStageInfo] = None
        self.active_status: Optional[int] = None
        self.delivery_type: Optional[int] = None
        self.resume_source_info: Optional[ApplicationResumeSource] = None
        self.website_resume_source: Optional[ApplicationWebsiteResumeSource] = None
        self.talent_attachment_resume_id: Optional[str] = None
        self.stage_time_list: Optional[List[ApplicationStageTime]] = None
        self.onboard_status: Optional[int] = None
        self.application_preferred_city_list: Optional[List[CodeNameObject]] = None
        self.termination_reason: Optional[TerminationReasonInfo] = None
        self.creator_id: Optional[str] = None
        self.owner_id: Optional[str] = None
        self.terminator_id: Optional[str] = None
        self.create_time: Optional[str] = None
        self.modify_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationDetailBasicInfoBuilder":
        return ApplicationDetailBasicInfoBuilder()


class ApplicationDetailBasicInfoBuilder(object):
    def __init__(self) -> None:
        self._application_detail_basic_info = ApplicationDetailBasicInfo()

    def id(self, id: str) -> "ApplicationDetailBasicInfoBuilder":
        self._application_detail_basic_info.id = id
        return self

    def job_id(self, job_id: str) -> "ApplicationDetailBasicInfoBuilder":
        self._application_detail_basic_info.job_id = job_id
        return self

    def talent_id(self, talent_id: str) -> "ApplicationDetailBasicInfoBuilder":
        self._application_detail_basic_info.talent_id = talent_id
        return self

    def stage(self, stage: ApplicationStageInfo) -> "ApplicationDetailBasicInfoBuilder":
        self._application_detail_basic_info.stage = stage
        return self

    def active_status(self, active_status: int) -> "ApplicationDetailBasicInfoBuilder":
        self._application_detail_basic_info.active_status = active_status
        return self

    def delivery_type(self, delivery_type: int) -> "ApplicationDetailBasicInfoBuilder":
        self._application_detail_basic_info.delivery_type = delivery_type
        return self

    def resume_source_info(self, resume_source_info: ApplicationResumeSource) -> "ApplicationDetailBasicInfoBuilder":
        self._application_detail_basic_info.resume_source_info = resume_source_info
        return self

    def website_resume_source(self,
                              website_resume_source: ApplicationWebsiteResumeSource) -> "ApplicationDetailBasicInfoBuilder":
        self._application_detail_basic_info.website_resume_source = website_resume_source
        return self

    def talent_attachment_resume_id(self, talent_attachment_resume_id: str) -> "ApplicationDetailBasicInfoBuilder":
        self._application_detail_basic_info.talent_attachment_resume_id = talent_attachment_resume_id
        return self

    def stage_time_list(self, stage_time_list: List[ApplicationStageTime]) -> "ApplicationDetailBasicInfoBuilder":
        self._application_detail_basic_info.stage_time_list = stage_time_list
        return self

    def onboard_status(self, onboard_status: int) -> "ApplicationDetailBasicInfoBuilder":
        self._application_detail_basic_info.onboard_status = onboard_status
        return self

    def application_preferred_city_list(self, application_preferred_city_list: List[
        CodeNameObject]) -> "ApplicationDetailBasicInfoBuilder":
        self._application_detail_basic_info.application_preferred_city_list = application_preferred_city_list
        return self

    def termination_reason(self, termination_reason: TerminationReasonInfo) -> "ApplicationDetailBasicInfoBuilder":
        self._application_detail_basic_info.termination_reason = termination_reason
        return self

    def creator_id(self, creator_id: str) -> "ApplicationDetailBasicInfoBuilder":
        self._application_detail_basic_info.creator_id = creator_id
        return self

    def owner_id(self, owner_id: str) -> "ApplicationDetailBasicInfoBuilder":
        self._application_detail_basic_info.owner_id = owner_id
        return self

    def terminator_id(self, terminator_id: str) -> "ApplicationDetailBasicInfoBuilder":
        self._application_detail_basic_info.terminator_id = terminator_id
        return self

    def create_time(self, create_time: str) -> "ApplicationDetailBasicInfoBuilder":
        self._application_detail_basic_info.create_time = create_time
        return self

    def modify_time(self, modify_time: str) -> "ApplicationDetailBasicInfoBuilder":
        self._application_detail_basic_info.modify_time = modify_time
        return self

    def build(self) -> "ApplicationDetailBasicInfo":
        return self._application_detail_basic_info