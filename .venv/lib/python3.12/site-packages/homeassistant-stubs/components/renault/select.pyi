from . import RenaultConfigEntry as RenaultConfigEntry
from .entity import RenaultDataEntity as RenaultDataEntity, RenaultDataEntityDescription as RenaultDataEntityDescription
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from renault_api.kamereon.models import KamereonVehicleBatteryStatusData

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RenaultSelectEntityDescription(SelectEntityDescription, RenaultDataEntityDescription):
    data_key: str

async def async_setup_entry(hass: HomeAssistant, config_entry: RenaultConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RenaultSelectEntity(RenaultDataEntity[KamereonVehicleBatteryStatusData], SelectEntity):
    entity_description: RenaultSelectEntityDescription
    @property
    def current_option(self) -> str | None: ...
    @property
    def data(self) -> StateType: ...
    async def async_select_option(self, option: str) -> None: ...

SENSOR_TYPES: tuple[RenaultSelectEntityDescription, ...]
