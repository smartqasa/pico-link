from .coordinator import AnovaCoordinator as AnovaCoordinator
from .entity import AnovaDescriptionEntity as AnovaDescriptionEntity
from .models import AnovaConfigEntry as AnovaConfigEntry
from anova_wifi import APCUpdateSensor as APCUpdateSensor
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

@dataclass(frozen=True, kw_only=True)
class AnovaSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[APCUpdateSensor], StateType]

SENSOR_DESCRIPTIONS: list[AnovaSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: AnovaConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def setup_coordinator(coordinator: AnovaCoordinator, async_add_entities: AddEntitiesCallback) -> None: ...

class AnovaSensor(AnovaDescriptionEntity, SensorEntity):
    entity_description: AnovaSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...
