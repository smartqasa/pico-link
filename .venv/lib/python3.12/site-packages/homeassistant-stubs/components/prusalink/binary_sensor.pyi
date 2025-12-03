from .const import DOMAIN as DOMAIN
from .coordinator import PrusaLinkUpdateCoordinator as PrusaLinkUpdateCoordinator
from .entity import PrusaLinkEntity as PrusaLinkEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyprusalink.types import JobInfo, PrinterInfo, PrinterStatus
from pyprusalink.types_legacy import LegacyPrinterStatus
from typing import Generic, TypeVar

T = TypeVar('T', PrinterStatus, LegacyPrinterStatus, JobInfo, PrinterInfo)

@dataclass(frozen=True)
class PrusaLinkBinarySensorEntityDescriptionMixin(Generic[T]):
    value_fn: Callable[[T], bool]

@dataclass(frozen=True)
class PrusaLinkBinarySensorEntityDescription(BinarySensorEntityDescription, PrusaLinkBinarySensorEntityDescriptionMixin[T], Generic[T]):
    available_fn: Callable[[T], bool] = ...

BINARY_SENSORS: dict[str, tuple[PrusaLinkBinarySensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PrusaLinkBinarySensorEntity(PrusaLinkEntity, BinarySensorEntity):
    entity_description: PrusaLinkBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PrusaLinkUpdateCoordinator, description: PrusaLinkBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
