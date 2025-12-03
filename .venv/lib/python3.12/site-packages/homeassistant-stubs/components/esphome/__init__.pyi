from .const import CONF_NOISE_PSK as CONF_NOISE_PSK, DATA_FFMPEG_PROXY as DATA_FFMPEG_PROXY, DOMAIN as DOMAIN
from .domain_data import DomainData as DomainData
from .entry_data import ESPHomeConfigEntry as ESPHomeConfigEntry, RuntimeEntryData as RuntimeEntryData
from .ffmpeg_proxy import FFmpegProxyData as FFmpegProxyData, FFmpegProxyView as FFmpegProxyView
from .manager import ESPHomeManager as ESPHomeManager, cleanup_instance as cleanup_instance
from _typeshed import Incomplete
from homeassistant.components import ffmpeg as ffmpeg, zeroconf as zeroconf
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete
CLIENT_INFO: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ESPHomeConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ESPHomeConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: ESPHomeConfigEntry) -> None: ...
