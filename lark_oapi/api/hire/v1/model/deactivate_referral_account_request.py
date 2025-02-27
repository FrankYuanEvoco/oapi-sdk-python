# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class DeactivateReferralAccountRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.referral_account_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeactivateReferralAccountRequestBuilder":
        return DeactivateReferralAccountRequestBuilder()


class DeactivateReferralAccountRequestBuilder(object):

    def __init__(self) -> None:
        deactivate_referral_account_request = DeactivateReferralAccountRequest()
        deactivate_referral_account_request.http_method = HttpMethod.POST
        deactivate_referral_account_request.uri = "/open-apis/hire/v1/referral_account/:referral_account_id/deactivate"
        deactivate_referral_account_request.token_types = {AccessTokenType.TENANT}
        self._deactivate_referral_account_request: DeactivateReferralAccountRequest = deactivate_referral_account_request

    def user_id_type(self, user_id_type: str) -> "DeactivateReferralAccountRequestBuilder":
        self._deactivate_referral_account_request.user_id_type = user_id_type
        self._deactivate_referral_account_request.add_query("user_id_type", user_id_type)
        return self

    def referral_account_id(self, referral_account_id: str) -> "DeactivateReferralAccountRequestBuilder":
        self._deactivate_referral_account_request.referral_account_id = referral_account_id
        self._deactivate_referral_account_request.paths["referral_account_id"] = str(referral_account_id)
        return self

    def build(self) -> DeactivateReferralAccountRequest:
        return self._deactivate_referral_account_request
