from .const import API as API, COORDINATOR as COORDINATOR, DOMAIN as DOMAIN
from .coordinator import Tami4EdgeCoordinator as Tami4EdgeCoordinator
from .entity import Tami4EdgeBaseEntity as Tami4EdgeBaseEntity
from Tami4EdgeAPI import Tami4EdgeAPI as Tami4EdgeAPI
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

_LOGGER: Incomplete
ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class Tami4EdgeSensorEntity(Tami4EdgeBaseEntity, CoordinatorEntity[Tami4EdgeCoordinator], SensorEntity):
    def __init__(self, coordinator: Tami4EdgeCoordinator, api: Tami4EdgeAPI, entity_description: SensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    def _update_attr(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
