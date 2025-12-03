from . import AutomowerConfigEntry as AutomowerConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import AutomowerDataUpdateCoordinator as AutomowerDataUpdateCoordinator
from .entity import AutomowerAvailableEntity as AutomowerAvailableEntity, handle_sending_exception as handle_sending_exception
from _typeshed import Incomplete
from aioautomower.model import WorkArea as WorkArea
from datetime import timedelta
from homeassistant.components.lawn_mower import LawnMowerActivity as LawnMowerActivity, LawnMowerEntity as LawnMowerEntity, LawnMowerEntityFeature as LawnMowerEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete
PARALLEL_UPDATES: int
DOCKED_ACTIVITIES: Incomplete
MOWING_ACTIVITIES: Incomplete
PAUSED_STATES: Incomplete
SUPPORT_STATE_SERVICES: Incomplete
MOW: str
PARK: str
OVERRIDE_MODES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AutomowerConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AutomowerLawnMowerEntity(AutomowerAvailableEntity, LawnMowerEntity):
    _attr_name: Incomplete
    _attr_supported_features = SUPPORT_STATE_SERVICES
    _attr_unique_id: Incomplete
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator) -> None: ...
    @property
    def activity(self) -> LawnMowerActivity: ...
    @property
    def work_areas(self) -> dict[int, WorkArea] | None: ...
    async def async_start_mowing(self) -> None: ...
    async def async_pause(self) -> None: ...
    async def async_dock(self) -> None: ...
    async def async_override_schedule(self, override_mode: str, duration: timedelta) -> None: ...
    async def async_override_schedule_work_area(self, work_area_id: int, duration: timedelta) -> None: ...
