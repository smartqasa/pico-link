from . import WizConfigEntry as WizConfigEntry
from .const import DOMAIN as DOMAIN, SIGNAL_WIZ_PIR as SIGNAL_WIZ_PIR
from .entity import WizEntity as WizEntity
from .models import WizData as WizData
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

OCCUPANCY_UNIQUE_ID: str

async def async_setup_entry(hass: HomeAssistant, entry: WizConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WizOccupancyEntity(WizEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, wiz_data: WizData, name: str) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
