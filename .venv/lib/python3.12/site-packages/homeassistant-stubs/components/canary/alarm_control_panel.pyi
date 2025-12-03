from .const import DATA_COORDINATOR as DATA_COORDINATOR, DOMAIN as DOMAIN
from .coordinator import CanaryDataUpdateCoordinator as CanaryDataUpdateCoordinator
from _typeshed import Incomplete
from canary.model import Location as Location
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity as AlarmControlPanelEntity, AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, AlarmControlPanelState as AlarmControlPanelState
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CanaryAlarm(CoordinatorEntity[CanaryDataUpdateCoordinator], AlarmControlPanelEntity):
    _attr_supported_features: Incomplete
    _attr_code_arm_required: bool
    _location_id: str
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: CanaryDataUpdateCoordinator, location: Location) -> None: ...
    @property
    def location(self) -> Location: ...
    @property
    def alarm_state(self) -> AlarmControlPanelState | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    def alarm_disarm(self, code: str | None = None) -> None: ...
    def alarm_arm_home(self, code: str | None = None) -> None: ...
    def alarm_arm_away(self, code: str | None = None) -> None: ...
    def alarm_arm_night(self, code: str | None = None) -> None: ...
