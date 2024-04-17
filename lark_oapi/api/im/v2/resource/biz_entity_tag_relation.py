# Code generated by Lark OpenAPI.

import io
from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core import JSON
from lark_oapi.core.token import verify
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.utils import Files
from requests_toolbelt import MultipartEncoder
from ..model.create_biz_entity_tag_relation_request import CreateBizEntityTagRelationRequest
from ..model.create_biz_entity_tag_relation_response import CreateBizEntityTagRelationResponse
from ..model.get_biz_entity_tag_relation_request import GetBizEntityTagRelationRequest
from ..model.get_biz_entity_tag_relation_response import GetBizEntityTagRelationResponse
from ..model.update_biz_entity_tag_relation_request import UpdateBizEntityTagRelationRequest
from ..model.update_biz_entity_tag_relation_response import UpdateBizEntityTagRelationResponse


class BizEntityTagRelation(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateBizEntityTagRelationRequest,
               option: Optional[RequestOption] = None) -> CreateBizEntityTagRelationResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateBizEntityTagRelationResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                      CreateBizEntityTagRelationResponse)
        response.raw = resp

        return response

    async def acreate(self, request: CreateBizEntityTagRelationRequest,
                      option: Optional[RequestOption] = None) -> CreateBizEntityTagRelationResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: CreateBizEntityTagRelationResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                      CreateBizEntityTagRelationResponse)
        response.raw = resp

        return response

    def get(self, request: GetBizEntityTagRelationRequest,
            option: Optional[RequestOption] = None) -> GetBizEntityTagRelationResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetBizEntityTagRelationResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   GetBizEntityTagRelationResponse)
        response.raw = resp

        return response

    async def aget(self, request: GetBizEntityTagRelationRequest,
                   option: Optional[RequestOption] = None) -> GetBizEntityTagRelationResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: GetBizEntityTagRelationResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   GetBizEntityTagRelationResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateBizEntityTagRelationRequest,
               option: Optional[RequestOption] = None) -> UpdateBizEntityTagRelationResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: UpdateBizEntityTagRelationResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                      UpdateBizEntityTagRelationResponse)
        response.raw = resp

        return response

    async def aupdate(self, request: UpdateBizEntityTagRelationRequest,
                      option: Optional[RequestOption] = None) -> UpdateBizEntityTagRelationResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: UpdateBizEntityTagRelationResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                      UpdateBizEntityTagRelationResponse)
        response.raw = resp

        return response