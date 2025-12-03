from . import OverkizDataConfigEntry as OverkizDataConfigEntry
from .entity import OverkizEntity as OverkizEntity
from _typeshed import Incomplete
from homeassistant.components.siren import ATTR_DURATION as ATTR_DURATION, SirenEntity as SirenEntity, SirenEntityFeature as SirenEntityFeature
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: OverkizDataConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OverkizSiren(OverkizEntity, SirenEntity):
    _attr_supported_features: Incomplete
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
