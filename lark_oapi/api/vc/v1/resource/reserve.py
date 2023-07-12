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
from lark_oapi.api.vc.v1.model.apply_reserve_request import ApplyReserveRequest
from lark_oapi.api.vc.v1.model.apply_reserve_response import ApplyReserveResponse
from lark_oapi.api.vc.v1.model.delete_reserve_request import DeleteReserveRequest
from lark_oapi.api.vc.v1.model.delete_reserve_response import DeleteReserveResponse
from lark_oapi.api.vc.v1.model.get_reserve_request import GetReserveRequest
from lark_oapi.api.vc.v1.model.get_reserve_response import GetReserveResponse
from lark_oapi.api.vc.v1.model.get_active_meeting_reserve_request import GetActiveMeetingReserveRequest
from lark_oapi.api.vc.v1.model.get_active_meeting_reserve_response import GetActiveMeetingReserveResponse
from lark_oapi.api.vc.v1.model.update_reserve_request import UpdateReserveRequest
from lark_oapi.api.vc.v1.model.update_reserve_response import UpdateReserveResponse


class Reserve(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def apply(self, request: ApplyReserveRequest, option: RequestOption = RequestOption()) -> ApplyReserveResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: ApplyReserveResponse = JSON.unmarshal(str(resp.content, UTF_8), ApplyReserveResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteReserveRequest, option: RequestOption = RequestOption()) -> DeleteReserveResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: DeleteReserveResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteReserveResponse)
        response.raw = resp

        return response

    def get(self, request: GetReserveRequest, option: RequestOption = RequestOption()) -> GetReserveResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: GetReserveResponse = JSON.unmarshal(str(resp.content, UTF_8), GetReserveResponse)
        response.raw = resp

        return response

    def get_active_meeting(self, request: GetActiveMeetingReserveRequest, option: RequestOption = RequestOption()) -> GetActiveMeetingReserveResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: GetActiveMeetingReserveResponse = JSON.unmarshal(str(resp.content, UTF_8), GetActiveMeetingReserveResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateReserveRequest, option: RequestOption = RequestOption()) -> UpdateReserveResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: UpdateReserveResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateReserveResponse)
        response.raw = resp

        return response

    