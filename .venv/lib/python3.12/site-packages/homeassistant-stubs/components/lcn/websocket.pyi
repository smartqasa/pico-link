from .const import ADD_ENTITIES_CALLBACKS as ADD_ENTITIES_CALLBACKS, CONF_DOMAIN_DATA as CONF_DOMAIN_DATA, CONF_HARDWARE_SERIAL as CONF_HARDWARE_SERIAL, CONF_HARDWARE_TYPE as CONF_HARDWARE_TYPE, CONF_SOFTWARE_SERIAL as CONF_SOFTWARE_SERIAL, CONNECTION as CONNECTION, DOMAIN as DOMAIN
from .helpers import DeviceConnectionType as DeviceConnectionType, async_update_device_config as async_update_device_config, generate_unique_id as generate_unique_id, get_device_config as get_device_config, get_device_connection as get_device_connection, get_resource as get_resource, purge_device_registry as purge_device_registry, purge_entity_registry as purge_entity_registry, register_lcn_address_devices as register_lcn_address_devices
from .schemas import ADDRESS_SCHEMA as ADDRESS_SCHEMA, DOMAIN_DATA_BINARY_SENSOR as DOMAIN_DATA_BINARY_SENSOR, DOMAIN_DATA_CLIMATE as DOMAIN_DATA_CLIMATE, DOMAIN_DATA_COVER as DOMAIN_DATA_COVER, DOMAIN_DATA_LIGHT as DOMAIN_DATA_LIGHT, DOMAIN_DATA_SCENE as DOMAIN_DATA_SCENE, DOMAIN_DATA_SENSOR as DOMAIN_DATA_SENSOR, DOMAIN_DATA_SWITCH as DOMAIN_DATA_SWITCH
from collections.abc import Awaitable, Callable
from homeassistant.components import panel_custom as panel_custom, websocket_api as websocket_api
from homeassistant.components.http import StaticPathConfig as StaticPathConfig
from homeassistant.components.websocket_api import ActiveConnection as ActiveConnection, AsyncWebSocketCommandHandler as AsyncWebSocketCommandHandler
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_DEVICES as CONF_DEVICES, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_RESOURCE as CONF_RESOURCE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_registry as er
from typing import Any, Final

type AsyncLcnWebSocketCommandHandler = Callable[[HomeAssistant, ActiveConnection, dict[str, Any], ConfigEntry], Awaitable[None]]
URL_BASE: Final[str]

async def register_panel_and_ws_api(hass: HomeAssistant) -> None: ...
def get_config_entry(func: AsyncLcnWebSocketCommandHandler) -> AsyncWebSocketCommandHandler: ...
@websocket_api.require_admin
@websocket_api.async_response
@get_config_entry
async def websocket_get_device_configs(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict, config_entry: ConfigEntry) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@get_config_entry
async def websocket_get_entity_configs(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict, config_entry: ConfigEntry) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@get_config_entry
async def websocket_scan_devices(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict, config_entry: ConfigEntry) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@get_config_entry
async def websocket_add_device(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict, config_entry: ConfigEntry) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@get_config_entry
async def websocket_delete_device(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict, config_entry: ConfigEntry) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@get_config_entry
async def websocket_add_entity(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict, config_entry: ConfigEntry) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@get_config_entry
async def websocket_delete_entity(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict, config_entry: ConfigEntry) -> None: ...
async def async_create_or_update_device_in_config_entry(hass: HomeAssistant, device_connection: DeviceConnectionType, config_entry: ConfigEntry) -> None: ...
def get_entity_entry(hass: HomeAssistant, entity_config: dict, config_entry: ConfigEntry) -> er.RegistryEntry | None: ...
