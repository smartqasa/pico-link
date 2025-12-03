from .entity import EsphomeEntity as EsphomeEntity, convert_api_error_ha_error as convert_api_error_ha_error, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from .enum_mapper import EsphomeEnumMapper as EsphomeEnumMapper
from _typeshed import Incomplete
from aioesphomeapi import EntityInfo as EntityInfo, TextInfo, TextMode as EsphomeTextMode, TextState
from homeassistant.components.text import TextEntity as TextEntity, TextMode as TextMode
from homeassistant.core import callback as callback

TEXT_MODES: EsphomeEnumMapper[EsphomeTextMode, TextMode]

class EsphomeText(EsphomeEntity[TextInfo, TextState], TextEntity):
    _attr_native_min: Incomplete
    _attr_native_max: Incomplete
    _attr_pattern: Incomplete
    _attr_mode: Incomplete
    @callback
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @property
    @esphome_state_property
    def native_value(self) -> str | None: ...
    @convert_api_error_ha_error
    async def async_set_value(self, value: str) -> None: ...

async_setup_entry: Incomplete
