# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class AuditObjectDetail(object):
    _types = {
        "clone_source": str,
        "text_detail": str,
        "file_name": str,
        "third_party_app_i_d": str,
        "contain_file_num": int,
        "permission_setting_type": str,
        "permission_external_access__type": bool,
        "permission_share_type": str,
        "file_service_source": str,
        "okr_download_content": str,
        "container_type": str,
        "container_id": str,
        "current_page": str,
    }

    def __init__(self, d):
        self.clone_source: Optional[str] = None
        self.text_detail: Optional[str] = None
        self.file_name: Optional[str] = None
        self.third_party_app_i_d: Optional[str] = None
        self.contain_file_num: Optional[int] = None
        self.permission_setting_type: Optional[str] = None
        self.permission_external_access__type: Optional[bool] = None
        self.permission_share_type: Optional[str] = None
        self.file_service_source: Optional[str] = None
        self.okr_download_content: Optional[str] = None
        self.container_type: Optional[str] = None
        self.container_id: Optional[str] = None
        self.current_page: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AuditObjectDetailBuilder":
        return AuditObjectDetailBuilder()


class AuditObjectDetailBuilder(object):
    def __init__(self, audit_object_detail: AuditObjectDetail = AuditObjectDetail({})) -> None:
        self._audit_object_detail: AuditObjectDetail = audit_object_detail
    
    def clone_source(self, clone_source: str) -> "AuditObjectDetailBuilder":
        self._audit_object_detail.clone_source = clone_source
        return self
    
    def text_detail(self, text_detail: str) -> "AuditObjectDetailBuilder":
        self._audit_object_detail.text_detail = text_detail
        return self
    
    def file_name(self, file_name: str) -> "AuditObjectDetailBuilder":
        self._audit_object_detail.file_name = file_name
        return self
    
    def third_party_app_i_d(self, third_party_app_i_d: str) -> "AuditObjectDetailBuilder":
        self._audit_object_detail.third_party_app_i_d = third_party_app_i_d
        return self
    
    def contain_file_num(self, contain_file_num: int) -> "AuditObjectDetailBuilder":
        self._audit_object_detail.contain_file_num = contain_file_num
        return self
    
    def permission_setting_type(self, permission_setting_type: str) -> "AuditObjectDetailBuilder":
        self._audit_object_detail.permission_setting_type = permission_setting_type
        return self
    
    def permission_external_access__type(self, permission_external_access__type: bool) -> "AuditObjectDetailBuilder":
        self._audit_object_detail.permission_external_access__type = permission_external_access__type
        return self
    
    def permission_share_type(self, permission_share_type: str) -> "AuditObjectDetailBuilder":
        self._audit_object_detail.permission_share_type = permission_share_type
        return self
    
    def file_service_source(self, file_service_source: str) -> "AuditObjectDetailBuilder":
        self._audit_object_detail.file_service_source = file_service_source
        return self
    
    def okr_download_content(self, okr_download_content: str) -> "AuditObjectDetailBuilder":
        self._audit_object_detail.okr_download_content = okr_download_content
        return self
    
    def container_type(self, container_type: str) -> "AuditObjectDetailBuilder":
        self._audit_object_detail.container_type = container_type
        return self
    
    def container_id(self, container_id: str) -> "AuditObjectDetailBuilder":
        self._audit_object_detail.container_id = container_id
        return self
    
    def current_page(self, current_page: str) -> "AuditObjectDetailBuilder":
        self._audit_object_detail.current_page = current_page
        return self
    
    def build(self) -> "AuditObjectDetail":
        return self._audit_object_detail