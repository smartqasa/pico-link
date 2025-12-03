from .entity import MatterEntity as MatterEntity
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.update import ATTR_LATEST_VERSION as ATTR_LATEST_VERSION, UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform, STATE_ON as STATE_ON
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.restore_state import ExtraStoredData as ExtraStoredData
from matter_server.common.models import MatterSoftwareVersion
from typing import Any

SCAN_INTERVAL: Incomplete
POLL_AFTER_INSTALL: int
ATTR_SOFTWARE_UPDATE: str

@dataclass
class MatterUpdateExtraStoredData(ExtraStoredData):
    software_update: MatterSoftwareVersion | None = ...
    def as_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> MatterUpdateExtraStoredData: ...

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MatterUpdate(MatterEntity, UpdateEntity):
    _attr_should_poll: bool
    _software_update: MatterSoftwareVersion | None
    _cancel_update: CALLBACK_TYPE | None
    _attr_supported_features: Incomplete
    _attr_installed_version: Incomplete
    _attr_in_progress: bool
    _attr_update_percentage: Incomplete
    @callback
    def _update_from_device(self) -> None: ...
    _attr_latest_version: Incomplete
    _attr_release_url: Incomplete
    async def async_update(self) -> None: ...
    async def async_release_notes(self) -> str | None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def extra_restore_state_data(self) -> MatterUpdateExtraStoredData: ...
    @property
    def entity_picture(self) -> str | None: ...
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
    async def _async_update_future(self, now: datetime | None = None) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
