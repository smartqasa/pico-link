from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberMode as NumberMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DemoNumber(NumberEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_should_poll: bool
    _attr_assumed_state: Incomplete
    _attr_device_class: Incomplete
    _attr_translation_key: Incomplete
    _attr_mode: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_native_value: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_min_value: Incomplete
    _attr_native_max_value: Incomplete
    _attr_native_step: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, unique_id: str, device_name: str, state: float, translation_key: str | None, assumed_state: bool, *, device_class: NumberDeviceClass | None = None, mode: NumberMode = ..., native_min_value: float | None = None, native_max_value: float | None = None, native_step: float | None = None, unit_of_measurement: str | None = None) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
