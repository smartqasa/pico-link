from .const import DEFAULT_RETRY_COUNT as DEFAULT_RETRY_COUNT, DEFAULT_RETRY_TIMEOUT as DEFAULT_RETRY_TIMEOUT
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from tololib import ToloSettings as ToloSettings, ToloStatus as ToloStatus
from typing import NamedTuple

_LOGGER: Incomplete

class ToloSaunaData(NamedTuple):
    status: ToloStatus
    settings: ToloSettings

class ToloSaunaUpdateCoordinator(DataUpdateCoordinator[ToloSaunaData]):
    client: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> ToloSaunaData: ...
    def _get_tolo_sauna_data(self) -> ToloSaunaData: ...
