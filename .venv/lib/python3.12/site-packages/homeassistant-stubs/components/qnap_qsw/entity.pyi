from .const import MANUFACTURER as MANUFACTURER
from .coordinator import QswDataCoordinator as QswDataCoordinator, QswFirmwareCoordinator as QswFirmwareCoordinator
from _typeshed import Incomplete
from aioqsw.const import QSD_LACP_PORTS, QSD_PORTS
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class QswEntityType(StrEnum):
    LACP_PORT = QSD_LACP_PORTS
    PORT = QSD_PORTS

class QswDataEntity(CoordinatorEntity[QswDataCoordinator]):
    type_id: Incomplete
    product: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: QswDataCoordinator, entry: ConfigEntry, type_id: int | None = None) -> None: ...
    def get_device_value(self, key: str, subkey: str, qsw_type: QswEntityType | None = None) -> Any: ...

@dataclass(frozen=True)
class QswEntityDescriptionMixin:
    subkey: str

@dataclass(frozen=True)
class QswEntityDescription(EntityDescription, QswEntityDescriptionMixin):
    attributes: dict[str, list[str]] | None = ...

class QswSensorEntity(QswDataEntity):
    entity_description: QswEntityDescription
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_extra_state_attributes: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...

class QswFirmwareEntity(CoordinatorEntity[QswFirmwareCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: QswFirmwareCoordinator, entry: ConfigEntry) -> None: ...
    def get_device_value(self, key: str, subkey: str) -> Any: ...
