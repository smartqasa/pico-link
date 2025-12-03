from .const import DOMAIN as DOMAIN, REG_KEY as REG_KEY
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.alarm_control_panel import AlarmControlPanelState as AlarmControlPanelState
from homeassistant.components.climate import HVACMode as HVACMode
from homeassistant.components.lock import LockState as LockState
from homeassistant.components.vacuum import VacuumActivity as VacuumActivity
from homeassistant.components.water_heater import STATE_ECO as STATE_ECO, STATE_ELECTRIC as STATE_ELECTRIC, STATE_GAS as STATE_GAS, STATE_HEAT_PUMP as STATE_HEAT_PUMP, STATE_HIGH_DEMAND as STATE_HIGH_DEMAND, STATE_PERFORMANCE as STATE_PERFORMANCE
from homeassistant.const import Platform as Platform, STATE_CLOSED as STATE_CLOSED, STATE_HOME as STATE_HOME, STATE_IDLE as STATE_IDLE, STATE_NOT_HOME as STATE_NOT_HOME, STATE_OFF as STATE_OFF, STATE_OK as STATE_OK, STATE_ON as STATE_ON, STATE_OPEN as STATE_OPEN, STATE_PAUSED as STATE_PAUSED, STATE_PLAYING as STATE_PLAYING, STATE_PROBLEM as STATE_PROBLEM
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.integration_platform import async_process_integration_platforms as async_process_integration_platforms
from typing import Protocol

EXCLUDED_DOMAINS: set[Platform | str]
ON_OFF_STATES: dict[Platform | str, tuple[set[str], str, str]]

async def async_setup(hass: HomeAssistant) -> None: ...

class GroupProtocol(Protocol):
    def async_describe_on_off_states(self, hass: HomeAssistant, registry: GroupIntegrationRegistry) -> None: ...

@callback
def _process_group_platform(hass: HomeAssistant, domain: str, platform: GroupProtocol) -> None: ...

@dataclass(frozen=True, slots=True)
class SingleStateType:
    on_state: str
    off_state: str

class GroupIntegrationRegistry:
    hass: Incomplete
    on_off_mapping: dict[str, str]
    off_on_mapping: dict[str, str]
    on_states_by_domain: dict[str, set[str]]
    exclude_domains: Incomplete
    state_group_mapping: dict[str, SingleStateType]
    def __init__(self, hass: HomeAssistant) -> None: ...
    @callback
    def exclude_domain(self, domain: str) -> None: ...
    @callback
    def on_off_states(self, domain: Platform | str, on_states: set[str], default_on_state: str, off_state: str) -> None: ...
