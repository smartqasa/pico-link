from ..const import CONF_ALLOW_CLIP_SENSOR as CONF_ALLOW_CLIP_SENSOR, CONF_ALLOW_DECONZ_GROUPS as CONF_ALLOW_DECONZ_GROUPS, CONF_ALLOW_NEW_DEVICES as CONF_ALLOW_NEW_DEVICES, DEFAULT_ALLOW_CLIP_SENSOR as DEFAULT_ALLOW_CLIP_SENSOR, DEFAULT_ALLOW_DECONZ_GROUPS as DEFAULT_ALLOW_DECONZ_GROUPS, DEFAULT_ALLOW_NEW_DEVICES as DEFAULT_ALLOW_NEW_DEVICES
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from typing import Self

@dataclass
class DeconzConfig:
    entry: ConfigEntry
    host: str
    port: int
    api_key: str
    allow_clip_sensor: bool
    allow_deconz_groups: bool
    allow_new_devices: bool
    @classmethod
    def from_config_entry(cls, config_entry: ConfigEntry) -> Self: ...
