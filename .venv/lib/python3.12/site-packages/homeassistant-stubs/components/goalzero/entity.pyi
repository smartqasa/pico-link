from .const import ATTRIBUTION as ATTRIBUTION, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import GoalZeroDataUpdateCoordinator as GoalZeroDataUpdateCoordinator
from _typeshed import Incomplete
from goalzero import Yeti as Yeti
from homeassistant.const import ATTR_MODEL as ATTR_MODEL, CONF_NAME as CONF_NAME
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class GoalZeroEntity(CoordinatorEntity[GoalZeroDataUpdateCoordinator]):
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: GoalZeroDataUpdateCoordinator, description: EntityDescription) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def _api(self) -> Yeti: ...
