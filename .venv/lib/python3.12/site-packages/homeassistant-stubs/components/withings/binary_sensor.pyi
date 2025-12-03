from . import WithingsConfigEntry as WithingsConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import WithingsBedPresenceDataUpdateCoordinator as WithingsBedPresenceDataUpdateCoordinator
from .entity import WithingsEntity as WithingsEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: WithingsConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WithingsBinarySensor(WithingsEntity, BinarySensorEntity):
    _attr_translation_key: str
    _attr_device_class: Incomplete
    coordinator: WithingsBedPresenceDataUpdateCoordinator
    def __init__(self, coordinator: WithingsBedPresenceDataUpdateCoordinator) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
