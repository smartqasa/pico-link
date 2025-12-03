from . import AbodeSystem as AbodeSystem
from .const import DOMAIN as DOMAIN
from .entity import AbodeDevice as AbodeDevice
from _typeshed import Incomplete
from homeassistant.components.cover import CoverEntity as CoverEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from jaraco.abode.devices.cover import Cover as Cover
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AbodeCover(AbodeDevice, CoverEntity):
    _device: Cover
    _attr_name: Incomplete
    @property
    def is_closed(self) -> bool: ...
    def close_cover(self, **kwargs: Any) -> None: ...
    def open_cover(self, **kwargs: Any) -> None: ...
