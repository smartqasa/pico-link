from . import NanoleafConfigEntry as NanoleafConfigEntry
from .coordinator import NanoleafCoordinator as NanoleafCoordinator
from .entity import NanoleafEntity as NanoleafEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: NanoleafConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NanoleafIdentifyButton(NanoleafEntity, ButtonEntity):
    _attr_entity_category: Incomplete
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: NanoleafCoordinator) -> None: ...
    async def async_press(self) -> None: ...
