import upcloud_api
from .const import DOMAIN as DOMAIN
from .coordinator import UpCloudDataUpdateCoordinator as UpCloudDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_USERNAME as CONF_USERNAME, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_PROBLEM as STATE_PROBLEM
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGER: Incomplete
ATTR_CORE_NUMBER: str
ATTR_HOSTNAME: str
ATTR_MEMORY_AMOUNT: str
ATTR_TITLE: str
ATTR_UUID: str
ATTR_ZONE: str
DEFAULT_COMPONENT_NAME: str
STATE_MAP: Incomplete

class UpCloudServerEntity(CoordinatorEntity[UpCloudDataUpdateCoordinator]):
    uuid: Incomplete
    def __init__(self, coordinator: UpCloudDataUpdateCoordinator, uuid: str) -> None: ...
    @property
    def _server(self) -> upcloud_api.Server: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def icon(self) -> str: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def device_info(self) -> DeviceInfo: ...
