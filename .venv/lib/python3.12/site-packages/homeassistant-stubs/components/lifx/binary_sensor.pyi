from .const import DOMAIN as DOMAIN, HEV_CYCLE_STATE as HEV_CYCLE_STATE
from .coordinator import LIFXUpdateCoordinator as LIFXUpdateCoordinator
from .entity import LIFXEntity as LIFXEntity
from .util import lifx_features as lifx_features
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

HEV_CYCLE_STATE_SENSOR: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LIFXHevCycleBinarySensorEntity(LIFXEntity, BinarySensorEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LIFXUpdateCoordinator, description: BinarySensorEntityDescription) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
