from . import DevoloHomeControlConfigEntry as DevoloHomeControlConfigEntry
from .devolo_multi_level_switch import DevoloMultiLevelSwitchDeviceEntity as DevoloMultiLevelSwitchDeviceEntity
from _typeshed import Incomplete
from devolo_home_control_api.devices.zwave import Zwave as Zwave
from devolo_home_control_api.homecontrol import HomeControl as HomeControl
from homeassistant.components.climate import ATTR_TEMPERATURE as ATTR_TEMPERATURE, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode
from homeassistant.const import PRECISION_HALVES as PRECISION_HALVES, PRECISION_TENTHS as PRECISION_TENTHS, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: DevoloHomeControlConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloClimateDeviceEntity(DevoloMultiLevelSwitchDeviceEntity, ClimateEntity):
    _attr_supported_features: Incomplete
    _attr_target_temperature_step = PRECISION_HALVES
    _attr_temperature_unit: Incomplete
    _attr_precision = PRECISION_TENTHS
    _attr_hvac_mode: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    def __init__(self, homecontrol: HomeControl, device_instance: Zwave, element_uid: str) -> None: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    def set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    def set_temperature(self, **kwargs: Any) -> None: ...
