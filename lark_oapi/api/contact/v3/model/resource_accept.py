# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ResourceAccept(object):
    _types = {
        "processing_type": int,
        "acceptor_user_id": int,
    }

    def __init__(self, d=None):
        self.processing_type: Optional[int] = None
        self.acceptor_user_id: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ResourceAcceptBuilder":
        return ResourceAcceptBuilder()


class ResourceAcceptBuilder(object):
    def __init__(self) -> None:
        self._resource_accept = ResourceAccept()

    def processing_type(self, processing_type: int) -> "ResourceAcceptBuilder":
        self._resource_accept.processing_type = processing_type
        return self

    def acceptor_user_id(self, acceptor_user_id: int) -> "ResourceAcceptBuilder":
        self._resource_accept.acceptor_user_id = acceptor_user_id
        return self

    def build(self) -> "ResourceAccept":
        return self._resource_accept
