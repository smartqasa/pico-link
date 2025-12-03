from .const import CONNECTIVITY_TRAIT_OFFLINE as CONNECTIVITY_TRAIT_OFFLINE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from google_nest_sdm.device import Device as Device
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo

DEVICE_TYPE_MAP: dict[str, str]

class NestDeviceInfo:
    device_brand: str
    _device: Incomplete
    def __init__(self, device: Device) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def device_name(self) -> str | None: ...
    @property
    def device_model(self) -> str | None: ...
    @property
    def suggested_area(self) -> str | None: ...

@callback
def async_nest_devices(hass: HomeAssistant) -> Mapping[str, Device]: ...
@callback
def async_nest_devices_by_device_id(hass: HomeAssistant) -> Mapping[str, Device]: ...
