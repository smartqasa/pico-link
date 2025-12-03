from .const import DOMAIN as DOMAIN, SERVICE_PHASES as SERVICE_PHASES, SERVICE_SETTINGS as SERVICE_SETTINGS, SERVICE_SMARTMETER as SERVICE_SMARTMETER, SERVICE_WATERMETER as SERVICE_WATERMETER
from .coordinator import P1MonitorDataUpdateCoordinator as P1MonitorDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CURRENCY_EURO as CURRENCY_EURO, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Literal

SENSORS_SMARTMETER: tuple[SensorEntityDescription, ...]
SENSORS_PHASES: tuple[SensorEntityDescription, ...]
SENSORS_SETTINGS: tuple[SensorEntityDescription, ...]
SENSORS_WATERMETER: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class P1MonitorSensorEntity(CoordinatorEntity[P1MonitorDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    _service_key: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, entry: ConfigEntry, description: SensorEntityDescription, name: str, service: Literal['smartmeter', 'watermeter', 'phases', 'settings']) -> None: ...
    @property
    def native_value(self) -> StateType: ...
