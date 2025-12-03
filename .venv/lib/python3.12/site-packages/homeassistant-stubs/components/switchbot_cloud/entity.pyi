from .const import DOMAIN as DOMAIN
from .coordinator import SwitchBotCoordinator as SwitchBotCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from switchbot_api import Commands as Commands, Device as Device, Remote as Remote, SwitchBotAPI as SwitchBotAPI
from typing import Any

class SwitchBotCloudEntity(CoordinatorEntity[SwitchBotCoordinator]):
    _api: SwitchBotAPI
    _switchbot_state: dict[str, Any] | None
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, api: SwitchBotAPI, device: Device | Remote, coordinator: SwitchBotCoordinator) -> None: ...
    async def send_api_command(self, command: Commands, command_type: str = 'command', parameters: dict | str = 'default') -> None: ...
