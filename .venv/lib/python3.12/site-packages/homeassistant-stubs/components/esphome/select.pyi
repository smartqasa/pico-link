from .const import DOMAIN as DOMAIN
from .entity import EsphomeAssistEntity as EsphomeAssistEntity, EsphomeEntity as EsphomeEntity, convert_api_error_ha_error as convert_api_error_ha_error, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from .entry_data import ESPHomeConfigEntry as ESPHomeConfigEntry, RuntimeEntryData as RuntimeEntryData
from _typeshed import Incomplete
from aioesphomeapi import EntityInfo as EntityInfo, SelectInfo, SelectState
from homeassistant.components.assist_pipeline.select import AssistPipelineSelect as AssistPipelineSelect, VadSensitivitySelect as VadSensitivitySelect
from homeassistant.components.assist_satellite import AssistSatelliteConfiguration as AssistSatelliteConfiguration
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import restore_state as restore_state
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ESPHomeConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EsphomeSelect(EsphomeEntity[SelectInfo, SelectState], SelectEntity):
    _attr_options: Incomplete
    @callback
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @property
    @esphome_state_property
    def current_option(self) -> str | None: ...
    @convert_api_error_ha_error
    async def async_select_option(self, option: str) -> None: ...

class EsphomeAssistPipelineSelect(EsphomeAssistEntity, AssistPipelineSelect):
    def __init__(self, hass: HomeAssistant, entry_data: RuntimeEntryData) -> None: ...

class EsphomeVadSensitivitySelect(EsphomeAssistEntity, VadSensitivitySelect):
    def __init__(self, hass: HomeAssistant, entry_data: RuntimeEntryData) -> None: ...

class EsphomeAssistSatelliteWakeWordSelect(EsphomeAssistEntity, SelectEntity, restore_state.RestoreEntity):
    entity_description: Incomplete
    _attr_should_poll: bool
    _attr_current_option: str | None
    _attr_options: list[str]
    _attr_unique_id: Incomplete
    _wake_words: dict[str, str]
    def __init__(self, hass: HomeAssistant, entry_data: RuntimeEntryData) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
    def async_satellite_config_updated(self, config: AssistSatelliteConfiguration) -> None: ...
