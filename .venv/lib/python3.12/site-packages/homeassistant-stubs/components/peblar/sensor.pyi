from .const import PEBLAR_CHARGE_LIMITER_TO_HOME_ASSISTANT as PEBLAR_CHARGE_LIMITER_TO_HOME_ASSISTANT, PEBLAR_CP_STATE_TO_HOME_ASSISTANT as PEBLAR_CP_STATE_TO_HOME_ASSISTANT
from .coordinator import PeblarConfigEntry as PeblarConfigEntry, PeblarData as PeblarData, PeblarDataUpdateCoordinator as PeblarDataUpdateCoordinator
from .entity import PeblarEntity as PeblarEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.dt import utcnow as utcnow
from peblar import PeblarUserConfiguration as PeblarUserConfiguration

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class PeblarSensorDescription(SensorEntityDescription):
    has_fn: Callable[[PeblarUserConfiguration], bool] = ...
    value_fn: Callable[[PeblarData], datetime | int | str | None]

DESCRIPTIONS: tuple[PeblarSensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PeblarConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PeblarSensorEntity(PeblarEntity[PeblarDataUpdateCoordinator], SensorEntity):
    entity_description: PeblarSensorDescription
    @property
    def native_value(self) -> datetime | int | str | None: ...
