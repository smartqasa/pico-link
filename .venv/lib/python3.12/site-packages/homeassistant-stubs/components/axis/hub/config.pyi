from ..const import CONF_STREAM_PROFILE as CONF_STREAM_PROFILE, CONF_VIDEO_SOURCE as CONF_VIDEO_SOURCE, DEFAULT_STREAM_PROFILE as DEFAULT_STREAM_PROFILE, DEFAULT_TRIGGER_TIME as DEFAULT_TRIGGER_TIME, DEFAULT_VIDEO_SOURCE as DEFAULT_VIDEO_SOURCE
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MODEL as CONF_MODEL, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_PROTOCOL as CONF_PROTOCOL, CONF_TRIGGER_TIME as CONF_TRIGGER_TIME, CONF_USERNAME as CONF_USERNAME
from typing import Self

@dataclass
class AxisConfig:
    entry: ConfigEntry
    protocol: str
    host: str
    port: int
    username: str
    password: str
    model: str
    name: str
    stream_profile: str
    trigger_time: int
    video_source: str
    @classmethod
    def from_config_entry(cls, config_entry: ConfigEntry) -> Self: ...
