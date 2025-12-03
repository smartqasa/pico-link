from . import WizConfigEntry as WizConfigEntry
from .entity import WizEntity as WizEntity
from .models import WizData as WizData
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pywizlight import wizlight as wizlight

@dataclass(frozen=True, kw_only=True)
class WizNumberEntityDescription(NumberEntityDescription):
    required_feature: str
    set_value_fn: Callable[[wizlight, int], Coroutine[None, None, None]]
    value_fn: Callable[[wizlight], int | None]

async def _async_set_speed(device: wizlight, speed: int) -> None: ...
async def _async_set_ratio(device: wizlight, ratio: int) -> None: ...

NUMBERS: tuple[WizNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: WizConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WizSpeedNumber(WizEntity, NumberEntity):
    entity_description: WizNumberEntityDescription
    _attr_mode: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, wiz_data: WizData, name: str, description: WizNumberEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    _attr_native_value: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
