# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListJobRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[str] = None
        self.name: Optional[str] = None
        self.query_language: Optional[str] = None

    @staticmethod
    def builder() -> "ListJobRequestBuilder":
        return ListJobRequestBuilder()


class ListJobRequestBuilder(object):

    def __init__(self, list_job_request: ListJobRequest = ListJobRequest()) -> None:
        list_job_request.http_method = HttpMethod.GET
        list_job_request.uri = "/open-apis/corehr/v1/jobs"
        list_job_request.token_types = {AccessTokenType.TENANT}
        self._list_job_request: ListJobRequest = list_job_request
    
    def page_token(self, page_token: str) -> "ListJobRequestBuilder":
        self._list_job_request.page_token = page_token
        self._list_job_request.queries["page_token"] = str(page_token)
        return self
    
    def page_size(self, page_size: str) -> "ListJobRequestBuilder":
        self._list_job_request.page_size = page_size
        self._list_job_request.queries["page_size"] = str(page_size)
        return self
    
    def name(self, name: str) -> "ListJobRequestBuilder":
        self._list_job_request.name = name
        self._list_job_request.queries["name"] = str(name)
        return self
    
    def query_language(self, query_language: str) -> "ListJobRequestBuilder":
        self._list_job_request.query_language = query_language
        self._list_job_request.queries["query_language"] = str(query_language)
        return self
    

    def build(self) -> ListJobRequest:
        return self._list_job_request