# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .time_range import TimeRange


class EmailFilter(object):
    _types = {
        "owner_userid_list": List[str],
        "owner_address_list": List[str],
        "time_range": TimeRange,
        "senders": List[str],
        "recipients": List[str],
        "email_title": str,
        "email_id": str,
    }

    def __init__(self, d=None):
        self.owner_userid_list: Optional[List[str]] = None
        self.owner_address_list: Optional[List[str]] = None
        self.time_range: Optional[TimeRange] = None
        self.senders: Optional[List[str]] = None
        self.recipients: Optional[List[str]] = None
        self.email_title: Optional[str] = None
        self.email_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EmailFilterBuilder":
        return EmailFilterBuilder()


class EmailFilterBuilder(object):
    def __init__(self) -> None:
        self._email_filter = EmailFilter()

    def owner_userid_list(self, owner_userid_list: List[str]) -> "EmailFilterBuilder":
        self._email_filter.owner_userid_list = owner_userid_list
        return self

    def owner_address_list(self, owner_address_list: List[str]) -> "EmailFilterBuilder":
        self._email_filter.owner_address_list = owner_address_list
        return self

    def time_range(self, time_range: TimeRange) -> "EmailFilterBuilder":
        self._email_filter.time_range = time_range
        return self

    def senders(self, senders: List[str]) -> "EmailFilterBuilder":
        self._email_filter.senders = senders
        return self

    def recipients(self, recipients: List[str]) -> "EmailFilterBuilder":
        self._email_filter.recipients = recipients
        return self

    def email_title(self, email_title: str) -> "EmailFilterBuilder":
        self._email_filter.email_title = email_title
        return self

    def email_id(self, email_id: str) -> "EmailFilterBuilder":
        self._email_filter.email_id = email_id
        return self

    def build(self) -> "EmailFilter":
        return self._email_filter