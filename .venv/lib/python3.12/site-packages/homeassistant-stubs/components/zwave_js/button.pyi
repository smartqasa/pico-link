from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN, LOGGER as LOGGER
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from .helpers import get_device_info as get_device_info, get_valueless_base_unique_id as get_valueless_base_unique_id
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from zwave_js_server.model.driver import Driver as Driver
from zwave_js_server.model.node import Node as ZwaveNode

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ZwaveBooleanNodeButton(ZWaveBaseEntity, ButtonEntity):
    _attr_name: Incomplete
    def __init__(self, config_entry: ConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo) -> None: ...
    async def async_press(self) -> None: ...

class ZWaveNodePingButton(ButtonEntity):
    _attr_should_poll: bool
    _attr_entity_category: Incomplete
    _attr_has_entity_name: bool
    _attr_translation_key: str
    node: Incomplete
    _base_unique_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, driver: Driver, node: ZwaveNode) -> None: ...
    async def async_poll_value(self, _: bool) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_press(self) -> None: ...

class ZWaveNotificationIdleButton(ZWaveBaseEntity, ButtonEntity):
    _attr_entity_category: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, config_entry: ConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo) -> None: ...
    async def async_press(self) -> None: ...
