from . import SensiboConfigEntry as SensiboConfigEntry
from .coordinator import SensiboDataUpdateCoordinator as SensiboDataUpdateCoordinator
from .entity import SensiboDeviceBaseEntity as SensiboDeviceBaseEntity, async_handle_api_call as async_handle_api_call
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pysensibo.model import SensiboDevice as SensiboDevice
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class SensiboNumberEntityDescription(NumberEntityDescription):
    remote_key: str
    value_fn: Callable[[SensiboDevice], float | None]

DEVICE_NUMBER_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SensiboConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SensiboNumber(SensiboDeviceBaseEntity, NumberEntity):
    entity_description: SensiboNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SensiboDataUpdateCoordinator, device_id: str, entity_description: SensiboNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
    @async_handle_api_call
    async def async_send_api_call(self, key: str, value: Any) -> bool: ...
