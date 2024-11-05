# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.corehr.v2 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ActiveCompanyRequest = ActiveCompanyRequest.builder() \
        .request_body(ActiveCompanyRequestBody.builder()
                      .company_id("1616161616")
                      .effective_time("2020-01-01")
                      .active(True)
                      .operation_reason("业务操作")
                      .build()) \
        .build()

    # 发起请求
    response: ActiveCompanyResponse = client.corehr.v2.company.active(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v2.company.active failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


# 异步方式
async def amain():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ActiveCompanyRequest = ActiveCompanyRequest.builder() \
        .request_body(ActiveCompanyRequestBody.builder()
                      .company_id("1616161616")
                      .effective_time("2020-01-01")
                      .active(True)
                      .operation_reason("业务操作")
                      .build()) \
        .build()

    # 发起请求
    response: ActiveCompanyResponse = await client.corehr.v2.company.aactive(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v2.company.aactive failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()