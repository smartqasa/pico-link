from .const import ATTR_ADD_ENTITIES as ATTR_ADD_ENTITIES, ATTR_ALL as ATTR_ALL, ATTR_AUTO as ATTR_AUTO, ATTR_ENTITIES as ATTR_ENTITIES, ATTR_OBJECT_ID as ATTR_OBJECT_ID, ATTR_ORDER as ATTR_ORDER, ATTR_REMOVE_ENTITIES as ATTR_REMOVE_ENTITIES, CONF_HIDE_MEMBERS as CONF_HIDE_MEMBERS, DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN, GROUP_ORDER as GROUP_ORDER, REG_KEY as REG_KEY
from .entity import Group as Group, async_get_component as async_get_component
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_ICON as ATTR_ICON, ATTR_NAME as ATTR_NAME, CONF_ENTITIES as CONF_ENTITIES, CONF_ICON as CONF_ICON, CONF_NAME as CONF_NAME, Platform as Platform, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.reload import async_reload_integration_platforms as async_reload_integration_platforms
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from typing import Any

CONF_ALL: str
SERVICE_SET: str
SERVICE_REMOVE: str
PLATFORMS: Incomplete
_LOGGER: Incomplete

def _conf_preprocess(value: Any) -> dict[str, Any]: ...

GROUP_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

@bind_hass
def is_on(hass: HomeAssistant, entity_id: str) -> bool: ...

expand_entity_ids: Incomplete
get_entity_ids: Incomplete

@bind_hass
def groups_with_entity(hass: HomeAssistant, entity_id: str) -> list[str]: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def config_entry_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def _async_process_config(hass: HomeAssistant, config: ConfigType) -> None: ...
