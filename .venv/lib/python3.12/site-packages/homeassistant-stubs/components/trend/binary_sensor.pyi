from . import PLATFORMS as PLATFORMS
from .const import ATTR_GRADIENT as ATTR_GRADIENT, ATTR_INVERT as ATTR_INVERT, ATTR_MIN_GRADIENT as ATTR_MIN_GRADIENT, ATTR_SAMPLE_COUNT as ATTR_SAMPLE_COUNT, ATTR_SAMPLE_DURATION as ATTR_SAMPLE_DURATION, CONF_INVERT as CONF_INVERT, CONF_MAX_SAMPLES as CONF_MAX_SAMPLES, CONF_MIN_GRADIENT as CONF_MIN_GRADIENT, CONF_MIN_SAMPLES as CONF_MIN_SAMPLES, CONF_SAMPLE_DURATION as CONF_SAMPLE_DURATION, DEFAULT_MAX_SAMPLES as DEFAULT_MAX_SAMPLES, DEFAULT_MIN_GRADIENT as DEFAULT_MIN_GRADIENT, DEFAULT_MIN_SAMPLES as DEFAULT_MIN_SAMPLES, DEFAULT_SAMPLE_DURATION as DEFAULT_SAMPLE_DURATION, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections import deque
from collections.abc import Mapping
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA, ENTITY_ID_FORMAT as ENTITY_ID_FORMAT
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, CONF_ATTRIBUTE as CONF_ATTRIBUTE, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_FRIENDLY_NAME as CONF_FRIENDLY_NAME, CONF_SENSORS as CONF_SENSORS, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.device import async_device_info_to_link_from_entity as async_device_info_to_link_from_entity
from homeassistant.helpers.entity import generate_entity_id as generate_entity_id
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.reload import async_setup_reload_service as async_setup_reload_service
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.dt import utcnow as utcnow
from typing import Any

_LOGGER: Incomplete

def _validate_min_max(data: dict[str, Any]) -> dict[str, Any]: ...

SENSOR_SCHEMA: Incomplete
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SensorTrend(BinarySensorEntity, RestoreEntity):
    _attr_should_poll: bool
    _gradient: float
    _state: bool | None
    _entity_id: Incomplete
    _attribute: Incomplete
    _invert: Incomplete
    _sample_duration: Incomplete
    _min_gradient: Incomplete
    _min_samples: Incomplete
    samples: deque
    _attr_name: Incomplete
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    entity_id: Incomplete
    def __init__(self, name: str, entity_id: str, attribute: str | None, invert: bool, sample_duration: int, min_gradient: float, min_samples: int, max_samples: int, unique_id: str | None = None, device_class: BinarySensorDeviceClass | None = None, sensor_entity_id: str | None = None, device_info: dr.DeviceInfo | None = None) -> None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any]: ...
    _attr_available: bool
    _attr_is_on: Incomplete
    async def async_added_to_hass(self) -> None: ...
    async def async_update(self) -> None: ...
    def _calculate_gradient(self) -> None: ...
