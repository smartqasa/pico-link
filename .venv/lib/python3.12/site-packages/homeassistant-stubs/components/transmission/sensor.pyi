from . import TransmissionConfigEntry as TransmissionConfigEntry
from .const import DOMAIN as DOMAIN, STATE_ATTR_TORRENT_INFO as STATE_ATTR_TORRENT_INFO, STATE_DOWNLOADING as STATE_DOWNLOADING, STATE_SEEDING as STATE_SEEDING, STATE_UP_DOWN as STATE_UP_DOWN, SUPPORTED_ORDER_MODES as SUPPORTED_ORDER_MODES
from .coordinator import TransmissionDataUpdateCoordinator as TransmissionDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import STATE_IDLE as STATE_IDLE, UnitOfDataRate as UnitOfDataRate
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from transmission_rpc.torrent import Torrent as Torrent
from typing import Any

MODES: dict[str, list[str] | None]

@dataclass(frozen=True, kw_only=True)
class TransmissionSensorEntityDescription(SensorEntityDescription):
    val_func: Callable[[TransmissionDataUpdateCoordinator], StateType]
    extra_state_attr_func: Callable[[Any], dict[str, str]] | None = ...

SENSOR_TYPES: tuple[TransmissionSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: TransmissionConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TransmissionSensor(CoordinatorEntity[TransmissionDataUpdateCoordinator], SensorEntity):
    entity_description: TransmissionSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: TransmissionDataUpdateCoordinator, entity_description: TransmissionSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...

def get_state(upload: int, download: int) -> str: ...
def _filter_torrents(torrents: list[Torrent], statuses: list[str] | None = None) -> list[Torrent]: ...
def _torrents_info_attr(coordinator: TransmissionDataUpdateCoordinator, key: str) -> dict[str, Any]: ...
