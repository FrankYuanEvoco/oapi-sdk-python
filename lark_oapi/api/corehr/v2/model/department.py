# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n
from .enum import Enum
from .i18n import I18n
from .custom_field_data import CustomFieldData
from .enum import Enum


class Department(object):
    _types = {
        "id": str,
        "version_id": str,
        "department_name": List[I18n],
        "sub_type": Enum,
        "parent_department_id": str,
        "manager": str,
        "tree_order": str,
        "list_order": str,
        "code": str,
        "is_root": bool,
        "is_confidential": bool,
        "effective_date": str,
        "expiration_date": str,
        "active": bool,
        "description": List[I18n],
        "custom_fields": List[CustomFieldData],
        "staffing_model": Enum,
        "cost_center_id": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.version_id: Optional[str] = None
        self.department_name: Optional[List[I18n]] = None
        self.sub_type: Optional[Enum] = None
        self.parent_department_id: Optional[str] = None
        self.manager: Optional[str] = None
        self.tree_order: Optional[str] = None
        self.list_order: Optional[str] = None
        self.code: Optional[str] = None
        self.is_root: Optional[bool] = None
        self.is_confidential: Optional[bool] = None
        self.effective_date: Optional[str] = None
        self.expiration_date: Optional[str] = None
        self.active: Optional[bool] = None
        self.description: Optional[List[I18n]] = None
        self.custom_fields: Optional[List[CustomFieldData]] = None
        self.staffing_model: Optional[Enum] = None
        self.cost_center_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DepartmentBuilder":
        return DepartmentBuilder()


class DepartmentBuilder(object):
    def __init__(self) -> None:
        self._department = Department()

    def id(self, id: str) -> "DepartmentBuilder":
        self._department.id = id
        return self

    def version_id(self, version_id: str) -> "DepartmentBuilder":
        self._department.version_id = version_id
        return self

    def department_name(self, department_name: List[I18n]) -> "DepartmentBuilder":
        self._department.department_name = department_name
        return self

    def sub_type(self, sub_type: Enum) -> "DepartmentBuilder":
        self._department.sub_type = sub_type
        return self

    def parent_department_id(self, parent_department_id: str) -> "DepartmentBuilder":
        self._department.parent_department_id = parent_department_id
        return self

    def manager(self, manager: str) -> "DepartmentBuilder":
        self._department.manager = manager
        return self

    def tree_order(self, tree_order: str) -> "DepartmentBuilder":
        self._department.tree_order = tree_order
        return self

    def list_order(self, list_order: str) -> "DepartmentBuilder":
        self._department.list_order = list_order
        return self

    def code(self, code: str) -> "DepartmentBuilder":
        self._department.code = code
        return self

    def is_root(self, is_root: bool) -> "DepartmentBuilder":
        self._department.is_root = is_root
        return self

    def is_confidential(self, is_confidential: bool) -> "DepartmentBuilder":
        self._department.is_confidential = is_confidential
        return self

    def effective_date(self, effective_date: str) -> "DepartmentBuilder":
        self._department.effective_date = effective_date
        return self

    def expiration_date(self, expiration_date: str) -> "DepartmentBuilder":
        self._department.expiration_date = expiration_date
        return self

    def active(self, active: bool) -> "DepartmentBuilder":
        self._department.active = active
        return self

    def description(self, description: List[I18n]) -> "DepartmentBuilder":
        self._department.description = description
        return self

    def custom_fields(self, custom_fields: List[CustomFieldData]) -> "DepartmentBuilder":
        self._department.custom_fields = custom_fields
        return self

    def staffing_model(self, staffing_model: Enum) -> "DepartmentBuilder":
        self._department.staffing_model = staffing_model
        return self

    def cost_center_id(self, cost_center_id: str) -> "DepartmentBuilder":
        self._department.cost_center_id = cost_center_id
        return self

    def build(self) -> "Department":
        return self._department
