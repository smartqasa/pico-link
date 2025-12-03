from . import DevoloHomeNetworkConfigEntry as DevoloHomeNetworkConfigEntry
from .const import CONNECTED_PLC_DEVICES as CONNECTED_PLC_DEVICES, CONNECTED_WIFI_CLIENTS as CONNECTED_WIFI_CLIENTS, LAST_RESTART as LAST_RESTART, NEIGHBORING_WIFI_NETWORKS as NEIGHBORING_WIFI_NETWORKS, PLC_RX_RATE as PLC_RX_RATE, PLC_TX_RATE as PLC_TX_RATE
from .coordinator import DevoloDataUpdateCoordinator as DevoloDataUpdateCoordinator
from .entity import DevoloCoordinatorEntity as DevoloCoordinatorEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from devolo_plc_api.device_api import ConnectedStationInfo, NeighborAPInfo
from devolo_plc_api.plcnet_api import DataRate, LogicalNetwork
from enum import StrEnum
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfDataRate as UnitOfDataRate
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.dt import utcnow as utcnow
from typing import Any

PARALLEL_UPDATES: int

def _last_restart(runtime: int) -> datetime: ...
type _CoordinatorDataType = LogicalNetwork | DataRate | list[ConnectedStationInfo] | list[NeighborAPInfo] | int
type _SensorDataType = int | float | datetime

class DataRateDirection(StrEnum):
    RX = 'rx_rate'
    TX = 'tx_rate'

@dataclass(frozen=True, kw_only=True)
class DevoloSensorEntityDescription[_CoordinatorDataT: _CoordinatorDataType, _SensorDataT: _SensorDataType](SensorEntityDescription):
    value_func: Callable[[_CoordinatorDataT], _SensorDataT]

SENSOR_TYPES: dict[str, DevoloSensorEntityDescription[Any, Any]]

async def async_setup_entry(hass: HomeAssistant, entry: DevoloHomeNetworkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BaseDevoloSensorEntity[_CoordinatorDataT: _CoordinatorDataType, _ValueDataT: _CoordinatorDataType, _SensorDataT: _SensorDataType](DevoloCoordinatorEntity[_CoordinatorDataT], SensorEntity):
    entity_description: Incomplete
    def __init__(self, entry: DevoloHomeNetworkConfigEntry, coordinator: DevoloDataUpdateCoordinator[_CoordinatorDataT], description: DevoloSensorEntityDescription[_ValueDataT, _SensorDataT]) -> None: ...

class DevoloSensorEntity[_CoordinatorDataT: _CoordinatorDataType, _ValueDataT: _CoordinatorDataType, _SensorDataT: _SensorDataType](BaseDevoloSensorEntity[_CoordinatorDataT, _ValueDataT, _SensorDataT]):
    entity_description: DevoloSensorEntityDescription[_CoordinatorDataT, _SensorDataT]
    @property
    def native_value(self) -> int | float | datetime: ...

class DevoloPlcDataRateSensorEntity(BaseDevoloSensorEntity[LogicalNetwork, DataRate, float]):
    entity_description: DevoloSensorEntityDescription[DataRate, float]
    _peer: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    def __init__(self, entry: DevoloHomeNetworkConfigEntry, coordinator: DevoloDataUpdateCoordinator[LogicalNetwork], description: DevoloSensorEntityDescription[DataRate, float], peer: str) -> None: ...
    @property
    def native_value(self) -> float: ...
