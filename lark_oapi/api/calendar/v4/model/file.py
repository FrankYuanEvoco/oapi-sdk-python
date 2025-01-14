# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class File(object):
    _types = {
        "file_token": str,
        "file_size": str,
        "name": str,
    }

    def __init__(self, d=None):
        self.file_token: Optional[str] = None
        self.file_size: Optional[str] = None
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FileBuilder":
        return FileBuilder()


class FileBuilder(object):
    def __init__(self) -> None:
        self._file = File()

    def file_token(self, file_token: str) -> "FileBuilder":
        self._file.file_token = file_token
        return self

    def file_size(self, file_size: str) -> "FileBuilder":
        self._file.file_size = file_size
        return self

    def name(self, name: str) -> "FileBuilder":
        self._file.name = name
        return self

    def build(self) -> "File":
        return self._file
