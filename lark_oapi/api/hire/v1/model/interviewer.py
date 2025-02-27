# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Interviewer(object):
    _types = {
        "user_id": str,
        "verify_status": int,
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        self.verify_status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InterviewerBuilder":
        return InterviewerBuilder()


class InterviewerBuilder(object):
    def __init__(self) -> None:
        self._interviewer = Interviewer()

    def user_id(self, user_id: str) -> "InterviewerBuilder":
        self._interviewer.user_id = user_id
        return self

    def verify_status(self, verify_status: int) -> "InterviewerBuilder":
        self._interviewer.verify_status = verify_status
        return self

    def build(self) -> "Interviewer":
        return self._interviewer
