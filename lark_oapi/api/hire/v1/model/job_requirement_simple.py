# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class JobRequirementSimple(object):
    _types = {
        "id": str,
        "short_code": str,
        "name": str,
        "department_id": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.short_code: Optional[str] = None
        self.name: Optional[str] = None
        self.department_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobRequirementSimpleBuilder":
        return JobRequirementSimpleBuilder()


class JobRequirementSimpleBuilder(object):
    def __init__(self) -> None:
        self._job_requirement_simple = JobRequirementSimple()

    def id(self, id: str) -> "JobRequirementSimpleBuilder":
        self._job_requirement_simple.id = id
        return self

    def short_code(self, short_code: str) -> "JobRequirementSimpleBuilder":
        self._job_requirement_simple.short_code = short_code
        return self

    def name(self, name: str) -> "JobRequirementSimpleBuilder":
        self._job_requirement_simple.name = name
        return self

    def department_id(self, department_id: str) -> "JobRequirementSimpleBuilder":
        self._job_requirement_simple.department_id = department_id
        return self

    def build(self) -> "JobRequirementSimple":
        return self._job_requirement_simple
