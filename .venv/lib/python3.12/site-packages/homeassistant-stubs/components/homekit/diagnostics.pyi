from .accessories import HomeAccessory as HomeAccessory, HomeBridge as HomeBridge
from .models import HomeKitConfigEntry as HomeKitConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.core import HomeAssistant as HomeAssistant
from pyhap.accessory_driver import AccessoryDriver as AccessoryDriver
from pyhap.state import State as State
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: HomeKitConfigEntry) -> dict[str, Any]: ...
def _get_bridge_diagnostics(hass: HomeAssistant, bridge: HomeBridge) -> dict[int, Any]: ...
def _get_accessory_diagnostics(hass: HomeAssistant, accessory: HomeAccessory) -> dict[str, Any]: ...
