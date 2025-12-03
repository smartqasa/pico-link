from .const import DOMAIN as DOMAIN, SENSOR_MOLD as SENSOR_MOLD, SENSOR_TEMPERATURE as SENSOR_TEMPERATURE
from .coordinator import NotionDataUpdateCoordinator as NotionDataUpdateCoordinator
from .entity import NotionEntity as NotionEntity, NotionEntityDescription as NotionEntityDescription
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class NotionSensorDescription(SensorEntityDescription, NotionEntityDescription): ...

SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NotionSensor(NotionEntity, SensorEntity):
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def native_value(self) -> str | None: ...
