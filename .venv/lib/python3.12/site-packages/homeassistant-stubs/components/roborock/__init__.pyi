from .const import CONF_BASE_URL as CONF_BASE_URL, CONF_USER_DATA as CONF_USER_DATA, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator, RoborockDataUpdateCoordinatorA01 as RoborockDataUpdateCoordinatorA01
from _typeshed import Incomplete
from collections.abc import Coroutine
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from roborock import HomeDataRoom as HomeDataRoom
from roborock.containers import HomeDataDevice as HomeDataDevice, HomeDataProduct as HomeDataProduct, UserData
from typing import Any

SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete
type RoborockConfigEntry = ConfigEntry[RoborockCoordinators]

@dataclass
class RoborockCoordinators:
    v1: list[RoborockDataUpdateCoordinator]
    a01: list[RoborockDataUpdateCoordinatorA01]
    def values(self) -> list[RoborockDataUpdateCoordinator | RoborockDataUpdateCoordinatorA01]: ...

async def async_setup_entry(hass: HomeAssistant, entry: RoborockConfigEntry) -> bool: ...
def build_setup_functions(hass: HomeAssistant, device_map: dict[str, HomeDataDevice], user_data: UserData, product_info: dict[str, HomeDataProduct], home_data_rooms: list[HomeDataRoom]) -> list[Coroutine[Any, Any, RoborockDataUpdateCoordinator | RoborockDataUpdateCoordinatorA01 | None]]: ...
async def setup_device(hass: HomeAssistant, user_data: UserData, device: HomeDataDevice, product_info: HomeDataProduct, home_data_rooms: list[HomeDataRoom]) -> RoborockDataUpdateCoordinator | RoborockDataUpdateCoordinatorA01 | None: ...
async def setup_device_v1(hass: HomeAssistant, user_data: UserData, device: HomeDataDevice, product_info: HomeDataProduct, home_data_rooms: list[HomeDataRoom]) -> RoborockDataUpdateCoordinator | None: ...
async def setup_device_a01(hass: HomeAssistant, user_data: UserData, device: HomeDataDevice, product_info: HomeDataProduct) -> RoborockDataUpdateCoordinatorA01 | None: ...
async def async_unload_entry(hass: HomeAssistant, entry: RoborockConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: RoborockConfigEntry) -> None: ...
