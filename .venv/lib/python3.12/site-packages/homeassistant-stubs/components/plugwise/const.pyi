from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.const import Platform as Platform
from typing import Final, Literal

DOMAIN: Final[str]
LOGGER: Incomplete
API: Final[str]
FLOW_SMILE: Final[str]
FLOW_STRETCH: Final[str]
FLOW_TYPE: Final[str]
GATEWAY: Final[str]
GATEWAY_ID: Final[str]
LOCATION: Final[str]
PW_TYPE: Final[str]
REBOOT: Final[str]
SMILE: Final[str]
STRETCH: Final[str]
STRETCH_USERNAME: Final[str]
PLATFORMS: Final[list[str]]
ZEROCONF_MAP: Final[dict[str, str]]
type NumberType = Literal['maximum_boiler_temperature', 'max_dhw_temperature', 'temperature_offset']
type SelectType = Literal['select_dhw_mode', 'select_gateway_mode', 'select_regulation_mode', 'select_schedule']
type SelectOptionsType = Literal['dhw_modes', 'gateway_modes', 'regulation_modes', 'available_schedules']
DEFAULT_MAX_TEMP: Final[int]
DEFAULT_MIN_TEMP: Final[int]
DEFAULT_PORT: Final[int]
DEFAULT_SCAN_INTERVAL: Final[dict[str, timedelta]]
DEFAULT_USERNAME: Final[str]
MASTER_THERMOSTATS: Final[list[str]]
