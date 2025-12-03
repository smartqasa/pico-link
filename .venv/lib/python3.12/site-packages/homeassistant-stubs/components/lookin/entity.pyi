import abc
from .const import DOMAIN as DOMAIN, MODEL_NAMES as MODEL_NAMES
from .coordinator import LookinDataUpdateCoordinator as LookinDataUpdateCoordinator
from .models import LookinData as LookinData
from _typeshed import Incomplete
from abc import abstractmethod
from aiolookin import Climate as Climate, MeteoSensor, Remote
from aiolookin.models import Device as Device, UDPEvent as UDPEvent
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

LOGGER: Incomplete

def _lookin_device_to_device_info(lookin_device: Device, host: str) -> DeviceInfo: ...
def _lookin_controlled_device_to_device_info(lookin_device: Device, uuid: str, device: Climate | Remote, host: str) -> DeviceInfo: ...

class LookinDeviceMixIn:
    _lookin_device: Incomplete
    _lookin_protocol: Incomplete
    _lookin_udp_subs: Incomplete
    def _set_lookin_device_attrs(self, lookin_data: LookinData) -> None: ...

class LookinDeviceCoordinatorEntity(LookinDeviceMixIn, CoordinatorEntity[LookinDataUpdateCoordinator[MeteoSensor]]):
    _attr_should_poll: bool
    _attr_device_info: Incomplete
    def __init__(self, lookin_data: LookinData) -> None: ...

class LookinEntityMixIn:
    _device: Incomplete
    _uuid: Incomplete
    _meteo_coordinator: Incomplete
    _function_names: Incomplete
    def _set_lookin_entity_attrs(self, uuid: str, device: Remote | Climate, lookin_data: LookinData) -> None: ...

class LookinCoordinatorEntity(LookinDeviceMixIn, LookinEntityMixIn, CoordinatorEntity[LookinDataUpdateCoordinator[Remote]]):
    _attr_should_poll: bool
    _attr_assumed_state: bool
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, coordinator: LookinDataUpdateCoordinator[Remote], uuid: str, device: Remote | Climate, lookin_data: LookinData) -> None: ...
    async def _async_send_command(self, command: str, signal: str = 'FF') -> None: ...

class LookinPowerEntity(LookinCoordinatorEntity):
    _power_on_command: str
    _power_off_command: str
    def __init__(self, coordinator: LookinDataUpdateCoordinator[Remote], uuid: str, device: Remote | Climate, lookin_data: LookinData) -> None: ...

class LookinPowerPushRemoteEntity(LookinPowerEntity, metaclass=abc.ABCMeta):
    _attr_name: Incomplete
    def __init__(self, coordinator: LookinDataUpdateCoordinator[Remote], uuid: str, device: Remote, lookin_data: LookinData) -> None: ...
    @property
    def _remote(self) -> Remote: ...
    @abstractmethod
    def _update_from_status(self, status: str) -> None: ...
    def _async_push_update(self, event: UDPEvent) -> None: ...
    async def _async_push_update_device(self, event: UDPEvent) -> None: ...
    async def async_added_to_hass(self) -> None: ...
