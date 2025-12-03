import ssl
from ..const import CONF_ALLOW_BANDWIDTH_SENSORS as CONF_ALLOW_BANDWIDTH_SENSORS, CONF_ALLOW_UPTIME_SENSORS as CONF_ALLOW_UPTIME_SENSORS, CONF_BLOCK_CLIENT as CONF_BLOCK_CLIENT, CONF_CLIENT_SOURCE as CONF_CLIENT_SOURCE, CONF_DETECTION_TIME as CONF_DETECTION_TIME, CONF_DPI_RESTRICTIONS as CONF_DPI_RESTRICTIONS, CONF_IGNORE_WIRED_BUG as CONF_IGNORE_WIRED_BUG, CONF_SITE_ID as CONF_SITE_ID, CONF_SSID_FILTER as CONF_SSID_FILTER, CONF_TRACK_CLIENTS as CONF_TRACK_CLIENTS, CONF_TRACK_DEVICES as CONF_TRACK_DEVICES, CONF_TRACK_WIRED_CLIENTS as CONF_TRACK_WIRED_CLIENTS, DEFAULT_ALLOW_BANDWIDTH_SENSORS as DEFAULT_ALLOW_BANDWIDTH_SENSORS, DEFAULT_ALLOW_UPTIME_SENSORS as DEFAULT_ALLOW_UPTIME_SENSORS, DEFAULT_DETECTION_TIME as DEFAULT_DETECTION_TIME, DEFAULT_DPI_RESTRICTIONS as DEFAULT_DPI_RESTRICTIONS, DEFAULT_IGNORE_WIRED_BUG as DEFAULT_IGNORE_WIRED_BUG, DEFAULT_TRACK_CLIENTS as DEFAULT_TRACK_CLIENTS, DEFAULT_TRACK_DEVICES as DEFAULT_TRACK_DEVICES, DEFAULT_TRACK_WIRED_CLIENTS as DEFAULT_TRACK_WIRED_CLIENTS
from dataclasses import dataclass
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from typing import Literal, Self

@dataclass
class UnifiConfig:
    entry: ConfigEntry
    host: str
    port: int
    username: str
    password: str
    site: str
    ssl_context: ssl.SSLContext | Literal[False]
    option_supported_clients: list[str]
    option_track_clients: list[str]
    option_track_wired_clients: list[str]
    option_track_devices: bool
    option_ssid_filter: set[str]
    option_detection_time: timedelta
    option_ignore_wired_bug: bool
    option_block_clients: list[str]
    option_dpi_restrictions: bool
    option_allow_bandwidth_sensors: bool
    option_allow_uptime_sensors: bool
    @classmethod
    def from_config_entry(cls, config_entry: ConfigEntry) -> Self: ...
