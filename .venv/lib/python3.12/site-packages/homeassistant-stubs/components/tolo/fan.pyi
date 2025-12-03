from .const import DOMAIN as DOMAIN
from .coordinator import ToloSaunaUpdateCoordinator as ToloSaunaUpdateCoordinator
from .entity import ToloSaunaCoordinatorEntity as ToloSaunaCoordinatorEntity
from _typeshed import Incomplete
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ToloFan(ToloSaunaCoordinatorEntity, FanEntity):
    _attr_translation_key: str
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ToloSaunaUpdateCoordinator, entry: ConfigEntry) -> None: ...
    @property
    def is_on(self) -> bool: ...
    def turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
