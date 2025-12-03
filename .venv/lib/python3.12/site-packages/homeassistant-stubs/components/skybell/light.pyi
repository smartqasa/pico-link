from .const import DOMAIN as DOMAIN
from .entity import SkybellEntity as SkybellEntity
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityDescription as LightEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SkybellLight(SkybellEntity, LightEntity):
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_name: Incomplete
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def brightness(self) -> int: ...
    @property
    def rgb_color(self) -> tuple[int, int, int] | None: ...
