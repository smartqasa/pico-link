from aioelectricitymaps import ElectricityMaps as ElectricityMaps
from aioelectricitymaps.models import CarbonIntensityResponse as CarbonIntensityResponse
from collections.abc import Mapping
from homeassistant.const import CONF_COUNTRY_CODE as CONF_COUNTRY_CODE, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def fetch_latest_carbon_intensity(hass: HomeAssistant, em: ElectricityMaps, config: Mapping[str, Any]) -> CarbonIntensityResponse: ...
