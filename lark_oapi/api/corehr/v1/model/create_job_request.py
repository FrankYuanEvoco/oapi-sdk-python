# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .job import Job


class CreateJobRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.client_token: Optional[str] = None
        self.request_body: Optional[Job] = None

    @staticmethod
    def builder() -> "CreateJobRequestBuilder":
        return CreateJobRequestBuilder()


class CreateJobRequestBuilder(object):

    def __init__(self, create_job_request: CreateJobRequest = CreateJobRequest()) -> None:
        create_job_request.http_method = HttpMethod.POST
        create_job_request.uri = "/open-apis/corehr/v1/jobs"
        create_job_request.token_types = {AccessTokenType.TENANT}
        self._create_job_request: CreateJobRequest = create_job_request
    
    def client_token(self, client_token: str) -> "CreateJobRequestBuilder":
        self._create_job_request.client_token = client_token
        self._create_job_request.queries["client_token"] = str(client_token)
        return self
    
    def request_body(self, request_body: Job) -> "CreateJobRequestBuilder":
        self._create_job_request.request_body = request_body
        self._create_job_request.body = request_body
        return self

    def build(self) -> CreateJobRequest:
        return self._create_job_request