from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from rpi_bad_power import UnderVoltage as UnderVoltage

_LOGGER: Incomplete
DESCRIPTION_NORMALIZED: str
DESCRIPTION_UNDER_VOLTAGE: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RaspberryChargerBinarySensor(BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    _attr_icon: str
    _attr_name: str
    _attr_unique_id: str
    _under_voltage: Incomplete
    def __init__(self, under_voltage: UnderVoltage) -> None: ...
    _attr_is_on: Incomplete
    def update(self) -> None: ...
