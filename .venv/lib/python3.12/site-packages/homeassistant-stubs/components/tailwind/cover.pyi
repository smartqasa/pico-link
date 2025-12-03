from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import TailwindConfigEntry as TailwindConfigEntry
from .entity import TailwindDoorEntity as TailwindDoorEntity
from _typeshed import Incomplete
from homeassistant.components.cover import CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: TailwindConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TailwindDoorCoverEntity(TailwindDoorEntity, CoverEntity):
    _attr_device_class: Incomplete
    _attr_is_closing: bool
    _attr_is_opening: bool
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    @property
    def is_closed(self) -> bool: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
