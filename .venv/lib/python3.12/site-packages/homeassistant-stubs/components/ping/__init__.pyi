from .const import CONF_PING_COUNT as CONF_PING_COUNT, DOMAIN as DOMAIN
from .coordinator import PingUpdateCoordinator as PingUpdateCoordinator
from .helpers import PingDataICMPLib as PingDataICMPLib, PingDataSubProcess as PingDataSubProcess
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
PLATFORMS: Incomplete
DATA_PRIVILEGED_KEY: HassKey[bool | None]
type PingConfigEntry = ConfigEntry[PingUpdateCoordinator]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: PingConfigEntry) -> bool: ...
async def async_reload_entry(hass: HomeAssistant, entry: PingConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: PingConfigEntry) -> bool: ...
async def _can_use_icmp_lib_with_privilege() -> bool | None: ...
