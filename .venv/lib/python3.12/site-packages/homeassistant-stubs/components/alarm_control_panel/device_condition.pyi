from . import AlarmControlPanelState as AlarmControlPanelState, DOMAIN as DOMAIN
from .const import AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, CONDITION_ARMED_AWAY as CONDITION_ARMED_AWAY, CONDITION_ARMED_CUSTOM_BYPASS as CONDITION_ARMED_CUSTOM_BYPASS, CONDITION_ARMED_HOME as CONDITION_ARMED_HOME, CONDITION_ARMED_NIGHT as CONDITION_ARMED_NIGHT, CONDITION_ARMED_VACATION as CONDITION_ARMED_VACATION, CONDITION_DISARMED as CONDITION_DISARMED, CONDITION_TRIGGERED as CONDITION_TRIGGERED
from _typeshed import Incomplete
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_CONDITION as CONF_CONDITION, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import condition as condition
from homeassistant.helpers.config_validation import DEVICE_CONDITION_BASE_SCHEMA as DEVICE_CONDITION_BASE_SCHEMA
from homeassistant.helpers.entity import get_supported_features as get_supported_features
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from typing import Final

CONDITION_TYPES: Final[set[str]]
CONDITION_SCHEMA: Final[Incomplete]

async def async_get_conditions(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
@callback
def async_condition_from_config(hass: HomeAssistant, config: ConfigType) -> condition.ConditionCheckerType: ...
