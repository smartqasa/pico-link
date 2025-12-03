from . import AirGradientConfigEntry as AirGradientConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import AirGradientCoordinator as AirGradientCoordinator
from .entity import AirGradientEntity as AirGradientEntity
from _typeshed import Incomplete
from airgradient import AirGradientClient as AirGradientClient
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class AirGradientButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[AirGradientClient], Awaitable[None]]

CO2_CALIBRATION: Incomplete
LED_BAR_TEST: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AirGradientConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirGradientButton(AirGradientEntity, ButtonEntity):
    entity_description: AirGradientButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirGradientCoordinator, description: AirGradientButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
