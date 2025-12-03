from .coordinator import IslamicPrayerDataUpdateCoordinator as IslamicPrayerDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

PLATFORMS: Incomplete
_LOGGER: Incomplete
type IslamicPrayerTimesConfigEntry = ConfigEntry[IslamicPrayerDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, config_entry: IslamicPrayerTimesConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: IslamicPrayerTimesConfigEntry) -> bool: ...
async def async_options_updated(hass: HomeAssistant, entry: IslamicPrayerTimesConfigEntry) -> None: ...
