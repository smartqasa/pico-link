from . import EheimDigitalConfigEntry as EheimDigitalConfigEntry
from .const import EFFECT_DAYCL_MODE as EFFECT_DAYCL_MODE, EFFECT_TO_LIGHT_MODE as EFFECT_TO_LIGHT_MODE
from .coordinator import EheimDigitalUpdateCoordinator as EheimDigitalUpdateCoordinator
from .entity import EheimDigitalEntity as EheimDigitalEntity
from _typeshed import Incomplete
from eheimdigital.classic_led_ctrl import EheimDigitalClassicLEDControl
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_EFFECT as ATTR_EFFECT, ColorMode as ColorMode, EFFECT_OFF as EFFECT_OFF, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.color import brightness_to_value as brightness_to_value, value_to_brightness as value_to_brightness
from typing import Any

BRIGHTNESS_SCALE: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: EheimDigitalConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EheimDigitalClassicLEDControlLight(EheimDigitalEntity[EheimDigitalClassicLEDControl], LightEntity):
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    _attr_effect_list: Incomplete
    _attr_supported_features: Incomplete
    _attr_translation_key: str
    _channel: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: EheimDigitalUpdateCoordinator, device: EheimDigitalClassicLEDControl, channel: int) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    _attr_brightness: Incomplete
    _attr_effect: Incomplete
    def _async_update_attrs(self) -> None: ...
