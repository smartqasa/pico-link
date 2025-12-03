from . import BryantEvolutionConfigEntry as BryantEvolutionConfigEntry, names as names
from .const import CONF_SYSTEM_ZONE as CONF_SYSTEM_ZONE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from evolutionhttp import BryantEvolutionLocalClient as BryantEvolutionLocalClient
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.const import UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: BryantEvolutionConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BryantEvolutionClimate(ClimateEntity):
    _attr_has_entity_name: bool
    _attr_temperature_unit: Incomplete
    _attr_supported_features: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_fan_modes: Incomplete
    _client: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, client: BryantEvolutionLocalClient, system_id: int, zone_id: int, sam_uid: str) -> None: ...
    _attr_current_temperature: Incomplete
    _attr_fan_mode: Incomplete
    _attr_target_temperature: Incomplete
    _attr_target_temperature_high: Incomplete
    _attr_target_temperature_low: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_hvac_action: Incomplete
    async def async_update(self) -> None: ...
    async def _read_hvac_mode(self) -> HVACMode: ...
    async def _read_hvac_action(self) -> HVACAction: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
