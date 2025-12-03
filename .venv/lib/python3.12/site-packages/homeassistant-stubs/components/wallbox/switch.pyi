from .const import CHARGER_DATA_KEY as CHARGER_DATA_KEY, CHARGER_PAUSE_RESUME_KEY as CHARGER_PAUSE_RESUME_KEY, CHARGER_SERIAL_NUMBER_KEY as CHARGER_SERIAL_NUMBER_KEY, CHARGER_STATUS_DESCRIPTION_KEY as CHARGER_STATUS_DESCRIPTION_KEY, ChargerStatus as ChargerStatus, DOMAIN as DOMAIN
from .coordinator import WallboxCoordinator as WallboxCoordinator
from .entity import WallboxEntity as WallboxEntity
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SWITCH_TYPES: dict[str, SwitchEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WallboxSwitch(WallboxEntity, SwitchEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WallboxCoordinator, description: SwitchEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
