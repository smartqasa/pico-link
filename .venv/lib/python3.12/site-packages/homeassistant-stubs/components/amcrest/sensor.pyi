from . import AmcrestDevice as AmcrestDevice
from .const import DATA_AMCREST as DATA_AMCREST, DEVICES as DEVICES, SENSOR_SCAN_INTERVAL_SECS as SENSOR_SCAN_INTERVAL_SECS, SERVICE_UPDATE as SERVICE_UPDATE
from .helpers import log_update_error as log_update_error, service_signal as service_signal
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_SENSORS as CONF_SENSORS, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
SENSOR_PTZ_PRESET: str
SENSOR_SDCARD: str
SENSOR_TYPES: tuple[SensorEntityDescription, ...]
SENSOR_KEYS: list[str]

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class AmcrestSensor(SensorEntity):
    entity_description: Incomplete
    _signal_name: Incomplete
    _api: Incomplete
    _channel: Incomplete
    _attr_name: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, name: str, device: AmcrestDevice, description: SensorEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    _attr_unique_id: Incomplete
    _attr_native_value: Incomplete
    async def async_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
