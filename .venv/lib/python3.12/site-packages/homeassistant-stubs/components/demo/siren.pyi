from _typeshed import Incomplete
from homeassistant.components.siren import SirenEntity as SirenEntity, SirenEntityFeature as SirenEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SUPPORT_FLAGS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DemoSiren(SirenEntity):
    _attr_name: Incomplete
    _attr_should_poll: bool
    _attr_supported_features: Incomplete
    _attr_is_on: Incomplete
    _attr_available_tones: Incomplete
    def __init__(self, name: str, available_tones: list[str | int] | None = None, support_volume_set: bool = False, support_duration: bool = False, is_on: bool = True) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
