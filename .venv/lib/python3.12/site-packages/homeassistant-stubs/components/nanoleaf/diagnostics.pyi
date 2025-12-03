from . import NanoleafConfigEntry as NanoleafConfigEntry
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_TOKEN as CONF_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: NanoleafConfigEntry) -> dict[str, Any]: ...
