from .const import ATTR_DELTA as ATTR_DELTA, ATTR_DEVICE as ATTR_DEVICE, ATTR_DIRECTION as ATTR_DIRECTION, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DATE as ATTR_DATE, UnitOfBloodGlucoseConcentration as UnitOfBloodGlucoseConcentration
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from py_nightscout import Api as NightscoutAPI
from typing import Any

SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete
DEFAULT_NAME: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NightscoutSensor(SensorEntity):
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_icon: str
    api: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_extra_state_attributes: dict[str, Any]
    def __init__(self, api: NightscoutAPI, name: str, unique_id: str | None) -> None: ...
    _attr_available: bool
    _attr_native_value: Incomplete
    async def async_update(self) -> None: ...
    def _parse_icon(self, direction: str) -> str: ...
