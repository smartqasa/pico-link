from . import get_hub as get_hub
from .const import CALL_TYPE_COIL as CALL_TYPE_COIL, CALL_TYPE_DISCRETE as CALL_TYPE_DISCRETE, CONF_SLAVE_COUNT as CONF_SLAVE_COUNT, CONF_VIRTUAL_COUNT as CONF_VIRTUAL_COUNT
from .entity import BasePlatform as BasePlatform
from .modbus import ModbusHub as ModbusHub
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.const import CONF_BINARY_SENSORS as CONF_BINARY_SENSORS, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class ModbusBinarySensor(BasePlatform, RestoreEntity, BinarySensorEntity):
    _count: Incomplete
    _coordinator: DataUpdateCoordinator[list[int] | None] | None
    _result: list[int]
    def __init__(self, hass: HomeAssistant, hub: ModbusHub, entry: dict[str, Any], slave_count: int) -> None: ...
    async def async_setup_slaves(self, hass: HomeAssistant, slave_count: int, entry: dict[str, Any]) -> list[SlaveSensor]: ...
    _attr_is_on: Incomplete
    async def async_added_to_hass(self) -> None: ...
    _call_active: bool
    _attr_available: bool
    async def async_update(self, now: datetime | None = None) -> None: ...

class SlaveSensor(CoordinatorEntity[DataUpdateCoordinator[list[int] | None]], RestoreEntity, BinarySensorEntity):
    _attr_name: Incomplete
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    _attr_available: bool
    _result_inx: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[list[int] | None], idx: int, entry: dict[str, Any]) -> None: ...
    _attr_is_on: Incomplete
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
