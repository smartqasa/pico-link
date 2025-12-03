from . import HomeWizardConfigEntry as HomeWizardConfigEntry
from .coordinator import HWEnergyDeviceUpdateCoordinator as HWEnergyDeviceUpdateCoordinator
from .entity import HomeWizardEntity as HomeWizardEntity
from .helpers import homewizard_exception_handler as homewizard_exception_handler
from _typeshed import Incomplete
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: HomeWizardConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HomeWizardIdentifyButton(HomeWizardEntity, ButtonEntity):
    _attr_entity_category: Incomplete
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: HWEnergyDeviceUpdateCoordinator) -> None: ...
    @homewizard_exception_handler
    async def async_press(self) -> None: ...
