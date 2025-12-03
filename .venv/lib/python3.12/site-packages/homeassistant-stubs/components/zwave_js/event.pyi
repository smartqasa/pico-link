from .const import ATTR_VALUE as ATTR_VALUE, DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from _typeshed import Incomplete
from homeassistant.components.event import EventEntity as EventEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from zwave_js_server.model.driver import Driver as Driver
from zwave_js_server.model.value import Value as Value, ValueNotification as ValueNotification

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _cc_and_label(value: Value) -> str: ...

class ZwaveEventEntity(ZWaveBaseEntity, EventEntity):
    states: dict[int, str]
    _attr_event_types: Incomplete
    _attr_name: Incomplete
    def __init__(self, config_entry: ConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo) -> None: ...
    @callback
    def _async_handle_event(self, value_notification: ValueNotification) -> None: ...
    async def async_added_to_hass(self) -> None: ...
