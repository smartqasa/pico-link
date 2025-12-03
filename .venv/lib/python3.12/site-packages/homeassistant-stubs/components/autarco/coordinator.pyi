from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from autarco import AccountSite as AccountSite, Autarco as Autarco, Battery as Battery, Inverter as Inverter, Site as Site, Solar as Solar
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import NamedTuple

class AutarcoData(NamedTuple):
    solar: Solar
    inverters: dict[str, Inverter]
    site: Site
    battery: Battery | None

class AutarcoDataUpdateCoordinator(DataUpdateCoordinator[AutarcoData]):
    config_entry: ConfigEntry
    client: Incomplete
    account_site: Incomplete
    def __init__(self, hass: HomeAssistant, client: Autarco, account_site: AccountSite) -> None: ...
    async def _async_update_data(self) -> AutarcoData: ...
