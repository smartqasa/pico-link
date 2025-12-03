from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.scene import Scene as Scene
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pylitejet import LiteJet as LiteJet
from typing import Any

_LOGGER: Incomplete
ATTR_NUMBER: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LiteJetScene(Scene):
    _attr_has_entity_name: bool
    _attr_entity_registry_enabled_default: bool
    _lj: Incomplete
    _index: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, entry_id: str, system: LiteJet, i: int, name: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    _attr_available: Incomplete
    def _on_connected_changed(self, connected: bool, reason: str) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    async def async_activate(self, **kwargs: Any) -> None: ...
