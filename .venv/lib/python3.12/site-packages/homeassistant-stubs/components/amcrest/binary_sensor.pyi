from . import AmcrestDevice as AmcrestDevice
from .const import BINARY_SENSOR_SCAN_INTERVAL_SECS as BINARY_SENSOR_SCAN_INTERVAL_SECS, DATA_AMCREST as DATA_AMCREST, DEVICES as DEVICES, SERVICE_EVENT as SERVICE_EVENT, SERVICE_UPDATE as SERVICE_UPDATE
from .helpers import log_update_error as log_update_error, service_signal as service_signal
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import CONF_BINARY_SENSORS as CONF_BINARY_SENSORS, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util import Throttle as Throttle

@dataclass(frozen=True)
class AmcrestSensorEntityDescription(BinarySensorEntityDescription):
    event_codes: set[str] | None = ...
    should_poll: bool = ...

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
_ONLINE_SCAN_INTERVAL: Incomplete
_AUDIO_DETECTED_KEY: str
_AUDIO_DETECTED_POLLED_KEY: str
_AUDIO_DETECTED_NAME: str
_AUDIO_DETECTED_EVENT_CODES: Incomplete
_CROSSLINE_DETECTED_KEY: str
_CROSSLINE_DETECTED_POLLED_KEY: str
_CROSSLINE_DETECTED_NAME: str
_CROSSLINE_DETECTED_EVENT_CODE: str
_MOTION_DETECTED_KEY: str
_MOTION_DETECTED_POLLED_KEY: str
_MOTION_DETECTED_NAME: str
_MOTION_DETECTED_EVENT_CODE: str
_ONLINE_KEY: str
BINARY_SENSORS: tuple[AmcrestSensorEntityDescription, ...]
BINARY_SENSOR_KEYS: Incomplete
_EXCLUSIVE_OPTIONS: Incomplete
_UPDATE_MSG: str

def check_binary_sensors(value: list[str]) -> list[str]: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class AmcrestBinarySensor(BinarySensorEntity):
    _signal_name: Incomplete
    _api: Incomplete
    _channel: Incomplete
    entity_description: AmcrestSensorEntityDescription
    _attr_name: Incomplete
    _attr_should_poll: Incomplete
    def __init__(self, name: str, device: AmcrestDevice, entity_description: AmcrestSensorEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_update(self) -> None: ...
    _attr_is_on: Incomplete
    async def _async_update_online(self) -> None: ...
    async def _async_update_others(self) -> None: ...
    _attr_unique_id: Incomplete
    async def _async_update_unique_id(self) -> None: ...
    @callback
    def async_on_demand_update_online(self) -> None: ...
    @callback
    def async_event_received(self, state: bool) -> None: ...
    async def async_added_to_hass(self) -> None: ...
