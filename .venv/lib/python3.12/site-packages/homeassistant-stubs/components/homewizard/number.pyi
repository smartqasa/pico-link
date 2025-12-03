from . import HomeWizardConfigEntry as HomeWizardConfigEntry
from .coordinator import HWEnergyDeviceUpdateCoordinator as HWEnergyDeviceUpdateCoordinator
from .entity import HomeWizardEntity as HomeWizardEntity
from .helpers import homewizard_exception_handler as homewizard_exception_handler
from _typeshed import Incomplete
from homeassistant.components.number import NumberEntity as NumberEntity
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.color import brightness_to_value as brightness_to_value, value_to_brightness as value_to_brightness

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: HomeWizardConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HWEnergyNumberEntity(HomeWizardEntity, NumberEntity):
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: HWEnergyDeviceUpdateCoordinator) -> None: ...
    @homewizard_exception_handler
    async def async_set_native_value(self, value: float) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> float | None: ...
