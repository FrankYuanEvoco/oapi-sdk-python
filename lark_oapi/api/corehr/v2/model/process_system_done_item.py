# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .process_link import ProcessLink
from .dataengine_i18n import DataengineI18n
from .dataengine_i18n import DataengineI18n


class ProcessSystemDoneItem(object):
    _types = {
        "approver_id": str,
        "type": int,
        "status": int,
        "links": ProcessLink,
        "operator_name": DataengineI18n,
        "node_name": DataengineI18n,
        "create_time": str,
        "complete_time": str,
        "node_definition_id": str,
    }

    def __init__(self, d=None):
        self.approver_id: Optional[str] = None
        self.type: Optional[int] = None
        self.status: Optional[int] = None
        self.links: Optional[ProcessLink] = None
        self.operator_name: Optional[DataengineI18n] = None
        self.node_name: Optional[DataengineI18n] = None
        self.create_time: Optional[str] = None
        self.complete_time: Optional[str] = None
        self.node_definition_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProcessSystemDoneItemBuilder":
        return ProcessSystemDoneItemBuilder()


class ProcessSystemDoneItemBuilder(object):
    def __init__(self) -> None:
        self._process_system_done_item = ProcessSystemDoneItem()

    def approver_id(self, approver_id: str) -> "ProcessSystemDoneItemBuilder":
        self._process_system_done_item.approver_id = approver_id
        return self

    def type(self, type: int) -> "ProcessSystemDoneItemBuilder":
        self._process_system_done_item.type = type
        return self

    def status(self, status: int) -> "ProcessSystemDoneItemBuilder":
        self._process_system_done_item.status = status
        return self

    def links(self, links: ProcessLink) -> "ProcessSystemDoneItemBuilder":
        self._process_system_done_item.links = links
        return self

    def operator_name(self, operator_name: DataengineI18n) -> "ProcessSystemDoneItemBuilder":
        self._process_system_done_item.operator_name = operator_name
        return self

    def node_name(self, node_name: DataengineI18n) -> "ProcessSystemDoneItemBuilder":
        self._process_system_done_item.node_name = node_name
        return self

    def create_time(self, create_time: str) -> "ProcessSystemDoneItemBuilder":
        self._process_system_done_item.create_time = create_time
        return self

    def complete_time(self, complete_time: str) -> "ProcessSystemDoneItemBuilder":
        self._process_system_done_item.complete_time = complete_time
        return self

    def node_definition_id(self, node_definition_id: str) -> "ProcessSystemDoneItemBuilder":
        self._process_system_done_item.node_definition_id = node_definition_id
        return self

    def build(self) -> "ProcessSystemDoneItem":
        return self._process_system_done_item
