from .const import DOMAIN as DOMAIN, QSW_TIMEOUT_SEC as QSW_TIMEOUT_SEC
from _typeshed import Incomplete
from aioqsw.localapi import QnapQswApi as QnapQswApi
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

DATA_SCAN_INTERVAL: Incomplete
FW_SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete

class QswDataCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    qsw: Incomplete
    def __init__(self, hass: HomeAssistant, qsw: QnapQswApi) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...

class QswFirmwareCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    qsw: Incomplete
    def __init__(self, hass: HomeAssistant, qsw: QnapQswApi) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
