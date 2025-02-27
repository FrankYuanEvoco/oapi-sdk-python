# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n
from .i18n import I18n
from .leave_request_detail import LeaveRequestDetail
from .leave_process_info import LeaveProcessInfo


class LeaveRequest(object):
    _types = {
        "leave_request_id": str,
        "employment_id": str,
        "employment_name": List[I18n],
        "leave_type_id": str,
        "leave_type_name": List[I18n],
        "start_time": str,
        "end_time": str,
        "leave_duration": str,
        "leave_duration_unit": int,
        "leave_request_status": int,
        "grant_source": str,
        "return_time": str,
        "submitted_at": str,
        "submitted_by": str,
        "notes": str,
        "approval_date": str,
        "is_deducted": bool,
        "details": List[LeaveRequestDetail],
        "leave_type_code": str,
        "actual_end_date": str,
        "estimated_end_date": str,
        "time_zone": str,
        "data_source": int,
        "leave_process_id": List[str],
        "leave_correct_process_id": List[str],
        "leave_cancel_process_id": List[str],
        "leave_return_process_id": List[str],
        "wd_paid_type": int,
        "leave_correct_process_info": List[LeaveProcessInfo],
    }

    def __init__(self, d=None):
        self.leave_request_id: Optional[str] = None
        self.employment_id: Optional[str] = None
        self.employment_name: Optional[List[I18n]] = None
        self.leave_type_id: Optional[str] = None
        self.leave_type_name: Optional[List[I18n]] = None
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        self.leave_duration: Optional[str] = None
        self.leave_duration_unit: Optional[int] = None
        self.leave_request_status: Optional[int] = None
        self.grant_source: Optional[str] = None
        self.return_time: Optional[str] = None
        self.submitted_at: Optional[str] = None
        self.submitted_by: Optional[str] = None
        self.notes: Optional[str] = None
        self.approval_date: Optional[str] = None
        self.is_deducted: Optional[bool] = None
        self.details: Optional[List[LeaveRequestDetail]] = None
        self.leave_type_code: Optional[str] = None
        self.actual_end_date: Optional[str] = None
        self.estimated_end_date: Optional[str] = None
        self.time_zone: Optional[str] = None
        self.data_source: Optional[int] = None
        self.leave_process_id: Optional[List[str]] = None
        self.leave_correct_process_id: Optional[List[str]] = None
        self.leave_cancel_process_id: Optional[List[str]] = None
        self.leave_return_process_id: Optional[List[str]] = None
        self.wd_paid_type: Optional[int] = None
        self.leave_correct_process_info: Optional[List[LeaveProcessInfo]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LeaveRequestBuilder":
        return LeaveRequestBuilder()


class LeaveRequestBuilder(object):
    def __init__(self) -> None:
        self._leave_request = LeaveRequest()

    def leave_request_id(self, leave_request_id: str) -> "LeaveRequestBuilder":
        self._leave_request.leave_request_id = leave_request_id
        return self

    def employment_id(self, employment_id: str) -> "LeaveRequestBuilder":
        self._leave_request.employment_id = employment_id
        return self

    def employment_name(self, employment_name: List[I18n]) -> "LeaveRequestBuilder":
        self._leave_request.employment_name = employment_name
        return self

    def leave_type_id(self, leave_type_id: str) -> "LeaveRequestBuilder":
        self._leave_request.leave_type_id = leave_type_id
        return self

    def leave_type_name(self, leave_type_name: List[I18n]) -> "LeaveRequestBuilder":
        self._leave_request.leave_type_name = leave_type_name
        return self

    def start_time(self, start_time: str) -> "LeaveRequestBuilder":
        self._leave_request.start_time = start_time
        return self

    def end_time(self, end_time: str) -> "LeaveRequestBuilder":
        self._leave_request.end_time = end_time
        return self

    def leave_duration(self, leave_duration: str) -> "LeaveRequestBuilder":
        self._leave_request.leave_duration = leave_duration
        return self

    def leave_duration_unit(self, leave_duration_unit: int) -> "LeaveRequestBuilder":
        self._leave_request.leave_duration_unit = leave_duration_unit
        return self

    def leave_request_status(self, leave_request_status: int) -> "LeaveRequestBuilder":
        self._leave_request.leave_request_status = leave_request_status
        return self

    def grant_source(self, grant_source: str) -> "LeaveRequestBuilder":
        self._leave_request.grant_source = grant_source
        return self

    def return_time(self, return_time: str) -> "LeaveRequestBuilder":
        self._leave_request.return_time = return_time
        return self

    def submitted_at(self, submitted_at: str) -> "LeaveRequestBuilder":
        self._leave_request.submitted_at = submitted_at
        return self

    def submitted_by(self, submitted_by: str) -> "LeaveRequestBuilder":
        self._leave_request.submitted_by = submitted_by
        return self

    def notes(self, notes: str) -> "LeaveRequestBuilder":
        self._leave_request.notes = notes
        return self

    def approval_date(self, approval_date: str) -> "LeaveRequestBuilder":
        self._leave_request.approval_date = approval_date
        return self

    def is_deducted(self, is_deducted: bool) -> "LeaveRequestBuilder":
        self._leave_request.is_deducted = is_deducted
        return self

    def details(self, details: List[LeaveRequestDetail]) -> "LeaveRequestBuilder":
        self._leave_request.details = details
        return self

    def leave_type_code(self, leave_type_code: str) -> "LeaveRequestBuilder":
        self._leave_request.leave_type_code = leave_type_code
        return self

    def actual_end_date(self, actual_end_date: str) -> "LeaveRequestBuilder":
        self._leave_request.actual_end_date = actual_end_date
        return self

    def estimated_end_date(self, estimated_end_date: str) -> "LeaveRequestBuilder":
        self._leave_request.estimated_end_date = estimated_end_date
        return self

    def time_zone(self, time_zone: str) -> "LeaveRequestBuilder":
        self._leave_request.time_zone = time_zone
        return self

    def data_source(self, data_source: int) -> "LeaveRequestBuilder":
        self._leave_request.data_source = data_source
        return self

    def leave_process_id(self, leave_process_id: List[str]) -> "LeaveRequestBuilder":
        self._leave_request.leave_process_id = leave_process_id
        return self

    def leave_correct_process_id(self, leave_correct_process_id: List[str]) -> "LeaveRequestBuilder":
        self._leave_request.leave_correct_process_id = leave_correct_process_id
        return self

    def leave_cancel_process_id(self, leave_cancel_process_id: List[str]) -> "LeaveRequestBuilder":
        self._leave_request.leave_cancel_process_id = leave_cancel_process_id
        return self

    def leave_return_process_id(self, leave_return_process_id: List[str]) -> "LeaveRequestBuilder":
        self._leave_request.leave_return_process_id = leave_return_process_id
        return self

    def wd_paid_type(self, wd_paid_type: int) -> "LeaveRequestBuilder":
        self._leave_request.wd_paid_type = wd_paid_type
        return self

    def leave_correct_process_info(self, leave_correct_process_info: List[LeaveProcessInfo]) -> "LeaveRequestBuilder":
        self._leave_request.leave_correct_process_info = leave_correct_process_info
        return self

    def build(self) -> "LeaveRequest":
        return self._leave_request
