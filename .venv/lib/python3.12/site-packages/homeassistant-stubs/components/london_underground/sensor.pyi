from .const import CONF_LINE as CONF_LINE, TUBE_LINES as TUBE_LINES
from .coordinator import LondonTubeCoordinator as LondonTubeCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGER: Incomplete
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class LondonTubeSensor(CoordinatorEntity[LondonTubeCoordinator], SensorEntity):
    _attr_attribution: str
    _attr_icon: str
    _name: Incomplete
    def __init__(self, coordinator: LondonTubeCoordinator, name: str) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def native_value(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
