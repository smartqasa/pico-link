from . import setup_mysensors_platform as setup_mysensors_platform
from .const import DiscoveryInfo as DiscoveryInfo, MYSENSORS_DISCOVERY as MYSENSORS_DISCOVERY
from .entity import MySensorsChildEntity as MySensorsChildEntity
from .helpers import on_unload as on_unload
from homeassistant.components.text import TextEntity as TextEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MySensorsText(MySensorsChildEntity, TextEntity):
    _attr_native_max: int
    @property
    def native_value(self) -> str | None: ...
    async def async_set_value(self, value: str) -> None: ...
