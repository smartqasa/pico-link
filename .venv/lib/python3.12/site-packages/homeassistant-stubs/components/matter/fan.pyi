from .entity import MatterEntity as MatterEntity
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from homeassistant.components.fan import DIRECTION_FORWARD as DIRECTION_FORWARD, DIRECTION_REVERSE as DIRECTION_REVERSE, FanEntity as FanEntity, FanEntityDescription as FanEntityDescription, FanEntityFeature as FanEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

FanControlFeature: Incomplete
WindBitmap: Incomplete
FanModeSequenceEnum: Incomplete
PRESET_LOW: str
PRESET_MEDIUM: str
PRESET_HIGH: str
PRESET_AUTO: str
FAN_MODE_MAP: Incomplete
FAN_MODE_MAP_REVERSE: Incomplete
PRESET_NATURAL_WIND: str
PRESET_SLEEP_WIND: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MatterFan(MatterEntity, FanEntity):
    _last_known_preset_mode: str | None
    _last_known_percentage: int
    _feature_map: int | None
    _platform_translation_key: str
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_oscillate(self, oscillating: bool) -> None: ...
    async def async_set_direction(self, direction: str) -> None: ...
    async def _set_wind_mode(self, wind_mode: str | None) -> None: ...
    _attr_preset_mode: Incomplete
    _attr_percentage: int
    _attr_current_direction: Incomplete
    _attr_oscillating: Incomplete
    @callback
    def _update_from_device(self) -> None: ...
    _attr_supported_features: Incomplete
    _attr_speed_count: Incomplete
    _attr_preset_modes: Incomplete
    @callback
    def _calculate_features(self) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
