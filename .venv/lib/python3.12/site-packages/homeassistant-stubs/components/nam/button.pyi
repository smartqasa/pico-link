from . import NAMConfigEntry as NAMConfigEntry, NAMDataUpdateCoordinator as NAMDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

PARALLEL_UPDATES: int
_LOGGER: Incomplete
RESTART_BUTTON: ButtonEntityDescription

async def async_setup_entry(hass: HomeAssistant, entry: NAMConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NAMButton(CoordinatorEntity[NAMDataUpdateCoordinator], ButtonEntity):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: NAMDataUpdateCoordinator, description: ButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
