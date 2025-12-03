from .const import OPTION_DIAGNOSTICS_INCLUDE_FIXTURES as OPTION_DIAGNOSTICS_INCLUDE_FIXTURES
from .coordinator import EnphaseConfigEntry as EnphaseConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_TOKEN as CONF_TOKEN, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.json import json_dumps as json_dumps
from homeassistant.util.json import json_loads as json_loads
from pyenphase.envoy import Envoy as Envoy
from typing import Any

CONF_TITLE: str
CLEAN_TEXT: str
TO_REDACT: Incomplete

async def _get_fixture_collection(envoy: Envoy, serial: str) -> dict[str, Any]: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: EnphaseConfigEntry) -> dict[str, Any]: ...
