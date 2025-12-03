import voluptuous as vol
from .binary_sensor import CONF_ALL as CONF_ALL, async_create_preview_binary_sensor as async_create_preview_binary_sensor
from .button import async_create_preview_button as async_create_preview_button
from .const import CONF_HIDE_MEMBERS as CONF_HIDE_MEMBERS, CONF_IGNORE_NON_NUMERIC as CONF_IGNORE_NON_NUMERIC, DOMAIN as DOMAIN
from .cover import async_create_preview_cover as async_create_preview_cover
from .entity import GroupEntity as GroupEntity
from .event import async_create_preview_event as async_create_preview_event
from .fan import async_create_preview_fan as async_create_preview_fan
from .light import async_create_preview_light as async_create_preview_light
from .lock import async_create_preview_lock as async_create_preview_lock
from .media_player import MediaPlayerGroup as MediaPlayerGroup, async_create_preview_media_player as async_create_preview_media_player
from .notify import async_create_preview_notify as async_create_preview_notify
from .sensor import async_create_preview_sensor as async_create_preview_sensor
from .switch import async_create_preview_switch as async_create_preview_switch
from _typeshed import Incomplete
from collections.abc import Callable, Coroutine, Mapping
from homeassistant.components import websocket_api as websocket_api
from homeassistant.const import CONF_ENTITIES as CONF_ENTITIES, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_registry as er, selector as selector
from homeassistant.helpers.schema_config_entry_flow import SchemaCommonFlowHandler as SchemaCommonFlowHandler, SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowFormStep as SchemaFlowFormStep, SchemaFlowMenuStep as SchemaFlowMenuStep, SchemaOptionsFlowHandler as SchemaOptionsFlowHandler, entity_selector_without_own_entities as entity_selector_without_own_entities
from typing import Any

_STATISTIC_MEASURES: Incomplete

async def basic_group_options_schema(domain: str | list[str], handler: SchemaCommonFlowHandler | None) -> vol.Schema: ...
def basic_group_config_schema(domain: str | list[str]) -> vol.Schema: ...
async def binary_sensor_options_schema(handler: SchemaCommonFlowHandler | None) -> vol.Schema: ...

BINARY_SENSOR_CONFIG_SCHEMA: Incomplete
SENSOR_CONFIG_EXTENDS: Incomplete
SENSOR_OPTIONS: Incomplete

async def sensor_options_schema(domain: str, handler: SchemaCommonFlowHandler | None) -> vol.Schema: ...

SENSOR_CONFIG_SCHEMA: Incomplete

async def light_switch_options_schema(domain: str, handler: SchemaCommonFlowHandler | None) -> vol.Schema: ...

GROUP_TYPES: Incomplete

async def choose_options_step(options: dict[str, Any]) -> str: ...
def set_group_type(group_type: str) -> Callable[[SchemaCommonFlowHandler, dict[str, Any]], Coroutine[Any, Any, dict[str, Any]]]: ...

CONFIG_FLOW: Incomplete
OPTIONS_FLOW: Incomplete
PREVIEW_OPTIONS_SCHEMA: dict[str, vol.Schema]
CREATE_PREVIEW_ENTITY: dict[str, Callable[[HomeAssistant, str, dict[str, Any]], GroupEntity | MediaPlayerGroup]]

class GroupConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW
    @callback
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...
    @callback
    def async_config_flow_finished(self, options: Mapping[str, Any]) -> None: ...
    @callback
    @staticmethod
    def async_options_flow_finished(hass: HomeAssistant, options: Mapping[str, Any]) -> None: ...
    @staticmethod
    async def async_setup_preview(hass: HomeAssistant) -> None: ...

def _async_hide_members(hass: HomeAssistant, members: list[str], hidden_by: er.RegistryEntryHider | None) -> None: ...
@callback
def ws_start_preview(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
