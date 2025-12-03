from . import AmberConfigEntry as AmberConfigEntry
from .const import ATTRIBUTION as ATTRIBUTION
from .coordinator import AmberUpdateCoordinator as AmberUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

PRICE_SPIKE_ICONS: Incomplete

class AmberPriceGridSensor(CoordinatorEntity[AmberUpdateCoordinator], BinarySensorEntity):
    _attr_attribution = ATTRIBUTION
    site_id: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AmberUpdateCoordinator, description: BinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...

class AmberPriceSpikeBinarySensor(AmberPriceGridSensor):
    @property
    def icon(self) -> str: ...
    @property
    def is_on(self) -> bool | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...

class AmberDemandWindowBinarySensor(AmberPriceGridSensor):
    @property
    def is_on(self) -> bool | None: ...

async def async_setup_entry(hass: HomeAssistant, entry: AmberConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
