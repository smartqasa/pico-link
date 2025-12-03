from .coordinator import ESPHomeDashboardCoordinator as ESPHomeDashboardCoordinator
from .dashboard import async_get_dashboard as async_get_dashboard
from .domain_data import DomainData as DomainData
from .entity import EsphomeEntity as EsphomeEntity, convert_api_error_ha_error as convert_api_error_ha_error, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from .entry_data import RuntimeEntryData as RuntimeEntryData
from _typeshed import Incomplete
from aioesphomeapi import DeviceInfo as ESPHomeDeviceInfo, EntityInfo as EntityInfo, UpdateInfo, UpdateState
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util.enum import try_parse_enum as try_parse_enum
from typing import Any

KEY_UPDATE_LOCK: str
NO_FEATURES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ESPHomeDashboardUpdateEntity(CoordinatorEntity[ESPHomeDashboardCoordinator], UpdateEntity):
    _attr_has_entity_name: bool
    _attr_device_class: Incomplete
    _attr_title: str
    _attr_name: str
    _attr_release_url: str
    _attr_entity_registry_enabled_default: bool
    _entry_data: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, entry_data: RuntimeEntryData, coordinator: ESPHomeDashboardCoordinator) -> None: ...
    _attr_supported_features: Incomplete
    _attr_installed_version: Incomplete
    _attr_latest_version: Incomplete
    @callback
    def _update_attrs(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @property
    def _device_info(self) -> ESPHomeDeviceInfo: ...
    @property
    def available(self) -> bool: ...
    @callback
    def _handle_device_update(self, static_info: list[EntityInfo] | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...

class ESPHomeUpdateEntity(EsphomeEntity[UpdateInfo, UpdateState], UpdateEntity):
    _attr_supported_features: Incomplete
    _attr_device_class: Incomplete
    @callback
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @property
    @esphome_state_property
    def installed_version(self) -> str | None: ...
    @property
    @esphome_state_property
    def in_progress(self) -> bool: ...
    @property
    @esphome_state_property
    def latest_version(self) -> str | None: ...
    @property
    @esphome_state_property
    def release_summary(self) -> str | None: ...
    @property
    @esphome_state_property
    def release_url(self) -> str | None: ...
    @property
    @esphome_state_property
    def title(self) -> str | None: ...
    @property
    @esphome_state_property
    def update_percentage(self) -> int | None: ...
    @convert_api_error_ha_error
    async def async_update(self) -> None: ...
    @convert_api_error_ha_error
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
