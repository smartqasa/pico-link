from _typeshed import Incomplete
from homeassistant.components.geo_location import GeolocationEvent as GeolocationEvent
from homeassistant.const import UnitOfLength as UnitOfLength
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import track_time_interval as track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

_LOGGER: Incomplete
AVG_KM_PER_DEGREE: float
DEFAULT_UPDATE_INTERVAL: Incomplete
MAX_RADIUS_IN_KM: int
NUMBER_OF_DEMO_DEVICES: int
EVENT_NAMES: Incomplete
SOURCE: str

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class DemoManager:
    _hass: Incomplete
    _add_entities: Incomplete
    _managed_devices: list[DemoGeolocationEvent]
    def __init__(self, hass: HomeAssistant, add_entities: AddEntitiesCallback) -> None: ...
    def _generate_random_event(self) -> DemoGeolocationEvent: ...
    def _init_regular_updates(self) -> None: ...
    def _update(self, count: int = 1) -> None: ...

class DemoGeolocationEvent(GeolocationEvent):
    _attr_should_poll: bool
    _attr_name: Incomplete
    _distance: Incomplete
    _latitude: Incomplete
    _longitude: Incomplete
    _unit_of_measurement: Incomplete
    def __init__(self, name: str, distance: float, latitude: float, longitude: float, unit_of_measurement: str) -> None: ...
    @property
    def source(self) -> str: ...
    @property
    def distance(self) -> float | None: ...
    @property
    def latitude(self) -> float | None: ...
    @property
    def longitude(self) -> float | None: ...
    @property
    def unit_of_measurement(self) -> str: ...
