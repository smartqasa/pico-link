from .entity import EsphomeEntity as EsphomeEntity, convert_api_error_ha_error as convert_api_error_ha_error, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from _typeshed import Incomplete
from aioesphomeapi import CoverInfo, CoverState, EntityInfo as EntityInfo
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, ATTR_TILT_POSITION as ATTR_TILT_POSITION, CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.core import callback as callback
from homeassistant.util.enum import try_parse_enum as try_parse_enum
from typing import Any

class EsphomeCover(EsphomeEntity[CoverInfo, CoverState], CoverEntity):
    _attr_supported_features: Incomplete
    _attr_device_class: Incomplete
    _attr_assumed_state: Incomplete
    @callback
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @property
    @esphome_state_property
    def is_closed(self) -> bool | None: ...
    @property
    @esphome_state_property
    def is_opening(self) -> bool: ...
    @property
    @esphome_state_property
    def is_closing(self) -> bool: ...
    @property
    @esphome_state_property
    def current_cover_position(self) -> int | None: ...
    @property
    @esphome_state_property
    def current_cover_tilt_position(self) -> int | None: ...
    @convert_api_error_ha_error
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    @convert_api_error_ha_error
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    @convert_api_error_ha_error
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    @convert_api_error_ha_error
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    @convert_api_error_ha_error
    async def async_open_cover_tilt(self, **kwargs: Any) -> None: ...
    @convert_api_error_ha_error
    async def async_close_cover_tilt(self, **kwargs: Any) -> None: ...
    @convert_api_error_ha_error
    async def async_set_cover_tilt_position(self, **kwargs: Any) -> None: ...

async_setup_entry: Incomplete
