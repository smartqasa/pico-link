from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SENSIBO_ERRORS as SENSIBO_ERRORS, TIMEOUT as TIMEOUT
from .coordinator import SensiboDataUpdateCoordinator as SensiboDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pysensibo.model import MotionSensor as MotionSensor, SensiboDevice as SensiboDevice
from typing import Any, Concatenate

def async_handle_api_call[_T: SensiboDeviceBaseEntity, **_P](function: Callable[Concatenate[_T, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_T, _P], Coroutine[Any, Any, Any]]: ...

class SensiboBaseEntity(CoordinatorEntity[SensiboDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _device_id: Incomplete
    _client: Incomplete
    def __init__(self, coordinator: SensiboDataUpdateCoordinator, device_id: str) -> None: ...
    @property
    def device_data(self) -> SensiboDevice: ...

class SensiboDeviceBaseEntity(SensiboBaseEntity):
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SensiboDataUpdateCoordinator, device_id: str) -> None: ...

class SensiboMotionBaseEntity(SensiboBaseEntity):
    _sensor_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SensiboDataUpdateCoordinator, device_id: str, sensor_id: str, sensor_data: MotionSensor) -> None: ...
    @property
    def sensor_data(self) -> MotionSensor | None: ...
