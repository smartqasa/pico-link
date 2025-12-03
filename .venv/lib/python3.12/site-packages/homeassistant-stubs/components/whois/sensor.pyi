from .const import ATTR_EXPIRES as ATTR_EXPIRES, ATTR_NAME_SERVERS as ATTR_NAME_SERVERS, ATTR_REGISTRAR as ATTR_REGISTRAR, ATTR_UPDATED as ATTR_UPDATED, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN, EntityCategory as EntityCategory, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from whois import Domain

@dataclass(frozen=True, kw_only=True)
class WhoisSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Domain], datetime | int | str | None]

def _days_until_expiration(domain: Domain) -> int | None: ...
def _ensure_timezone(timestamp: datetime | None) -> datetime | None: ...

SENSORS: tuple[WhoisSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WhoisSensorEntity(CoordinatorEntity[DataUpdateCoordinator[Domain | None]], SensorEntity):
    entity_description: WhoisSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _domain: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[Domain | None], description: WhoisSensorEntityDescription, domain: str) -> None: ...
    @property
    def native_value(self) -> datetime | int | str | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, int | float | None] | None: ...
