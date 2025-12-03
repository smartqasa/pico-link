from . import AirzoneConfigEntry as AirzoneConfigEntry
from .coordinator import AirzoneUpdateCoordinator as AirzoneUpdateCoordinator
from .entity import AirzoneEntity as AirzoneEntity, AirzoneZoneEntity as AirzoneZoneEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

@dataclass(frozen=True, kw_only=True)
class AirzoneSwitchDescription(SwitchEntityDescription):
    api_param: str

ZONE_SWITCH_TYPES: Final[tuple[AirzoneSwitchDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: AirzoneConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirzoneBaseSwitch(AirzoneEntity, SwitchEntity):
    entity_description: AirzoneSwitchDescription
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...

class AirzoneZoneSwitch(AirzoneZoneEntity, AirzoneBaseSwitch):
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, description: AirzoneSwitchDescription, entry: ConfigEntry, system_zone_id: str, zone_data: dict[str, Any]) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
