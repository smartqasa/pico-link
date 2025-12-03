from .const import DOMAIN as DOMAIN
from .entity import DuotecnoEntity as DuotecnoEntity
from duotecno.controller import PyDuotecno as PyDuotecno
from duotecno.unit import ControlUnit as ControlUnit, VirtualUnit as VirtualUnit
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DuotecnoBinarySensor(DuotecnoEntity, BinarySensorEntity):
    _unit: ControlUnit | VirtualUnit
    @property
    def is_on(self) -> bool: ...
