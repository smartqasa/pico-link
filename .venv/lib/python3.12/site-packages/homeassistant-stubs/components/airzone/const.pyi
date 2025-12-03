from aioairzone.common import TemperatureUnit
from homeassistant.const import UnitOfTemperature as UnitOfTemperature
from typing import Final

DOMAIN: Final[str]
MANUFACTURER: Final[str]
AIOAIRZONE_DEVICE_TIMEOUT_SEC: Final[int]
API_TEMPERATURE_STEP: Final[float]
TEMP_UNIT_LIB_TO_HASS: Final[dict[TemperatureUnit, str]]
