# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class FieldVariableValueToFile(object):
    _types = {
        "open_file_id": str,
        "file_name": str,
        "length": int,
        "mime_type": str,
    }

    def __init__(self, d=None):
        self.open_file_id: Optional[str] = None
        self.file_name: Optional[str] = None
        self.length: Optional[int] = None
        self.mime_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FieldVariableValueToFileBuilder":
        return FieldVariableValueToFileBuilder()


class FieldVariableValueToFileBuilder(object):
    def __init__(self) -> None:
        self._field_variable_value_to_file = FieldVariableValueToFile()

    def open_file_id(self, open_file_id: str) -> "FieldVariableValueToFileBuilder":
        self._field_variable_value_to_file.open_file_id = open_file_id
        return self

    def file_name(self, file_name: str) -> "FieldVariableValueToFileBuilder":
        self._field_variable_value_to_file.file_name = file_name
        return self

    def length(self, length: int) -> "FieldVariableValueToFileBuilder":
        self._field_variable_value_to_file.length = length
        return self

    def mime_type(self, mime_type: str) -> "FieldVariableValueToFileBuilder":
        self._field_variable_value_to_file.mime_type = mime_type
        return self

    def build(self) -> "FieldVariableValueToFile":
        return self._field_variable_value_to_file
