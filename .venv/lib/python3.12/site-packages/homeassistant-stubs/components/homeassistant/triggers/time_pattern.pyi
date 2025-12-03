from _typeshed import Incomplete
from homeassistant.const import CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.event import async_track_time_change as async_track_time_change
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

CONF_HOURS: str
CONF_MINUTES: str
CONF_SECONDS: str

class TimePattern:
    maximum: Incomplete
    def __init__(self, maximum: int) -> None: ...
    def __call__(self, value: Any) -> str | int: ...

TRIGGER_SCHEMA: Incomplete

async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
