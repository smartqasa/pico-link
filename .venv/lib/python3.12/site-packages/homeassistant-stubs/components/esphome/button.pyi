from .entity import EsphomeEntity as EsphomeEntity, convert_api_error_ha_error as convert_api_error_ha_error, platform_async_setup_entry as platform_async_setup_entry
from _typeshed import Incomplete
from aioesphomeapi import ButtonInfo, EntityInfo as EntityInfo, EntityState
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity
from homeassistant.core import callback as callback
from homeassistant.util.enum import try_parse_enum as try_parse_enum

class EsphomeButton(EsphomeEntity[ButtonInfo, EntityState], ButtonEntity):
    _attr_device_class: Incomplete
    @callback
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @callback
    def _on_device_update(self) -> None: ...
    @convert_api_error_ha_error
    async def async_press(self) -> None: ...

async_setup_entry: Incomplete
