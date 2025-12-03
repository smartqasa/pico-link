from . import GuardianData as GuardianData
from .const import API_VALVE_STATUS as API_VALVE_STATUS, API_WIFI_STATUS as API_WIFI_STATUS, DOMAIN as DOMAIN
from .entity import ValveControllerEntity as ValveControllerEntity, ValveControllerEntityDescription as ValveControllerEntityDescription
from .util import convert_exceptions_to_homeassistant_error as convert_exceptions_to_homeassistant_error
from .valve import GuardianValveState as GuardianValveState
from _typeshed import Incomplete
from aioguardian import Client as Client
from collections.abc import Awaitable, Callable as Callable, Mapping
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

ATTR_AVG_CURRENT: str
ATTR_CONNECTED_CLIENTS: str
ATTR_INST_CURRENT: str
ATTR_INST_CURRENT_DDT: str
ATTR_STATION_CONNECTED: str
ATTR_TRAVEL_COUNT: str
SWITCH_KIND_ONBOARD_AP: str
SWITCH_KIND_VALVE: str

@dataclass(frozen=True, kw_only=True)
class ValveControllerSwitchDescription(SwitchEntityDescription, ValveControllerEntityDescription):
    extra_state_attributes_fn: Callable[[dict[str, Any]], Mapping[str, Any]]
    is_on_fn: Callable[[dict[str, Any]], bool]
    off_fn: Callable[[Client], Awaitable]
    on_fn: Callable[[Client], Awaitable]

async def _async_disable_ap(client: Client) -> None: ...
async def _async_enable_ap(client: Client) -> None: ...
async def _async_close_valve(client: Client) -> None: ...
async def _async_open_valve(client: Client) -> None: ...
@callback
def is_open(data: dict[str, Any]) -> bool: ...

VALVE_CONTROLLER_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ValveControllerSwitch(ValveControllerEntity, SwitchEntity):
    entity_description: ValveControllerSwitchDescription
    _client: Incomplete
    def __init__(self, entry: ConfigEntry, data: GuardianData, description: ValveControllerSwitchDescription) -> None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any]: ...
    @property
    def is_on(self) -> bool: ...
    @convert_exceptions_to_homeassistant_error
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @convert_exceptions_to_homeassistant_error
    async def async_turn_on(self, **kwargs: Any) -> None: ...
