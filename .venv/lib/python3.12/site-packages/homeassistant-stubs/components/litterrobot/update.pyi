from . import LitterRobotConfigEntry as LitterRobotConfigEntry
from .entity import LitterRobotEntity as LitterRobotEntity
from _typeshed import Incomplete
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pylitterbot import LitterRobot4
from typing import Any

SCAN_INTERVAL: Incomplete
FIRMWARE_UPDATE_ENTITY: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RobotUpdateEntity(LitterRobotEntity[LitterRobot4], UpdateEntity):
    _attr_supported_features: Incomplete
    @property
    def installed_version(self) -> str: ...
    @property
    def in_progress(self) -> bool: ...
    @property
    def should_poll(self) -> bool: ...
    _attr_latest_version: Incomplete
    async def async_update(self) -> None: ...
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
