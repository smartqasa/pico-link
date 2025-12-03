from . import DATA_RFXOBJECT as DATA_RFXOBJECT, DOMAIN as DOMAIN
from .helpers import async_get_device_object as async_get_device_object
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.device_automation import InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_TYPE as CONF_TYPE
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType

CONF_DATA: str
CONF_SUBTYPE: str
ACTION_TYPE_COMMAND: str
ACTION_TYPE_STATUS: str
ACTION_TYPES: Incomplete
ACTION_SELECTION: Incomplete
ACTION_SCHEMA: Incomplete

async def async_get_actions(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
def _get_commands(hass: HomeAssistant, device_id: str, action_type: str) -> tuple[dict[str, str], Callable[..., None]]: ...
async def async_validate_action_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_call_action_from_config(hass: HomeAssistant, config: ConfigType, variables: TemplateVarsType, context: Context | None) -> None: ...
