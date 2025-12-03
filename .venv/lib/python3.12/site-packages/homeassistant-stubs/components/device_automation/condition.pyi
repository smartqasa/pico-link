import voluptuous as vol
from . import DeviceAutomationType as DeviceAutomationType, async_get_device_automation_platform as async_get_device_automation_platform
from .helpers import async_validate_device_automation_config as async_validate_device_automation_config
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import condition as condition
from homeassistant.helpers.condition import ConditionProtocol as ConditionProtocol, trace_condition_function as trace_condition_function
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Protocol

class DeviceAutomationConditionProtocol(ConditionProtocol, Protocol):
    async def async_get_condition_capabilities(self, hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
    async def async_get_conditions(self, hass: HomeAssistant, device_id: str) -> list[dict[str, Any]]: ...

async def async_validate_condition_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_condition_from_config(hass: HomeAssistant, config: ConfigType) -> condition.ConditionCheckerType: ...
