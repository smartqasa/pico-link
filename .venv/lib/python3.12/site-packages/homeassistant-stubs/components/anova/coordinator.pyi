from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from anova_wifi import APCUpdate, APCWifiDevice as APCWifiDevice
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete

class AnovaCoordinator(DataUpdateCoordinator[APCUpdate]):
    config_entry: ConfigEntry
    device_unique_id: Incomplete
    anova_device: Incomplete
    device_info: DeviceInfo | None
    sensor_data_set: bool
    def __init__(self, hass: HomeAssistant, anova_device: APCWifiDevice) -> None: ...
