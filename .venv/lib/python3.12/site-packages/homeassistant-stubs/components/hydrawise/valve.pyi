from .const import DOMAIN as DOMAIN
from .coordinator import HydrawiseUpdateCoordinators as HydrawiseUpdateCoordinators
from .entity import HydrawiseEntity as HydrawiseEntity
from _typeshed import Incomplete
from homeassistant.components.valve import ValveDeviceClass as ValveDeviceClass, ValveEntity as ValveEntity, ValveEntityDescription as ValveEntityDescription, ValveEntityFeature as ValveEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydrawise.schema import Zone as Zone
from typing import Any

VALVE_TYPES: tuple[ValveEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HydrawiseValve(HydrawiseEntity, ValveEntity):
    _attr_name: Incomplete
    _attr_reports_position: bool
    _attr_supported_features: Incomplete
    zone: Zone
    async def async_open_valve(self, **kwargs: Any) -> None: ...
    async def async_close_valve(self) -> None: ...
    _attr_is_closed: Incomplete
    def _update_attrs(self) -> None: ...
