# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .user_id import UserId
from .location_info_event import LocationInfoEvent
from .wifi_info_event import WifiInfoEvent
from .scan_wifi_info import ScanWifiInfo


class LocationRecord(object):
    _types = {
        "user_id": UserId,
        "timestamp": str,
        "location": LocationInfoEvent,
        "wifi": WifiInfoEvent,
        "rule_snapshot_id": str,
        "type": str,
        "scan_wifi_list": List[ScanWifiInfo],
        "device_id": str,
        "client_info": str,
    }

    def __init__(self, d):
        self.user_id: Optional[UserId] = None
        self.timestamp: Optional[str] = None
        self.location: Optional[LocationInfoEvent] = None
        self.wifi: Optional[WifiInfoEvent] = None
        self.rule_snapshot_id: Optional[str] = None
        self.type: Optional[str] = None
        self.scan_wifi_list: Optional[List[ScanWifiInfo]] = None
        self.device_id: Optional[str] = None
        self.client_info: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LocationRecordBuilder":
        return LocationRecordBuilder()


class LocationRecordBuilder(object):
    def __init__(self, location_record: LocationRecord = LocationRecord({})) -> None:
        self._location_record: LocationRecord = location_record
    
    def user_id(self, user_id: UserId) -> "LocationRecordBuilder":
        self._location_record.user_id = user_id
        return self
    
    def timestamp(self, timestamp: str) -> "LocationRecordBuilder":
        self._location_record.timestamp = timestamp
        return self
    
    def location(self, location: LocationInfoEvent) -> "LocationRecordBuilder":
        self._location_record.location = location
        return self
    
    def wifi(self, wifi: WifiInfoEvent) -> "LocationRecordBuilder":
        self._location_record.wifi = wifi
        return self
    
    def rule_snapshot_id(self, rule_snapshot_id: str) -> "LocationRecordBuilder":
        self._location_record.rule_snapshot_id = rule_snapshot_id
        return self
    
    def type(self, type: str) -> "LocationRecordBuilder":
        self._location_record.type = type
        return self
    
    def scan_wifi_list(self, scan_wifi_list: List[ScanWifiInfo]) -> "LocationRecordBuilder":
        self._location_record.scan_wifi_list = scan_wifi_list
        return self
    
    def device_id(self, device_id: str) -> "LocationRecordBuilder":
        self._location_record.device_id = device_id
        return self
    
    def client_info(self, client_info: str) -> "LocationRecordBuilder":
        self._location_record.client_info = client_info
        return self
    
    def build(self) -> "LocationRecord":
        return self._location_record