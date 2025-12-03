from homeassistant.const import PRECISION_HALVES as PRECISION_HALVES, PRECISION_TENTHS as PRECISION_TENTHS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter

def display_temp(hass: HomeAssistant, temperature: float | None, unit: str, precision: float) -> float | None: ...
