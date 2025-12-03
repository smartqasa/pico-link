from .const import BIDIRECTIONAL_MODEL_PREFIXES as BIDIRECTIONAL_MODEL_PREFIXES, CHARGER_DATA_KEY as CHARGER_DATA_KEY, CHARGER_ENERGY_PRICE_KEY as CHARGER_ENERGY_PRICE_KEY, CHARGER_MAX_AVAILABLE_POWER_KEY as CHARGER_MAX_AVAILABLE_POWER_KEY, CHARGER_MAX_CHARGING_CURRENT_KEY as CHARGER_MAX_CHARGING_CURRENT_KEY, CHARGER_MAX_ICP_CURRENT_KEY as CHARGER_MAX_ICP_CURRENT_KEY, CHARGER_PART_NUMBER_KEY as CHARGER_PART_NUMBER_KEY, CHARGER_SERIAL_NUMBER_KEY as CHARGER_SERIAL_NUMBER_KEY, DOMAIN as DOMAIN
from .coordinator import InvalidAuth as InvalidAuth, WallboxCoordinator as WallboxCoordinator
from .entity import WallboxEntity as WallboxEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

def min_charging_current_value(coordinator: WallboxCoordinator) -> float: ...

@dataclass(frozen=True, kw_only=True)
class WallboxNumberEntityDescription(NumberEntityDescription):
    max_value_fn: Callable[[WallboxCoordinator], float]
    min_value_fn: Callable[[WallboxCoordinator], float]
    set_value_fn: Callable[[WallboxCoordinator], Callable[[float], Awaitable[None]]]

NUMBER_TYPES: dict[str, WallboxNumberEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WallboxNumber(WallboxEntity, NumberEntity):
    entity_description: WallboxNumberEntityDescription
    _coordinator: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WallboxCoordinator, entry: ConfigEntry, description: WallboxNumberEntityDescription) -> None: ...
    @property
    def native_max_value(self) -> float: ...
    @property
    def native_min_value(self) -> float: ...
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
