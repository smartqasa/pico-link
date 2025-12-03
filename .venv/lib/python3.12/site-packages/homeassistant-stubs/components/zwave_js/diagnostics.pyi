from .const import DATA_CLIENT as DATA_CLIENT, USER_AGENT as USER_AGENT
from .helpers import ZwaveValueMatcher as ZwaveValueMatcher, get_home_and_node_id_from_device_entry as get_home_and_node_id_from_device_entry, get_state_key_from_unique_id as get_state_key_from_unique_id, get_value_id_from_unique_id as get_value_id_from_unique_id, value_matches_matcher as value_matches_matcher
from _typeshed import Incomplete
from homeassistant.components.diagnostics import REDACTED as REDACTED, async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any
from zwave_js_server.client import Client as Client
from zwave_js_server.model.node import Node as Node
from zwave_js_server.model.value import ValueDataType as ValueDataType

KEYS_TO_REDACT: Incomplete
VALUES_TO_REDACT: Incomplete

def _redacted_value(zwave_value: ValueDataType) -> ValueDataType: ...
def optionally_redact_value_of_zwave_value(zwave_value: ValueDataType) -> ValueDataType: ...
def redact_node_state(node_state: dict) -> dict: ...
def get_device_entities(hass: HomeAssistant, node: Node, config_entry: ConfigEntry, device: dr.DeviceEntry) -> list[dict[str, Any]]: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: ConfigEntry) -> dict[str, Any]: ...
async def async_get_device_diagnostics(hass: HomeAssistant, config_entry: ConfigEntry, device: dr.DeviceEntry) -> dict[str, Any]: ...
