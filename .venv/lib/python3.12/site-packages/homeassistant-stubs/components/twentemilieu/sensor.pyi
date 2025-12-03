from .const import DOMAIN as DOMAIN
from .coordinator import TwenteMilieuConfigEntry as TwenteMilieuConfigEntry
from .entity import TwenteMilieuEntity as TwenteMilieuEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import date
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import CONF_ID as CONF_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from twentemilieu import WasteType

@dataclass(frozen=True, kw_only=True)
class TwenteMilieuSensorDescription(SensorEntityDescription):
    waste_type: WasteType

SENSORS: tuple[TwenteMilieuSensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TwenteMilieuConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TwenteMilieuSensor(TwenteMilieuEntity, SensorEntity):
    entity_description: TwenteMilieuSensorDescription
    _attr_unique_id: Incomplete
    def __init__(self, entry: TwenteMilieuConfigEntry, description: TwenteMilieuSensorDescription) -> None: ...
    @property
    def native_value(self) -> date | None: ...
