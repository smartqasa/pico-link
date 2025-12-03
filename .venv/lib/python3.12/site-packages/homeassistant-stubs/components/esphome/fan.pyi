from .entity import EsphomeEntity as EsphomeEntity, convert_api_error_ha_error as convert_api_error_ha_error, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from .enum_mapper import EsphomeEnumMapper as EsphomeEnumMapper
from _typeshed import Incomplete
from aioesphomeapi import EntityInfo as EntityInfo, FanDirection, FanInfo, FanState
from homeassistant.components.fan import DIRECTION_FORWARD as DIRECTION_FORWARD, DIRECTION_REVERSE as DIRECTION_REVERSE, FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.core import callback as callback
from homeassistant.util.percentage import ordered_list_item_to_percentage as ordered_list_item_to_percentage, percentage_to_ordered_list_item as percentage_to_ordered_list_item, percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from typing import Any

ORDERED_NAMED_FAN_SPEEDS: Incomplete
_FAN_DIRECTIONS: EsphomeEnumMapper[FanDirection, str]

class EsphomeFan(EsphomeEntity[FanInfo, FanState], FanEntity):
    _supports_speed_levels: bool
    async def async_set_percentage(self, percentage: int) -> None: ...
    @convert_api_error_ha_error
    async def _async_set_percentage(self, percentage: int | None) -> None: ...
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    @convert_api_error_ha_error
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @convert_api_error_ha_error
    async def async_oscillate(self, oscillating: bool) -> None: ...
    @convert_api_error_ha_error
    async def async_set_direction(self, direction: str) -> None: ...
    @convert_api_error_ha_error
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    @property
    @esphome_state_property
    def is_on(self) -> bool | None: ...
    @property
    @esphome_state_property
    def percentage(self) -> int | None: ...
    @property
    @esphome_state_property
    def oscillating(self) -> bool | None: ...
    @property
    @esphome_state_property
    def current_direction(self) -> str | None: ...
    @property
    @esphome_state_property
    def preset_mode(self) -> str | None: ...
    _attr_supported_features: Incomplete
    _attr_preset_modes: Incomplete
    _attr_speed_count: Incomplete
    @callback
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...

async_setup_entry: Incomplete
