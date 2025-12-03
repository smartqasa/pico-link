from .coordinator import ForecastSolarDataUpdateCoordinator as ForecastSolarDataUpdateCoordinator
from homeassistant.core import HomeAssistant as HomeAssistant

async def async_get_solar_forecast(hass: HomeAssistant, config_entry_id: str) -> dict[str, dict[str, float | int]] | None: ...
