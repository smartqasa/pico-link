from .const import CONF_CLOCK_FORMAT as CONF_CLOCK_FORMAT, CONF_MONITORED_RESOURCES as CONF_MONITORED_RESOURCES, FitbitScope as FitbitScope
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

@dataclass
class FitbitProfile:
    encoded_id: str
    display_name: str
    locale: str | None

@dataclass
class FitbitDevice:
    id: str
    device_version: str
    battery_level: int
    battery: str
    type: str

@dataclass
class FitbitConfig:
    clock_format: str | None
    monitored_resources: set[str] | None
    scopes: set[FitbitScope]
    def is_explicit_enable(self, key: str) -> bool: ...
    def is_allowed_resource(self, scope: FitbitScope | None, key: str) -> bool: ...

def config_from_entry_data(data: Mapping[str, Any]) -> FitbitConfig: ...
