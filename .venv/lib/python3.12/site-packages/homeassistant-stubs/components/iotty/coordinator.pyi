from . import api as api
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client, device_registry as dr
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from iottycloud.device import Device as Device

_LOGGER: Incomplete
UPDATE_INTERVAL: Incomplete

@dataclass
class IottyData:
    devices: list[Device]

class IottyDataUpdateCoordinator(DataUpdateCoordinator[IottyData]):
    config_entry: ConfigEntry
    _entities: dict[str, Entity]
    _devices: list[Device]
    _device_registry: dr.DeviceRegistry
    iotty: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, session: OAuth2Session) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> IottyData: ...
