from .entity import DeconzDevice as DeconzDevice
from .hub import DeconzHub as DeconzHub
from _typeshed import Incomplete
from homeassistant.components.siren import ATTR_DURATION as ATTR_DURATION, DOMAIN as SIREN_DOMAIN, SirenEntity as SirenEntity, SirenEntityFeature as SirenEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydeconz.models.event import EventType as EventType
from pydeconz.models.light.siren import Siren
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzSiren(DeconzDevice[Siren], SirenEntity):
    TYPE = SIREN_DOMAIN
    _attr_supported_features: Incomplete
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
