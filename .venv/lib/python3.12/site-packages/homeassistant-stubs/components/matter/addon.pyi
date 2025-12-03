from .const import ADDON_SLUG as ADDON_SLUG, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.components.hassio import AddonManager as AddonManager
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.singleton import singleton as singleton

DATA_ADDON_MANAGER: Incomplete

@callback
def get_addon_manager(hass: HomeAssistant) -> AddonManager: ...
