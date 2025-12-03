import voluptuous as vol
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.device_automation import toggle_entity as toggle_entity
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.condition import ConditionCheckerType as ConditionCheckerType
from homeassistant.helpers.typing import ConfigType as ConfigType

CONDITION_SCHEMA: Incomplete

@callback
def async_condition_from_config(hass: HomeAssistant, config: ConfigType) -> ConditionCheckerType: ...
async def async_get_conditions(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
async def async_get_condition_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
