from . import ElkM1ConfigEntry as ElkM1ConfigEntry
from .entity import ElkEntity as ElkEntity, create_elk_entities as create_elk_entities
from .models import ELKM1Data as ELKM1Data
from _typeshed import Incomplete
from elkm1_lib.elements import Element as Element
from elkm1_lib.elk import Elk as Elk
from elkm1_lib.lights import Light as Light
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ElkM1ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElkLight(ElkEntity, LightEntity):
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _element: Light
    _brightness: Incomplete
    def __init__(self, element: Element, elk: Elk, elk_data: ELKM1Data) -> None: ...
    @property
    def brightness(self) -> int: ...
    @property
    def is_on(self) -> bool: ...
    def _element_changed(self, element: Element, changeset: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
