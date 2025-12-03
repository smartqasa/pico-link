from .entity import EsphomeEntity as EsphomeEntity, convert_api_error_ha_error as convert_api_error_ha_error, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from _typeshed import Incomplete
from aioesphomeapi import EntityInfo as EntityInfo, ValveInfo, ValveState
from homeassistant.components.valve import ValveDeviceClass as ValveDeviceClass, ValveEntity as ValveEntity, ValveEntityFeature as ValveEntityFeature
from homeassistant.core import callback as callback
from homeassistant.util.enum import try_parse_enum as try_parse_enum
from typing import Any

class EsphomeValve(EsphomeEntity[ValveInfo, ValveState], ValveEntity):
    _attr_supported_features: Incomplete
    _attr_device_class: Incomplete
    _attr_assumed_state: Incomplete
    _attr_reports_position: Incomplete
    @callback
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @property
    @esphome_state_property
    def is_closed(self) -> bool: ...
    @property
    @esphome_state_property
    def is_opening(self) -> bool: ...
    @property
    @esphome_state_property
    def is_closing(self) -> bool: ...
    @property
    @esphome_state_property
    def current_valve_position(self) -> int | None: ...
    @convert_api_error_ha_error
    async def async_open_valve(self, **kwargs: Any) -> None: ...
    @convert_api_error_ha_error
    async def async_close_valve(self, **kwargs: Any) -> None: ...
    @convert_api_error_ha_error
    async def async_stop_valve(self, **kwargs: Any) -> None: ...
    @convert_api_error_ha_error
    async def async_set_valve_position(self, position: float) -> None: ...

async_setup_entry: Incomplete
