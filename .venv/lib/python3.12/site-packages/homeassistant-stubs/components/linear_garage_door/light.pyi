from .const import DOMAIN as DOMAIN
from .coordinator import LinearUpdateCoordinator as LinearUpdateCoordinator
from .entity import LinearEntity as LinearEntity
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from linear_garage_door import Linear as Linear
from typing import Any

SUPPORTED_SUBDEVICES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LinearLightEntity(LinearEntity, LightEntity):
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_translation_key: str
    @property
    def is_on(self) -> bool: ...
    @property
    def brightness(self) -> int | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
