# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class MyaiReply(object):
    _types = {
        "reply": str,
    }

    def __init__(self, d=None):
        self.reply: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MyaiReplyBuilder":
        return MyaiReplyBuilder()


class MyaiReplyBuilder(object):
    def __init__(self) -> None:
        self._myai_reply = MyaiReply()

    def reply(self, reply: str) -> "MyaiReplyBuilder":
        self._myai_reply.reply = reply
        return self

    def build(self) -> "MyaiReply":
        return self._myai_reply