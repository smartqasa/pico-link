from . import AnalyticsInsightsConfigEntry as AnalyticsInsightsConfigEntry
from .const import CONF_TRACKED_ADDONS as CONF_TRACKED_ADDONS, CONF_TRACKED_CUSTOM_INTEGRATIONS as CONF_TRACKED_CUSTOM_INTEGRATIONS, CONF_TRACKED_INTEGRATIONS as CONF_TRACKED_INTEGRATIONS, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from python_homeassistant_analytics import CustomIntegration as CustomIntegration, HomeassistantAnalyticsClient as HomeassistantAnalyticsClient
from python_homeassistant_analytics.models import Addon as Addon

@dataclass(frozen=True)
class AnalyticsData:
    active_installations: int
    reports_integrations: int
    addons: dict[str, int]
    core_integrations: dict[str, int]
    custom_integrations: dict[str, int]

class HomeassistantAnalyticsDataUpdateCoordinator(DataUpdateCoordinator[AnalyticsData]):
    config_entry: AnalyticsInsightsConfigEntry
    _client: Incomplete
    _tracked_addons: Incomplete
    _tracked_integrations: Incomplete
    _tracked_custom_integrations: Incomplete
    def __init__(self, hass: HomeAssistant, client: HomeassistantAnalyticsClient) -> None: ...
    async def _async_update_data(self) -> AnalyticsData: ...

def get_addon_value(data: dict[str, Addon], name_slug: str) -> int: ...
def get_custom_integration_value(data: dict[str, CustomIntegration], domain: str) -> int: ...
