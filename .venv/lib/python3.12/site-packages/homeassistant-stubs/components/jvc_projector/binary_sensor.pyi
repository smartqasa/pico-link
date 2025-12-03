from . import JVCConfigEntry as JVCConfigEntry, JvcProjectorDataUpdateCoordinator as JvcProjectorDataUpdateCoordinator
from .entity import JvcProjectorEntity as JvcProjectorEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

ON_STATUS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: JVCConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class JvcBinarySensor(JvcProjectorEntity, BinarySensorEntity):
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: JvcProjectorDataUpdateCoordinator) -> None: ...
    @property
    def is_on(self) -> bool: ...
