from . import RainMachineConfigEntry as RainMachineConfigEntry
from .const import DATA_MACHINE_FIRMWARE_UPDATE_STATUS as DATA_MACHINE_FIRMWARE_UPDATE_STATUS
from .entity import RainMachineEntity as RainMachineEntity, RainMachineEntityDescription as RainMachineEntityDescription
from _typeshed import Incomplete
from dataclasses import dataclass
from enum import Enum
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

class UpdateStates(Enum):
    IDLE = 1
    CHECKING = 2
    DOWNLOADING = 3
    UPGRADING = 4
    ERROR = 5
    REBOOT = 6

UPDATE_STATE_MAP: Incomplete

@dataclass(frozen=True, kw_only=True)
class RainMachineUpdateEntityDescription(UpdateEntityDescription, RainMachineEntityDescription): ...

UPDATE_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: RainMachineConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RainMachineUpdateEntity(RainMachineEntity, UpdateEntity):
    _attr_device_class: Incomplete
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
    _attr_installed_version: Incomplete
    _attr_in_progress: bool
    _attr_latest_version: Incomplete
    _attr_title: Incomplete
    @callback
    def update_from_latest_data(self) -> None: ...
