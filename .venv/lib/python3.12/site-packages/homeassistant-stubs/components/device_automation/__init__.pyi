import voluptuous as vol
from .action import DeviceAutomationActionProtocol as DeviceAutomationActionProtocol
from .condition import DeviceAutomationConditionProtocol as DeviceAutomationConditionProtocol
from .const import CONF_IS_OFF as CONF_IS_OFF, CONF_IS_ON as CONF_IS_ON, CONF_TURNED_OFF as CONF_TURNED_OFF, CONF_TURNED_ON as CONF_TURNED_ON
from .exceptions import DeviceNotFound as DeviceNotFound, EntityNotFound as EntityNotFound, InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from .trigger import DeviceAutomationTriggerProtocol as DeviceAutomationTriggerProtocol
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine, Iterable, Mapping
from dataclasses import dataclass
from enum import Enum
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.websocket_api import ActiveConnection as ActiveConnection
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.typing import ConfigType as ConfigType, VolSchemaType as VolSchemaType
from homeassistant.loader import IntegrationNotFound as IntegrationNotFound
from homeassistant.requirements import RequirementsNotFound as RequirementsNotFound, async_get_integration_with_requirements as async_get_integration_with_requirements
from types import ModuleType
from typing import Any, Literal, overload

type DeviceAutomationPlatformType = ModuleType | DeviceAutomationTriggerProtocol | DeviceAutomationConditionProtocol | DeviceAutomationActionProtocol
DOMAIN: str
CONFIG_SCHEMA: Incomplete
DEVICE_TRIGGER_BASE_SCHEMA: vol.Schema

@dataclass
class DeviceAutomationDetails:
    section: str
    get_automations_func: str
    get_capabilities_func: str

class DeviceAutomationType(Enum):
    TRIGGER = ...
    CONDITION = ...
    ACTION = ...

TYPES: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
@overload
async def async_get_device_automation_platform(hass: HomeAssistant, domain: str, automation_type: Literal[DeviceAutomationType.TRIGGER]) -> DeviceAutomationTriggerProtocol: ...
@overload
async def async_get_device_automation_platform(hass: HomeAssistant, domain: str, automation_type: Literal[DeviceAutomationType.CONDITION]) -> DeviceAutomationConditionProtocol: ...
@overload
async def async_get_device_automation_platform(hass: HomeAssistant, domain: str, automation_type: Literal[DeviceAutomationType.ACTION]) -> DeviceAutomationActionProtocol: ...
@overload
async def async_get_device_automation_platform(hass: HomeAssistant, domain: str, automation_type: DeviceAutomationType) -> DeviceAutomationPlatformType: ...
@callback
def _async_set_entity_device_automation_metadata(hass: HomeAssistant, automation: dict[str, Any]) -> None: ...
async def _async_get_device_automations_from_domain(hass: HomeAssistant, domain: str, automation_type: DeviceAutomationType, device_ids: Iterable[str], return_exceptions: bool) -> list[list[dict[str, Any]] | Exception]: ...
async def async_get_device_automations(hass: HomeAssistant, automation_type: DeviceAutomationType, device_ids: Iterable[str] | None = None) -> Mapping[str, list[dict[str, Any]]]: ...
async def _async_get_device_automation_capabilities(hass: HomeAssistant, automation_type: DeviceAutomationType, automation: Mapping[str, Any]) -> dict[str, Any]: ...
@callback
def async_get_entity_registry_entry_or_raise(hass: HomeAssistant, entity_registry_id: str) -> er.RegistryEntry: ...
@callback
def async_validate_entity_schema(hass: HomeAssistant, config: ConfigType, schema: VolSchemaType) -> ConfigType: ...
def handle_device_errors(func: Callable[[HomeAssistant, ActiveConnection, dict[str, Any]], Awaitable[None]]) -> Callable[[HomeAssistant, ActiveConnection, dict[str, Any]], Coroutine[Any, Any, None]]: ...
@websocket_api.async_response
@handle_device_errors
async def websocket_device_automation_list_actions(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
@handle_device_errors
async def websocket_device_automation_list_conditions(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
@handle_device_errors
async def websocket_device_automation_list_triggers(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
@handle_device_errors
async def websocket_device_automation_get_action_capabilities(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
@handle_device_errors
async def websocket_device_automation_get_condition_capabilities(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
@handle_device_errors
async def websocket_device_automation_get_trigger_capabilities(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
