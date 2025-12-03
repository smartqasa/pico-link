from .coordinator import ProximityConfigEntry as ProximityConfigEntry
from _typeshed import Incomplete
from homeassistant.components.device_tracker import ATTR_GPS as ATTR_GPS, ATTR_IP as ATTR_IP, ATTR_MAC as ATTR_MAC
from homeassistant.components.diagnostics import REDACTED as REDACTED, async_redact_data as async_redact_data
from homeassistant.components.person import ATTR_USER_ID as ATTR_USER_ID
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, STATE_HOME as STATE_HOME, STATE_NOT_HOME as STATE_NOT_HOME, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ProximityConfigEntry) -> dict[str, Any]: ...
