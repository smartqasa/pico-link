from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey
from propcache import cached_property
from typing import Any, final

_LOGGER: Incomplete
DOMAIN: str
DATA_COMPONENT: HassKey[EntityComponent[GeolocationEvent]]
ENTITY_ID_FORMAT: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete
ATTR_DISTANCE: str
ATTR_SOURCE: str

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class GeolocationEvent(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    _attr_source: str
    _attr_distance: float | None
    _attr_latitude: float | None
    _attr_longitude: float | None
    @final
    @property
    def state(self) -> float | None: ...
    @cached_property
    def source(self) -> str: ...
    @cached_property
    def distance(self) -> float | None: ...
    @cached_property
    def latitude(self) -> float | None: ...
    @cached_property
    def longitude(self) -> float | None: ...
    @final
    @property
    def state_attributes(self) -> dict[str, Any]: ...
