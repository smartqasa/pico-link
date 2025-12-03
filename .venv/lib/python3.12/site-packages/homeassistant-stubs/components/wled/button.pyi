from . import WLEDConfigEntry as WLEDConfigEntry
from .coordinator import WLEDDataUpdateCoordinator as WLEDDataUpdateCoordinator
from .entity import WLEDEntity as WLEDEntity
from .helpers import wled_exception_handler as wled_exception_handler
from _typeshed import Incomplete
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: WLEDConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WLEDRestartButton(WLEDEntity, ButtonEntity):
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator) -> None: ...
    @wled_exception_handler
    async def async_press(self) -> None: ...
