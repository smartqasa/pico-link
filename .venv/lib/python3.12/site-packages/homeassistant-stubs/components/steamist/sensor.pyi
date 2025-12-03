from .const import DOMAIN as DOMAIN
from .coordinator import SteamistDataUpdateCoordinator as SteamistDataUpdateCoordinator
from .entity import SteamistEntity as SteamistEntity
from _typeshed import Incomplete
from aiosteamist import SteamistStatus as SteamistStatus
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_KEY_MINUTES_REMAIN: str
_KEY_TEMP: str
UNIT_MAPPINGS: Incomplete

@dataclass(frozen=True, kw_only=True)
class SteamistSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[SteamistStatus], int | None]

SENSORS: tuple[SteamistSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SteamistSensorEntity(SteamistEntity, SensorEntity):
    entity_description: SteamistSensorEntityDescription
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, coordinator: SteamistDataUpdateCoordinator, entry: ConfigEntry, description: SteamistSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> int | None: ...
