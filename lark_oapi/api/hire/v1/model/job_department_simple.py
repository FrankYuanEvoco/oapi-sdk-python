# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n


class JobDepartmentSimple(object):
    _types = {
        "id": str,
        "name": I18n,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobDepartmentSimpleBuilder":
        return JobDepartmentSimpleBuilder()


class JobDepartmentSimpleBuilder(object):
    def __init__(self) -> None:
        self._job_department_simple = JobDepartmentSimple()

    def id(self, id: str) -> "JobDepartmentSimpleBuilder":
        self._job_department_simple.id = id
        return self

    def name(self, name: I18n) -> "JobDepartmentSimpleBuilder":
        self._job_department_simple.name = name
        return self

    def build(self) -> "JobDepartmentSimple":
        return self._job_department_simple
