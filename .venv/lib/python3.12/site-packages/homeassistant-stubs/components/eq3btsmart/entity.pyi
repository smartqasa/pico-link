from . import Eq3ConfigEntry as Eq3ConfigEntry
from .const import DEVICE_MODEL as DEVICE_MODEL, MANUFACTURER as MANUFACTURER, SIGNAL_THERMOSTAT_CONNECTED as SIGNAL_THERMOSTAT_CONNECTED, SIGNAL_THERMOSTAT_DISCONNECTED as SIGNAL_THERMOSTAT_DISCONNECTED
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import CONNECTION_BLUETOOTH as CONNECTION_BLUETOOTH, DeviceInfo as DeviceInfo, format_mac as format_mac
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.util import slugify as slugify

class Eq3Entity(Entity):
    _attr_has_entity_name: bool
    _eq3_config: Incomplete
    _thermostat: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, entry: Eq3ConfigEntry, unique_id_key: str | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def _async_on_updated(self) -> None: ...
    _attr_available: bool
    @callback
    def _async_on_disconnected(self) -> None: ...
    @callback
    def _async_on_connected(self) -> None: ...
    @property
    def available(self) -> bool: ...
