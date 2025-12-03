from .entity import EsphomeEntity as EsphomeEntity, convert_api_error_ha_error as convert_api_error_ha_error, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from _typeshed import Incomplete
from aioesphomeapi import EntityInfo as EntityInfo, SwitchInfo, SwitchState
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity
from homeassistant.core import callback as callback
from homeassistant.util.enum import try_parse_enum as try_parse_enum
from typing import Any

class EsphomeSwitch(EsphomeEntity[SwitchInfo, SwitchState], SwitchEntity):
    _attr_assumed_state: Incomplete
    _attr_device_class: Incomplete
    @callback
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @property
    @esphome_state_property
    def is_on(self) -> bool | None: ...
    @convert_api_error_ha_error
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @convert_api_error_ha_error
    async def async_turn_off(self, **kwargs: Any) -> None: ...

async_setup_entry: Incomplete
