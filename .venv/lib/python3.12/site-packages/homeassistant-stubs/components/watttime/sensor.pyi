from .const import CONF_BALANCING_AUTHORITY as CONF_BALANCING_AUTHORITY, CONF_BALANCING_AUTHORITY_ABBREV as CONF_BALANCING_AUTHORITY_ABBREV, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONF_SHOW_ON_MAP as CONF_SHOW_ON_MAP, PERCENTAGE as PERCENTAGE, UnitOfMass as UnitOfMass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

ATTR_BALANCING_AUTHORITY: str
SENSOR_TYPE_REALTIME_EMISSIONS_MOER: str
SENSOR_TYPE_REALTIME_EMISSIONS_PERCENT: str
REALTIME_EMISSIONS_SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RealtimeEmissionsSensor(CoordinatorEntity, SensorEntity):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _entry: Incomplete
    entity_description: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator, entry: ConfigEntry, description: SensorEntityDescription) -> None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
    @property
    def native_value(self) -> StateType: ...
