from .const import DOMAIN as DOMAIN, ICON_EMPTY as ICON_EMPTY, ICON_OCCUPIED as ICON_OCCUPIED, IS_IN_BED as IS_IN_BED
from .coordinator import SleepIQData as SleepIQData, SleepIQDataUpdateCoordinator as SleepIQDataUpdateCoordinator
from .entity import SleepIQSleeperEntity as SleepIQSleeperEntity
from _typeshed import Incomplete
from asyncsleepiq import SleepIQBed as SleepIQBed, SleepIQSleeper as SleepIQSleeper
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IsInBedBinarySensor(SleepIQSleeperEntity[SleepIQDataUpdateCoordinator], BinarySensorEntity):
    _attr_device_class: Incomplete
    def __init__(self, coordinator: SleepIQDataUpdateCoordinator, bed: SleepIQBed, sleeper: SleepIQSleeper) -> None: ...
    _attr_is_on: Incomplete
    _attr_icon: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
