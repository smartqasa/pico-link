from .const import CONF_ROUND_DIGITS as CONF_ROUND_DIGITS, CONF_TIME_WINDOW as CONF_TIME_WINDOW, CONF_UNIT as CONF_UNIT, CONF_UNIT_PREFIX as CONF_UNIT_PREFIX, CONF_UNIT_TIME as CONF_UNIT_TIME
from _typeshed import Incomplete
from datetime import datetime, timedelta
from decimal import Decimal
from homeassistant.components.sensor import ATTR_STATE_CLASS as ATTR_STATE_CLASS, RestoreSensor as RestoreSensor, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, CONF_NAME as CONF_NAME, CONF_SOURCE as CONF_SOURCE, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfTime as UnitOfTime
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device import async_device_info_to_link_from_entity as async_device_info_to_link_from_entity
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

_LOGGER: Incomplete
ATTR_SOURCE_ID: str
UNIT_PREFIXES: Incomplete
UNIT_TIME: Incomplete
DEFAULT_ROUND: int
DEFAULT_TIME_WINDOW: int
PLATFORM_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class DerivativeSensor(RestoreSensor, SensorEntity):
    _attr_translation_key: str
    _attr_should_poll: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _sensor_source_id: Incomplete
    _round_digits: Incomplete
    _attr_native_value: Incomplete
    _state_list: list[tuple[datetime, datetime, Decimal]]
    _attr_name: Incomplete
    _attr_extra_state_attributes: Incomplete
    _unit_template: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _unit_prefix: Incomplete
    _unit_time: Incomplete
    _time_window: Incomplete
    def __init__(self, *, name: str | None, round_digits: int, source_entity: str, time_window: timedelta, unit_of_measurement: str | None, unit_prefix: str | None, unit_time: UnitOfTime, unique_id: str | None, device_info: DeviceInfo | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
