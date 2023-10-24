# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class DocHeading(object):
    _types = {
        "text": str,
        "heading_level": int,
    }

    def __init__(self, d=None):
        self.text: Optional[str] = None
        self.heading_level: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DocHeadingBuilder":
        return DocHeadingBuilder()


class DocHeadingBuilder(object):
    def __init__(self) -> None:
        self._doc_heading = DocHeading()

    def text(self, text: str) -> "DocHeadingBuilder":
        self._doc_heading.text = text
        return self

    def heading_level(self, heading_level: int) -> "DocHeadingBuilder":
        self._doc_heading.heading_level = heading_level
        return self

    def build(self) -> "DocHeading":
        return self._doc_heading