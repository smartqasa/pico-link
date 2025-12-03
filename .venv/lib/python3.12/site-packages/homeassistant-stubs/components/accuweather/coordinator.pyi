from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from _typeshed import Incomplete
from accuweather import AccuWeather as AccuWeather
from dataclasses import dataclass
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, TimestampDataUpdateCoordinator as TimestampDataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

EXCEPTIONS: Incomplete
_LOGGER: Incomplete

@dataclass
class AccuWeatherData:
    coordinator_observation: AccuWeatherObservationDataUpdateCoordinator
    coordinator_daily_forecast: AccuWeatherDailyForecastDataUpdateCoordinator
type AccuWeatherConfigEntry = ConfigEntry[AccuWeatherData]

class AccuWeatherObservationDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    accuweather: Incomplete
    location_key: Incomplete
    device_info: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: AccuWeatherConfigEntry, accuweather: AccuWeather, name: str, coordinator_type: str, update_interval: timedelta) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...

class AccuWeatherDailyForecastDataUpdateCoordinator(TimestampDataUpdateCoordinator[list[dict[str, Any]]]):
    accuweather: Incomplete
    location_key: Incomplete
    device_info: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: AccuWeatherConfigEntry, accuweather: AccuWeather, name: str, coordinator_type: str, update_interval: timedelta) -> None: ...
    async def _async_update_data(self) -> list[dict[str, Any]]: ...

def _get_device_info(location_key: str, name: str) -> DeviceInfo: ...
