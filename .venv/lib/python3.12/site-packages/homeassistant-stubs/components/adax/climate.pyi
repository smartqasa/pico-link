from .const import ACCOUNT_ID as ACCOUNT_ID, CONNECTION_TYPE as CONNECTION_TYPE, DOMAIN as DOMAIN, LOCAL as LOCAL
from _typeshed import Incomplete
from adax import Adax
from adax_local import Adax as AdaxLocal
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, CONF_TOKEN as CONF_TOKEN, CONF_UNIQUE_ID as CONF_UNIQUE_ID, PRECISION_WHOLE as PRECISION_WHOLE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AdaxDevice(ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_max_temp: int
    _attr_min_temp: int
    _attr_supported_features: Incomplete
    _attr_target_temperature_step = PRECISION_WHOLE
    _attr_temperature_unit: Incomplete
    _device_id: Incomplete
    _adax_data_handler: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, heater_data: dict[str, Any], adax_data_handler: Adax) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    _attr_name: Incomplete
    _attr_current_temperature: Incomplete
    _attr_target_temperature: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_icon: str
    async def async_update(self) -> None: ...

class LocalAdaxDevice(ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_max_temp: int
    _attr_min_temp: int
    _attr_supported_features: Incomplete
    _attr_target_temperature_step = PRECISION_WHOLE
    _attr_temperature_unit: Incomplete
    _adax_data_handler: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, adax_data_handler: AdaxLocal, unique_id: str) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    _attr_current_temperature: Incomplete
    _attr_available: Incomplete
    _attr_icon: str
    _attr_target_temperature: Incomplete
    async def async_update(self) -> None: ...
