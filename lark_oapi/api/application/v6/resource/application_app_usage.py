# Code generated by Lark OpenAPI.

import io
from typing import *
from typing import IO
from lark_oapi.core.const import UTF_8, CONTENT_TYPE
from lark_oapi.core import JSON
from lark_oapi.core.token import verify
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.utils import Files
from requests_toolbelt import MultipartEncoder
from lark_oapi.api.application.v6.model.overview_application_app_usage_request import OverviewApplicationAppUsageRequest
from lark_oapi.api.application.v6.model.overview_application_app_usage_response import OverviewApplicationAppUsageResponse


class ApplicationAppUsage(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def overview(self, request: OverviewApplicationAppUsageRequest, option: RequestOption = RequestOption()) -> OverviewApplicationAppUsageResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: OverviewApplicationAppUsageResponse = JSON.unmarshal(str(resp.content, UTF_8), OverviewApplicationAppUsageResponse)
        response.raw = resp

        return response

    