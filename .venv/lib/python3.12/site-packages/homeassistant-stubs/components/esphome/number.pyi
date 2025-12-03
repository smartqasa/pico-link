from .entity import EsphomeEntity as EsphomeEntity, convert_api_error_ha_error as convert_api_error_ha_error, esphome_float_state_property as esphome_float_state_property, platform_async_setup_entry as platform_async_setup_entry
from .enum_mapper import EsphomeEnumMapper as EsphomeEnumMapper
from _typeshed import Incomplete
from aioesphomeapi import EntityInfo as EntityInfo, NumberInfo, NumberMode as EsphomeNumberMode, NumberState
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberMode as NumberMode
from homeassistant.core import callback as callback
from homeassistant.util.enum import try_parse_enum as try_parse_enum

NUMBER_MODES: EsphomeEnumMapper[EsphomeNumberMode, NumberMode]

class EsphomeNumber(EsphomeEntity[NumberInfo, NumberState], NumberEntity):
    _attr_device_class: Incomplete
    _attr_native_min_value: Incomplete
    _attr_native_max_value: Incomplete
    _attr_native_step: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_mode: Incomplete
    @callback
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @property
    @esphome_float_state_property
    def native_value(self) -> float | None: ...
    @convert_api_error_ha_error
    async def async_set_native_value(self, value: float) -> None: ...

async_setup_entry: Incomplete
