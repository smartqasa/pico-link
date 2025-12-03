from . import CO2SignalConfigEntry as CO2SignalConfigEntry
from .const import ATTRIBUTION as ATTRIBUTION, DOMAIN as DOMAIN
from .coordinator import CO2SignalCoordinator as CO2SignalCoordinator
from _typeshed import Incomplete
from aioelectricitymaps.models import CarbonIntensityResponse as CarbonIntensityResponse
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

@dataclass(frozen=True, kw_only=True)
class CO2SensorEntityDescription(SensorEntityDescription):
    unique_id: str | None = ...
    unit_of_measurement_fn: Callable[[CarbonIntensityResponse], str | None] | None = ...
    value_fn: Callable[[CarbonIntensityResponse], float | None]

SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: CO2SignalConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CO2Sensor(CoordinatorEntity[CO2SignalCoordinator], SensorEntity):
    entity_description: CO2SensorEntityDescription
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    _attr_state_class: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: CO2SignalCoordinator, description: CO2SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
