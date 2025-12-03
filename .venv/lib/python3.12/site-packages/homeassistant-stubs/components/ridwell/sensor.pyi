from .const import DOMAIN as DOMAIN, SENSOR_TYPE_NEXT_PICKUP as SENSOR_TYPE_NEXT_PICKUP
from .coordinator import RidwellDataUpdateCoordinator as RidwellDataUpdateCoordinator
from .entity import RidwellEntity as RidwellEntity
from _typeshed import Incomplete
from aioridwell.model import RidwellAccount as RidwellAccount
from collections.abc import Mapping
from datetime import date
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

ATTR_CATEGORY: str
ATTR_PICKUP_STATE: str
ATTR_PICKUP_TYPES: str
ATTR_QUANTITY: str
SENSOR_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RidwellSensor(RidwellEntity, SensorEntity):
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: RidwellDataUpdateCoordinator, account: RidwellAccount, description: SensorEntityDescription) -> None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any]: ...
    @property
    def native_value(self) -> date: ...
