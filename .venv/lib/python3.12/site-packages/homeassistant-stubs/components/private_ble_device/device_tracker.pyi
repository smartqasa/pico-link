from .entity import BasePrivateDeviceEntity as BasePrivateDeviceEntity
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components import bluetooth as bluetooth
from homeassistant.components.device_tracker import SourceType as SourceType
from homeassistant.components.device_tracker.config_entry import BaseTrackerEntity as BaseTrackerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_HOME as STATE_HOME, STATE_NOT_HOME as STATE_NOT_HOME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BasePrivateDeviceTracker(BasePrivateDeviceEntity, BaseTrackerEntity):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    _attr_translation_key: str
    _attr_name: Incomplete
    @property
    def extra_state_attributes(self) -> Mapping[str, str]: ...
    _last_info: Incomplete
    @callback
    def _async_track_unavailable(self, service_info: bluetooth.BluetoothServiceInfoBleak) -> None: ...
    @callback
    def _async_track_service_info(self, service_info: bluetooth.BluetoothServiceInfoBleak, change: bluetooth.BluetoothChange) -> None: ...
    @property
    def state(self) -> str: ...
    @property
    def source_type(self) -> SourceType: ...
