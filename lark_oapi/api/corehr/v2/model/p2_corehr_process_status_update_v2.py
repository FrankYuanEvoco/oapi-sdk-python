# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext


class P2CorehrProcessStatusUpdateV2Data(object):
    _types = {
        "process_id": str,
        "status": int,
        "biz_type": str,
        "flow_definition_id": str,
        "properties": int,
    }

    def __init__(self, d=None):
        self.process_id: Optional[str] = None
        self.status: Optional[int] = None
        self.biz_type: Optional[str] = None
        self.flow_definition_id: Optional[str] = None
        self.properties: Optional[int] = None
        init(self, d, self._types)


class P2CorehrProcessStatusUpdateV2(EventContext):
    _types = {
        "event": P2CorehrProcessStatusUpdateV2Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2CorehrProcessStatusUpdateV2Data] = None
        init(self, d, self._types)
