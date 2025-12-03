from .const import DOMAIN as DOMAIN
from .coordinator import ValloxDataUpdateCoordinator as ValloxDataUpdateCoordinator
from .entity import ValloxEntity as ValloxEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from vallox_websocket_api import Vallox as Vallox

class ValloxNumberEntity(ValloxEntity, NumberEntity):
    entity_description: ValloxNumberEntityDescription
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    _client: Incomplete
    def __init__(self, name: str, coordinator: ValloxDataUpdateCoordinator, description: ValloxNumberEntityDescription, client: Vallox) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...

@dataclass(frozen=True, kw_only=True)
class ValloxNumberEntityDescription(NumberEntityDescription):
    metric_key: str

NUMBER_ENTITIES: tuple[ValloxNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
