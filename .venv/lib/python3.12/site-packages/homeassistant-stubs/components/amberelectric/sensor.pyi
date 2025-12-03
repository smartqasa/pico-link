from . import AmberConfigEntry as AmberConfigEntry
from .const import ATTRIBUTION as ATTRIBUTION
from .coordinator import AmberUpdateCoordinator as AmberUpdateCoordinator, normalize_descriptor as normalize_descriptor
from _typeshed import Incomplete
from amberelectric.models.current_interval import CurrentInterval as CurrentInterval
from amberelectric.models.forecast_interval import ForecastInterval as ForecastInterval
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CURRENCY_DOLLAR as CURRENCY_DOLLAR, PERCENTAGE as PERCENTAGE, UnitOfEnergy as UnitOfEnergy
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

UNIT: Incomplete

def format_cents_to_dollars(cents: float) -> float: ...
def friendly_channel_type(channel_type: str) -> str: ...

class AmberSensor(CoordinatorEntity[AmberUpdateCoordinator], SensorEntity):
    _attr_attribution = ATTRIBUTION
    site_id: Incomplete
    entity_description: Incomplete
    channel_type: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AmberUpdateCoordinator, description: SensorEntityDescription, channel_type: str) -> None: ...

class AmberPriceSensor(AmberSensor):
    @property
    def native_value(self) -> float | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...

class AmberForecastSensor(AmberSensor):
    @property
    def native_value(self) -> float | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...

class AmberPriceDescriptorSensor(AmberSensor):
    @property
    def native_value(self) -> str | None: ...

class AmberGridSensor(CoordinatorEntity[AmberUpdateCoordinator], SensorEntity):
    _attr_attribution = ATTRIBUTION
    site_id: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AmberUpdateCoordinator, description: SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> str | None: ...

async def async_setup_entry(hass: HomeAssistant, entry: AmberConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
