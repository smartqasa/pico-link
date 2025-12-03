from . import StreamlabsCoordinator as StreamlabsCoordinator
from .const import DOMAIN as DOMAIN
from .entity import StreamlabsWaterEntity as StreamlabsWaterEntity
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class StreamlabsAwayMode(StreamlabsWaterEntity, BinarySensorEntity):
    _attr_translation_key: str
    def __init__(self, coordinator: StreamlabsCoordinator, location_id: str) -> None: ...
    @property
    def is_on(self) -> bool: ...
