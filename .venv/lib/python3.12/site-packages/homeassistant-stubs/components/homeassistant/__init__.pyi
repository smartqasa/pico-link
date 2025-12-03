from .const import DATA_EXPOSED_ENTITIES as DATA_EXPOSED_ENTITIES, DATA_STOP_HANDLER as DATA_STOP_HANDLER, DOMAIN as DOMAIN, SERVICE_HOMEASSISTANT_RESTART as SERVICE_HOMEASSISTANT_RESTART, SERVICE_HOMEASSISTANT_STOP as SERVICE_HOMEASSISTANT_STOP
from .exposed_entities import ExposedEntities as ExposedEntities, async_should_expose as async_should_expose
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant import core_config as core_config
from homeassistant.auth.permissions.const import CAT_ENTITIES as CAT_ENTITIES, POLICY_CONTROL as POLICY_CONTROL
from homeassistant.components import persistent_notification as persistent_notification
from homeassistant.const import ATTR_ELEVATION as ATTR_ELEVATION, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, RESTART_EXIT_CODE as RESTART_EXIT_CODE, SERVICE_RELOAD as SERVICE_RELOAD, SERVICE_SAVE_PERSISTENT_STATES as SERVICE_SAVE_PERSISTENT_STATES, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, callback as callback, split_entity_id as split_entity_id
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, Unauthorized as Unauthorized, UnknownUser as UnknownUser
from homeassistant.helpers import recorder as recorder, restore_state as restore_state
from homeassistant.helpers.entity_component import async_update_entity as async_update_entity
from homeassistant.helpers.service import async_extract_config_entry_ids as async_extract_config_entry_ids, async_extract_referenced_entity_ids as async_extract_referenced_entity_ids, async_register_admin_service as async_register_admin_service
from homeassistant.helpers.signal import KEY_HA_STOP as KEY_HA_STOP
from homeassistant.helpers.template import async_load_custom_templates as async_load_custom_templates
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

ATTR_ENTRY_ID: str
ATTR_SAFE_MODE: str
_LOGGER: Incomplete
SERVICE_RELOAD_CORE_CONFIG: str
SERVICE_RELOAD_CONFIG_ENTRY: str
SERVICE_RELOAD_CUSTOM_TEMPLATES: str
SERVICE_CHECK_CONFIG: str
SERVICE_UPDATE_ENTITY: str
SERVICE_SET_LOCATION: str
SERVICE_RELOAD_ALL: str
SCHEMA_UPDATE_ENTITY: Incomplete
SCHEMA_RELOAD_CONFIG_ENTRY: Incomplete
SCHEMA_RESTART: Incomplete
SHUTDOWN_SERVICES: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def _async_stop(hass: HomeAssistant, restart: bool) -> None: ...
@callback
def async_set_stop_handler(hass: HomeAssistant, stop_handler: Callable[[HomeAssistant, bool], Coroutine[Any, Any, None]]) -> None: ...
