from .const import DOMAIN as DOMAIN
from .coordinator import EvilGeniusUpdateCoordinator as EvilGeniusUpdateCoordinator
from .entity import EvilGeniusEntity as EvilGeniusEntity
from .util import update_when_done as update_when_done
from _typeshed import Incomplete
from homeassistant.components import light as light
from homeassistant.components.light import ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

HA_NO_EFFECT: str
FIB_NO_EFFECT: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EvilGeniusLight(EvilGeniusEntity, LightEntity):
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    _attr_unique_id: Incomplete
    _attr_effect_list: Incomplete
    def __init__(self, coordinator: EvilGeniusUpdateCoordinator) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def brightness(self) -> int: ...
    @property
    def rgb_color(self) -> tuple[int, int, int]: ...
    @property
    def effect(self) -> str: ...
    @update_when_done
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @update_when_done
    async def async_turn_off(self, **kwargs: Any) -> None: ...
