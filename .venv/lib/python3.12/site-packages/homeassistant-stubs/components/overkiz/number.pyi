from . import OverkizDataConfigEntry as OverkizDataConfigEntry
from .const import IGNORED_OVERKIZ_DEVICES as IGNORED_OVERKIZ_DEVICES
from .coordinator import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator
from .entity import OverkizDescriptiveEntity as OverkizDescriptiveEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

BOOST_MODE_DURATION_DELAY: int
OPERATING_MODE_DELAY: int

@dataclass(frozen=True, kw_only=True)
class OverkizNumberDescription(NumberEntityDescription):
    command: str
    min_value_state_name: str | None = ...
    max_value_state_name: str | None = ...
    inverted: bool = ...
    set_native_value: Callable[[float, Callable[..., Awaitable[None]]], Awaitable[None]] | None = ...

async def _async_set_native_value_boost_mode_duration(value: float, execute_command: Callable[..., Awaitable[None]]) -> None: ...

NUMBER_DESCRIPTIONS: list[OverkizNumberDescription]
SUPPORTED_STATES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: OverkizDataConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OverkizNumber(OverkizDescriptiveEntity, NumberEntity):
    entity_description: OverkizNumberDescription
    _attr_native_min_value: Incomplete
    _attr_native_max_value: Incomplete
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator, description: OverkizNumberDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
