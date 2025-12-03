from .coordinator import SwitcherDataUpdateCoordinator as SwitcherDataUpdateCoordinator
from _typeshed import Incomplete
from aioswitcher.api.messages import SwitcherBaseResponse as SwitcherBaseResponse
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGER: Incomplete

class SwitcherEntity(CoordinatorEntity[SwitcherDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SwitcherDataUpdateCoordinator) -> None: ...
    async def _async_call_api(self, api: str, *args: Any, **kwargs: Any) -> None: ...
