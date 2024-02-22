# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class PatchPeriodResponseBody(object):
    _types = {
        "period_id": str,
        "status": int,
    }

    def __init__(self, d=None):
        self.period_id: Optional[str] = None
        self.status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchPeriodResponseBodyBuilder":
        return PatchPeriodResponseBodyBuilder()


class PatchPeriodResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_period_response_body = PatchPeriodResponseBody()

    def period_id(self, period_id: str) -> "PatchPeriodResponseBodyBuilder":
        self._patch_period_response_body.period_id = period_id
        return self

    def status(self, status: int) -> "PatchPeriodResponseBodyBuilder":
        self._patch_period_response_body.status = status
        return self

    def build(self) -> "PatchPeriodResponseBody":
        return self._patch_period_response_body