from .const import CONF_APPS as CONF_APPS, DOMAIN as DOMAIN
from _typeshed import Incomplete
from androidtvremote2 import AndroidTVRemote as AndroidTVRemote
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_NAME as CONF_NAME
from homeassistant.core import callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from typing import Any

class AndroidTVRemoteBaseEntity(Entity):
    _attr_name: Incomplete
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _api: Incomplete
    _host: Incomplete
    _name: Incomplete
    _apps: dict[str, Any]
    _attr_unique_id: Incomplete
    _attr_is_on: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, api: AndroidTVRemote, config_entry: ConfigEntry) -> None: ...
    _attr_available: Incomplete
    @callback
    def _is_available_updated(self, is_available: bool) -> None: ...
    @callback
    def _is_on_updated(self, is_on: bool) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def _send_key_command(self, key_code: str, direction: str = 'SHORT') -> None: ...
    def _send_launch_app_command(self, app_link: str) -> None: ...
