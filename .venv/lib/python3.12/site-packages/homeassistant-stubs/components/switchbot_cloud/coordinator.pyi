from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from switchbot_api import Device as Device, Remote, SwitchBotAPI as SwitchBotAPI
from typing import Any

_LOGGER: Incomplete
type Status = dict[str, Any] | None

class SwitchBotCoordinator(DataUpdateCoordinator[Status]):
    _api: SwitchBotAPI
    _device_id: str
    _should_poll: Incomplete
    def __init__(self, hass: HomeAssistant, api: SwitchBotAPI, device: Device | Remote) -> None: ...
    async def _async_update_data(self) -> Status: ...
