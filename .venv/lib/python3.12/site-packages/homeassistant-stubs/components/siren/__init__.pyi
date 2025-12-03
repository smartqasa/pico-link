from .const import ATTR_AVAILABLE_TONES as ATTR_AVAILABLE_TONES, ATTR_DURATION as ATTR_DURATION, ATTR_TONE as ATTR_TONE, ATTR_VOLUME_LEVEL as ATTR_VOLUME_LEVEL, DOMAIN as DOMAIN, SirenEntityFeature as SirenEntityFeature
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity, ToggleEntityDescription as ToggleEntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType, VolDictType as VolDictType
from homeassistant.util.hass_dict import HassKey as HassKey
from propcache import cached_property
from typing import Any, TypedDict, final

_LOGGER: Incomplete
DATA_COMPONENT: HassKey[EntityComponent[SirenEntity]]
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete
TURN_ON_SCHEMA: VolDictType

class SirenTurnOnServiceParameters(TypedDict, total=False):
    tone: int | str
    duration: int
    volume_level: float

def process_turn_on_params(siren: SirenEntity, params: SirenTurnOnServiceParameters) -> SirenTurnOnServiceParameters: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class SirenEntityDescription(ToggleEntityDescription, frozen_or_thawed=True):
    available_tones: list[int | str] | dict[int, str] | None = ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class SirenEntity(ToggleEntity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    _entity_component_unrecorded_attributes: Incomplete
    entity_description: SirenEntityDescription
    _attr_available_tones: list[int | str] | dict[int, str] | None
    _attr_supported_features: SirenEntityFeature
    @final
    @property
    def capability_attributes(self) -> dict[str, Any] | None: ...
    @cached_property
    def available_tones(self) -> list[int | str] | dict[int, str] | None: ...
    @cached_property
    def supported_features(self) -> SirenEntityFeature: ...
