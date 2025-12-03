from .const import ATTR_CHANNEL as ATTR_CHANNEL, ATTR_CLICK_TYPE as ATTR_CLICK_TYPE, ATTR_DEVICE as ATTR_DEVICE, BLOCK_INPUTS_EVENTS_TYPES as BLOCK_INPUTS_EVENTS_TYPES, DOMAIN as DOMAIN, EVENT_SHELLY_CLICK as EVENT_SHELLY_CLICK, RPC_INPUTS_EVENTS_TYPES as RPC_INPUTS_EVENTS_TYPES
from .coordinator import get_block_coordinator_by_device_id as get_block_coordinator_by_device_id, get_rpc_coordinator_by_device_id as get_rpc_coordinator_by_device_id
from .utils import get_rpc_entity_name as get_rpc_entity_name
from collections.abc import Callable as Callable
from homeassistant.components.logbook import LOGBOOK_ENTRY_MESSAGE as LOGBOOK_ENTRY_MESSAGE, LOGBOOK_ENTRY_NAME as LOGBOOK_ENTRY_NAME
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback

@callback
def async_describe_events(hass: HomeAssistant, async_describe_event: Callable[[str, str, Callable[[Event], dict]], None]) -> None: ...
