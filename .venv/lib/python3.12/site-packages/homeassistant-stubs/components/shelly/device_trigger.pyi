from .const import ATTR_CHANNEL as ATTR_CHANNEL, ATTR_CLICK_TYPE as ATTR_CLICK_TYPE, BLOCK_INPUTS_EVENTS_TYPES as BLOCK_INPUTS_EVENTS_TYPES, CONF_SUBTYPE as CONF_SUBTYPE, DOMAIN as DOMAIN, EVENT_SHELLY_CLICK as EVENT_SHELLY_CLICK, INPUTS_EVENTS_SUBTYPES as INPUTS_EVENTS_SUBTYPES, RPC_INPUTS_EVENTS_TYPES as RPC_INPUTS_EVENTS_TYPES, SHBTN_MODELS as SHBTN_MODELS
from .coordinator import get_block_coordinator_by_device_id as get_block_coordinator_by_device_id, get_rpc_coordinator_by_device_id as get_rpc_coordinator_by_device_id
from .utils import get_block_input_triggers as get_block_input_triggers, get_rpc_input_triggers as get_rpc_input_triggers, get_shbtn_input_triggers as get_shbtn_input_triggers
from _typeshed import Incomplete
from homeassistant.components.device_automation import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA, InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_EVENT as CONF_EVENT, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Final

TRIGGER_SCHEMA: Final[Incomplete]

def append_input_triggers(triggers: list[dict[str, str]], input_triggers: list[tuple[str, str]], device_id: str) -> None: ...
async def async_validate_trigger_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_get_triggers(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
