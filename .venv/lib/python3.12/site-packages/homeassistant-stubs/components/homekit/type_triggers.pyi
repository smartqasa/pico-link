from .accessories import HomeAccessory as HomeAccessory, TYPES as TYPES
from .aidmanager import get_system_unique_id as get_system_unique_id
from .const import CHAR_NAME as CHAR_NAME, CHAR_PROGRAMMABLE_SWITCH_EVENT as CHAR_PROGRAMMABLE_SWITCH_EVENT, CHAR_SERVICE_LABEL_INDEX as CHAR_SERVICE_LABEL_INDEX, CHAR_SERVICE_LABEL_NAMESPACE as CHAR_SERVICE_LABEL_NAMESPACE, SERV_SERVICE_LABEL as SERV_SERVICE_LABEL, SERV_STATELESS_PROGRAMMABLE_SWITCH as SERV_STATELESS_PROGRAMMABLE_SWITCH
from .util import cleanup_name_for_homekit as cleanup_name_for_homekit
from _typeshed import Incomplete
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Context as Context, callback as callback
from homeassistant.helpers.trigger import async_initialize_triggers as async_initialize_triggers
from pyhap.util import callback as pyhap_callback
from typing import Any

_LOGGER: Incomplete

class DeviceTriggerAccessory(HomeAccessory):
    _device_triggers: Incomplete
    _remove_triggers: CALLBACK_TYPE | None
    triggers: Incomplete
    def __init__(self, *args: Any, device_triggers: list[dict[str, Any]] | None = None, device_id: str | None = None) -> None: ...
    @callback
    def _remove_triggers_if_configured(self) -> None: ...
    async def async_attach(self) -> None: ...
    @pyhap_callback
    @callback
    def run(self) -> None: ...
    async def async_trigger(self, run_variables: dict[str, Any], context: Context | None = None, skip_condition: bool = False) -> None: ...
    @callback
    def async_stop(self) -> None: ...
    @property
    def available(self) -> bool: ...
