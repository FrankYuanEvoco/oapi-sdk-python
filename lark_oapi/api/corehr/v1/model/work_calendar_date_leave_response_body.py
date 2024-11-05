# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .wk_calendar_date import WkCalendarDate


class WorkCalendarDateLeaveResponseBody(object):
    _types = {
        "calendar_dates": List[WkCalendarDate],
    }

    def __init__(self, d=None):
        self.calendar_dates: Optional[List[WkCalendarDate]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WorkCalendarDateLeaveResponseBodyBuilder":
        return WorkCalendarDateLeaveResponseBodyBuilder()


class WorkCalendarDateLeaveResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._work_calendar_date_leave_response_body = WorkCalendarDateLeaveResponseBody()

    def calendar_dates(self, calendar_dates: List[WkCalendarDate]) -> "WorkCalendarDateLeaveResponseBodyBuilder":
        self._work_calendar_date_leave_response_body.calendar_dates = calendar_dates
        return self

    def build(self) -> "WorkCalendarDateLeaveResponseBody":
        return self._work_calendar_date_leave_response_body