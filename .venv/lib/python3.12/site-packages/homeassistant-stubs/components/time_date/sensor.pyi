from .const import OPTION_TYPES as OPTION_TYPES
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from datetime import datetime
from homeassistant.components.sensor import ENTITY_ID_FORMAT as ENTITY_ID_FORMAT, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DISPLAY_OPTIONS as CONF_DISPLAY_OPTIONS, EVENT_CORE_CONFIG_UPDATE as EVENT_CORE_CONFIG_UPDATE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
TIME_STR_FORMAT: str
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TimeDateSensor(SensorEntity):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    _state: str | None
    unsub: CALLBACK_TYPE | None
    _attr_translation_key: Incomplete
    type: Incomplete
    entity_id: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, option_type: str, entry_id: str | None = None) -> None: ...
    @property
    def native_value(self) -> str | None: ...
    @property
    def icon(self) -> str: ...
    @callback
    def async_start_preview(self, preview_callback: Callable[[str, Mapping[str, Any]], None]) -> CALLBACK_TYPE: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def get_next_interval(self, time_date: datetime) -> datetime: ...
    def _update_internal_state(self, time_date: datetime) -> None: ...
    def _update_state_and_setup_listener(self) -> None: ...
    @callback
    def point_in_time_listener(self, time_date: datetime) -> None: ...
