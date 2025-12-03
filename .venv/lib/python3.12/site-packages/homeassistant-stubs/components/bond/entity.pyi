import abc
from .const import DOMAIN as DOMAIN
from .models import BondData as BondData
from .utils import BondDevice as BondDevice
from _typeshed import Incomplete
from abc import abstractmethod
from datetime import datetime
from homeassistant.const import ATTR_HW_VERSION as ATTR_HW_VERSION, ATTR_MODEL as ATTR_MODEL, ATTR_NAME as ATTR_NAME, ATTR_SUGGESTED_AREA as ATTR_SUGGESTED_AREA, ATTR_SW_VERSION as ATTR_SW_VERSION, ATTR_VIA_DEVICE as ATTR_VIA_DEVICE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HassJob as HassJob, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.event import async_call_later as async_call_later

_LOGGER: Incomplete
_FALLBACK_SCAN_INTERVAL: int
_BPUP_ALIVE_SCAN_INTERVAL: int

class BondEntity(Entity, metaclass=abc.ABCMeta):
    _attr_should_poll: bool
    _hub: Incomplete
    _bond: Incomplete
    _device: Incomplete
    _device_id: Incomplete
    _sub_device: Incomplete
    _attr_available: bool
    _bpup_subs: Incomplete
    _update_lock: Incomplete
    _initialized: bool
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_assumed_state: Incomplete
    _bpup_polling_fallback: CALLBACK_TYPE | None
    _async_update_if_bpup_not_alive_job: Incomplete
    def __init__(self, data: BondData, device: BondDevice, sub_device: str | None = None, sub_device_id: str | None = None) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    async def async_update(self) -> None: ...
    @callback
    def _async_update_if_bpup_not_alive(self, now: datetime) -> None: ...
    async def _async_update(self) -> None: ...
    async def _async_update_from_api(self) -> None: ...
    @abstractmethod
    def _apply_state(self) -> None: ...
    @callback
    def _async_state_callback(self, state: dict) -> None: ...
    @callback
    def _async_bpup_callback(self, json_msg: dict) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_schedule_bpup_alive_or_poll(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
