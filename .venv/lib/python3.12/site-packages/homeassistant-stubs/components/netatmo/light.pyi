from .const import CONF_URL_CONTROL as CONF_URL_CONTROL, CONF_URL_SECURITY as CONF_URL_SECURITY, DOMAIN as DOMAIN, EVENT_TYPE_LIGHT_MODE as EVENT_TYPE_LIGHT_MODE, NETATMO_CREATE_CAMERA_LIGHT as NETATMO_CREATE_CAMERA_LIGHT, NETATMO_CREATE_LIGHT as NETATMO_CREATE_LIGHT, WEBHOOK_LIGHT_MODE as WEBHOOK_LIGHT_MODE, WEBHOOK_PUSH_TYPE as WEBHOOK_PUSH_TYPE
from .data_handler import HOME as HOME, NetatmoDevice as NetatmoDevice, SIGNAL_NAME as SIGNAL_NAME
from .entity import NetatmoModuleEntity as NetatmoModuleEntity
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyatmo import modules as NaModules
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NetatmoCameraLight(NetatmoModuleEntity, LightEntity):
    device: NaModules.NOC
    _attr_is_on: bool
    _attr_name: Incomplete
    _attr_configuration_url = CONF_URL_SECURITY
    _attr_color_mode: Incomplete
    _attr_has_entity_name: bool
    _attr_supported_color_modes: Incomplete
    _attr_unique_id: Incomplete
    _signal_name: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def handle_event(self, event: dict) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @callback
    def async_update_callback(self) -> None: ...

class NetatmoLight(NetatmoModuleEntity, LightEntity):
    _attr_name: Incomplete
    _attr_configuration_url = CONF_URL_CONTROL
    _attr_brightness: int | None
    device: NaModules.NLFN
    _attr_unique_id: Incomplete
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _signal_name: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice) -> None: ...
    _attr_is_on: bool
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @callback
    def async_update_callback(self) -> None: ...
