from .const import ATTRIBUTION as ATTRIBUTION, DOMAIN as DOMAIN, HOP_COORDINATOR as HOP_COORDINATOR
from .coordinator import ElectricKiwiHOPDataCoordinator as ElectricKiwiHOPDataCoordinator
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

_LOGGER: Incomplete
ATTR_EK_HOP_SELECT: str
HOP_SELECT: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElectricKiwiSelectHOPEntity(CoordinatorEntity[ElectricKiwiHOPDataCoordinator], SelectEntity):
    entity_description: SelectEntityDescription
    _attr_has_entity_name: bool
    _attr_attribution = ATTRIBUTION
    values_dict: dict[str, int]
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    def __init__(self, coordinator: ElectricKiwiHOPDataCoordinator, description: SelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
