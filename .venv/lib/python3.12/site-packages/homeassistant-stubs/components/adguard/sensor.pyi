from . import AdGuardConfigEntry as AdGuardConfigEntry, AdGuardData as AdGuardData
from .const import DOMAIN as DOMAIN
from .entity import AdGuardHomeEntity as AdGuardHomeEntity
from _typeshed import Incomplete
from adguardhome import AdGuardHome as AdGuardHome
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SCAN_INTERVAL: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class AdGuardHomeEntityDescription(SensorEntityDescription):
    value_fn: Callable[[AdGuardHome], Coroutine[Any, Any, int | float]]

SENSORS: tuple[AdGuardHomeEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AdGuardConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AdGuardHomeSensor(AdGuardHomeEntity, SensorEntity):
    entity_description: AdGuardHomeEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, data: AdGuardData, entry: AdGuardConfigEntry, description: AdGuardHomeEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    async def _adguard_update(self) -> None: ...
