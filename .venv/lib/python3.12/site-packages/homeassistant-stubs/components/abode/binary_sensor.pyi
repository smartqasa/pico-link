from . import AbodeSystem as AbodeSystem
from .const import DOMAIN as DOMAIN
from .entity import AbodeDevice as AbodeDevice
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.enum import try_parse_enum as try_parse_enum
from jaraco.abode.devices.binary_sensor import BinarySensor as BinarySensor

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AbodeBinarySensor(AbodeDevice, BinarySensorEntity):
    _attr_name: Incomplete
    _device: BinarySensor
    @property
    def is_on(self) -> bool: ...
    @property
    def device_class(self) -> BinarySensorDeviceClass | None: ...
