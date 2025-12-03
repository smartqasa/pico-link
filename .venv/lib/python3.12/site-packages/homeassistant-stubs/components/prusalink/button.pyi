from .const import DOMAIN as DOMAIN
from .coordinator import PrusaLinkUpdateCoordinator as PrusaLinkUpdateCoordinator
from .entity import PrusaLinkEntity as PrusaLinkEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyprusalink import JobInfo, LegacyPrinterStatus, PrinterStatus, PrusaLink as PrusaLink
from typing import Any, Generic, TypeVar

T = TypeVar('T', PrinterStatus, LegacyPrinterStatus, JobInfo)

@dataclass(frozen=True)
class PrusaLinkButtonEntityDescriptionMixin(Generic[T]):
    press_fn: Callable[[PrusaLink], Callable[[int], Coroutine[Any, Any, None]]]

@dataclass(frozen=True)
class PrusaLinkButtonEntityDescription(ButtonEntityDescription, PrusaLinkButtonEntityDescriptionMixin[T], Generic[T]):
    available_fn: Callable[[T], bool] = ...

BUTTONS: dict[str, tuple[PrusaLinkButtonEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PrusaLinkButtonEntity(PrusaLinkEntity, ButtonEntity):
    entity_description: PrusaLinkButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PrusaLinkUpdateCoordinator, description: PrusaLinkButtonEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_press(self) -> None: ...
