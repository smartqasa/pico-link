from . import UnifiConfigEntry as UnifiConfigEntry
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.diagnostics import REDACTED as REDACTED, async_redact_data as async_redact_data
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import format_mac as format_mac
from typing import Any

TO_REDACT: Incomplete
REDACT_CONFIG: Incomplete
REDACT_CLIENTS: Incomplete
REDACT_DEVICES: Incomplete
REDACT_WLANS: Incomplete

@callback
def async_replace_dict_data(data: Mapping, to_replace: dict[str, str]) -> dict[str, Any]: ...
@callback
def async_replace_list_data(data: list | set | tuple, to_replace: dict[str, str]) -> list[Any]: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: UnifiConfigEntry) -> dict[str, Any]: ...
