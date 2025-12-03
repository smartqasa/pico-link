from . import FytaConfigEntry as FytaConfigEntry
from .const import CONF_EXPIRATION as CONF_EXPIRATION, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from fyta_cli.fyta_connector import FytaConnector as FytaConnector
from fyta_cli.fyta_models import Plant
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete

class FytaCoordinator(DataUpdateCoordinator[dict[int, Plant]]):
    config_entry: FytaConfigEntry
    fyta: Incomplete
    _plants_last_update: set[int]
    new_device_callbacks: list[Callable[[int], None]]
    def __init__(self, hass: HomeAssistant, fyta: FytaConnector) -> None: ...
    data: Incomplete
    async def _async_update_data(self) -> dict[int, Plant]: ...
    def _async_add_remove_devices(self) -> None: ...
    async def renew_authentication(self) -> bool: ...
