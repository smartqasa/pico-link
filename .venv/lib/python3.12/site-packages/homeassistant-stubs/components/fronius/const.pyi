from enum import StrEnum
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.typing import StateType as StateType
from typing import Final, NamedTuple, TypedDict

DOMAIN: Final[str]
type SolarNetId = str
SOLAR_NET_DISCOVERY_NEW: Final[str]
SOLAR_NET_ID_POWER_FLOW: SolarNetId
SOLAR_NET_ID_SYSTEM: SolarNetId
SOLAR_NET_RESCAN_TIMER: Final[int]

class FroniusConfigEntryData(TypedDict):
    host: str
    is_logger: bool

class FroniusDeviceInfo(NamedTuple):
    device_info: DeviceInfo
    solar_net_id: SolarNetId
    unique_id: str

class InverterStatusCodeOption(StrEnum):
    STARTUP = 'startup'
    RUNNING = 'running'
    STANDBY = 'standby'
    BOOTLOADING = 'bootloading'
    ERROR = 'error'
    IDLE = 'idle'
    READY = 'ready'
    SLEEPING = 'sleeping'

_INVERTER_STATUS_CODES: Final[dict[int, InverterStatusCodeOption]]

def get_inverter_status_message(code: StateType) -> InverterStatusCodeOption | None: ...

INVERTER_ERROR_CODES: Final[dict[int, str]]

class MeterLocationCodeOption(StrEnum):
    FEED_IN = 'feed_in'
    CONSUMPTION_PATH = 'consumption_path'
    GENERATOR = 'external_generator'
    EXT_BATTERY = 'external_battery'
    SUBLOAD = 'subload'

def get_meter_location_description(code: StateType) -> MeterLocationCodeOption | None: ...

class OhmPilotStateCodeOption(StrEnum):
    UP_AND_RUNNING = 'up_and_running'
    KEEP_MINIMUM_TEMPERATURE = 'keep_minimum_temperature'
    LEGIONELLA_PROTECTION = 'legionella_protection'
    CRITICAL_FAULT = 'critical_fault'
    FAULT = 'fault'
    BOOST_MODE = 'boost_mode'

_OHMPILOT_STATE_CODES: Final[dict[int, OhmPilotStateCodeOption]]

def get_ohmpilot_state_message(code: StateType) -> OhmPilotStateCodeOption | None: ...
