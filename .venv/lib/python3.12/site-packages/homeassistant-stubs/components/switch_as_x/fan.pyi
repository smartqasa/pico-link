from .entity import BaseToggleEntity as BaseToggleEntity
from _typeshed import Incomplete
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FanSwitch(BaseToggleEntity, FanEntity):
    _attr_supported_features: Incomplete
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
