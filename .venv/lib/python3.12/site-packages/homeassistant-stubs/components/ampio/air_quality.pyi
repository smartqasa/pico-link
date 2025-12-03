from .const import CONF_STATION_ID as CONF_STATION_ID, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from asmog import AmpioSmog
from homeassistant.components.air_quality import AirQualityEntity as AirQualityEntity
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util import Throttle as Throttle
from typing import Final

_LOGGER: Final[Incomplete]
PLATFORM_SCHEMA: Final[Incomplete]

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class AmpioSmogQuality(AirQualityEntity):
    _attr_attribution: str
    _ampio: Incomplete
    _station_id: Incomplete
    _name: Incomplete
    def __init__(self, api: AmpioSmogMapData, station_id: str, name: str | None) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def particulate_matter_2_5(self) -> str | None: ...
    @property
    def particulate_matter_10(self) -> str | None: ...
    async def async_update(self) -> None: ...

class AmpioSmogMapData:
    api: Incomplete
    def __init__(self, api: AmpioSmog) -> None: ...
    async def async_update(self) -> None: ...
