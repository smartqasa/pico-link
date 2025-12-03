from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import singleton as singleton, storage as storage
from typing import Literal, TypedDict

STORAGE_VERSION: int
STORAGE_KEY = DOMAIN

async def async_get_manager(hass: HomeAssistant) -> EnergyManager: ...

class FlowFromGridSourceType(TypedDict):
    stat_energy_from: str
    stat_cost: str | None
    entity_energy_price: str | None
    number_energy_price: float | None

class FlowToGridSourceType(TypedDict):
    stat_energy_to: str
    stat_compensation: str | None
    entity_energy_price: str | None
    number_energy_price: float | None

class GridSourceType(TypedDict):
    type: Literal['grid']
    flow_from: list[FlowFromGridSourceType]
    flow_to: list[FlowToGridSourceType]
    cost_adjustment_day: float

class SolarSourceType(TypedDict):
    type: Literal['solar']
    stat_energy_from: str
    config_entry_solar_forecast: list[str] | None

class BatterySourceType(TypedDict):
    type: Literal['battery']
    stat_energy_from: str
    stat_energy_to: str

class GasSourceType(TypedDict):
    type: Literal['gas']
    stat_energy_from: str
    stat_cost: str | None
    entity_energy_price: str | None
    number_energy_price: float | None

class WaterSourceType(TypedDict):
    type: Literal['water']
    stat_energy_from: str
    stat_cost: str | None
    entity_energy_price: str | None
    number_energy_price: float | None
type SourceType = GridSourceType | SolarSourceType | BatterySourceType | GasSourceType | WaterSourceType

class DeviceConsumption(TypedDict):
    stat_consumption: str
    name: str | None

class EnergyPreferences(TypedDict):
    energy_sources: list[SourceType]
    device_consumption: list[DeviceConsumption]

class EnergyPreferencesUpdate(EnergyPreferences, total=False): ...

def _flow_from_ensure_single_price(val: FlowFromGridSourceType) -> FlowFromGridSourceType: ...

FLOW_FROM_GRID_SOURCE_SCHEMA: Incomplete
FLOW_TO_GRID_SOURCE_SCHEMA: Incomplete

def _generate_unique_value_validator(key: str) -> Callable[[list[dict]], list[dict]]: ...

GRID_SOURCE_SCHEMA: Incomplete
SOLAR_SOURCE_SCHEMA: Incomplete
BATTERY_SOURCE_SCHEMA: Incomplete
GAS_SOURCE_SCHEMA: Incomplete
WATER_SOURCE_SCHEMA: Incomplete

def check_type_limits(value: list[SourceType]) -> list[SourceType]: ...

ENERGY_SOURCE_SCHEMA: Incomplete
DEVICE_CONSUMPTION_SCHEMA: Incomplete

class EnergyManager:
    _hass: Incomplete
    _store: Incomplete
    data: EnergyPreferences | None
    _update_listeners: list[Callable[[], Awaitable]]
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_initialize(self) -> None: ...
    @staticmethod
    def default_preferences() -> EnergyPreferences: ...
    async def async_update(self, update: EnergyPreferencesUpdate) -> None: ...
    @callback
    def async_listen_updates(self, update_listener: Callable[[], Awaitable]) -> None: ...
