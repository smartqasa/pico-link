import abc
from . import FroniusSolarNet as FroniusSolarNet
from .const import DOMAIN as DOMAIN, FroniusDeviceInfo as FroniusDeviceInfo, SOLAR_NET_ID_POWER_FLOW as SOLAR_NET_ID_POWER_FLOW, SOLAR_NET_ID_SYSTEM as SOLAR_NET_ID_SYSTEM, SolarNetId as SolarNetId
from .sensor import FroniusSensorEntityDescription as FroniusSensorEntityDescription, INVERTER_ENTITY_DESCRIPTIONS as INVERTER_ENTITY_DESCRIPTIONS, LOGGER_ENTITY_DESCRIPTIONS as LOGGER_ENTITY_DESCRIPTIONS, METER_ENTITY_DESCRIPTIONS as METER_ENTITY_DESCRIPTIONS, OHMPILOT_ENTITY_DESCRIPTIONS as OHMPILOT_ENTITY_DESCRIPTIONS, POWER_FLOW_ENTITY_DESCRIPTIONS as POWER_FLOW_ENTITY_DESCRIPTIONS, STORAGE_ENTITY_DESCRIPTIONS as STORAGE_ENTITY_DESCRIPTIONS, _FroniusSensorEntity as _FroniusSensorEntity
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from datetime import timedelta
from homeassistant.core import callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

class FroniusCoordinatorBase(ABC, DataUpdateCoordinator[dict[SolarNetId, dict[str, Any]]], metaclass=abc.ABCMeta):
    default_interval: timedelta
    error_interval: timedelta
    valid_descriptions: list[FroniusSensorEntityDescription]
    MAX_FAILED_UPDATES: int
    _failed_update_count: int
    solar_net: Incomplete
    unregistered_descriptors: dict[SolarNetId, list[FroniusSensorEntityDescription]]
    def __init__(self, *args: Any, solar_net: FroniusSolarNet, **kwargs: Any) -> None: ...
    @abstractmethod
    async def _update_method(self) -> dict[SolarNetId, Any]: ...
    update_interval: Incomplete
    async def _async_update_data(self) -> dict[SolarNetId, Any]: ...
    @callback
    def add_entities_for_seen_keys[_FroniusEntityT: _FroniusSensorEntity](self, async_add_entities: AddEntitiesCallback, entity_constructor: type[_FroniusEntityT]) -> None: ...

class FroniusInverterUpdateCoordinator(FroniusCoordinatorBase):
    default_interval: Incomplete
    error_interval: Incomplete
    valid_descriptions = INVERTER_ENTITY_DESCRIPTIONS
    SILENT_RETRIES: int
    inverter_info: Incomplete
    def __init__(self, *args: Any, inverter_info: FroniusDeviceInfo, **kwargs: Any) -> None: ...
    async def _update_method(self) -> dict[SolarNetId, Any]: ...

class FroniusLoggerUpdateCoordinator(FroniusCoordinatorBase):
    default_interval: Incomplete
    error_interval: Incomplete
    valid_descriptions = LOGGER_ENTITY_DESCRIPTIONS
    async def _update_method(self) -> dict[SolarNetId, Any]: ...

class FroniusMeterUpdateCoordinator(FroniusCoordinatorBase):
    default_interval: Incomplete
    error_interval: Incomplete
    valid_descriptions = METER_ENTITY_DESCRIPTIONS
    async def _update_method(self) -> dict[SolarNetId, Any]: ...

class FroniusOhmpilotUpdateCoordinator(FroniusCoordinatorBase):
    default_interval: Incomplete
    error_interval: Incomplete
    valid_descriptions = OHMPILOT_ENTITY_DESCRIPTIONS
    async def _update_method(self) -> dict[SolarNetId, Any]: ...

class FroniusPowerFlowUpdateCoordinator(FroniusCoordinatorBase):
    default_interval: Incomplete
    error_interval: Incomplete
    valid_descriptions = POWER_FLOW_ENTITY_DESCRIPTIONS
    async def _update_method(self) -> dict[SolarNetId, Any]: ...

class FroniusStorageUpdateCoordinator(FroniusCoordinatorBase):
    default_interval: Incomplete
    error_interval: Incomplete
    valid_descriptions = STORAGE_ENTITY_DESCRIPTIONS
    async def _update_method(self) -> dict[SolarNetId, Any]: ...
