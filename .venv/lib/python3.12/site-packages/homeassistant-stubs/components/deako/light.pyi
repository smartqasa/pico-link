from . import DeakoConfigEntry as DeakoConfigEntry
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydeako import Deako as Deako
from typing import Any

MODEL_SMART: str
MODEL_DIMMER: str

async def async_setup_entry(hass: HomeAssistant, config: DeakoConfigEntry, add_entities: AddEntitiesCallback) -> None: ...

class DeakoLightEntity(LightEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_is_on: bool
    _attr_available: bool
    client: Deako
    _attr_unique_id: Incomplete
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, client: Deako, uuid: str) -> None: ...
    def on_update(self) -> None: ...
    async def control_device(self, power: bool, dim: int | None = None) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_brightness: Incomplete
    def update(self) -> None: ...
