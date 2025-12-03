import evohomeasync2 as evo
from . import EvoBroker as EvoBroker, EvoService as EvoService
from .const import DOMAIN as DOMAIN
from .helpers import convert_dict as convert_dict, convert_until as convert_until
from _typeshed import Incomplete
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import Entity as Entity
from typing import Any

_LOGGER: Incomplete

class EvoDevice(Entity):
    _attr_should_poll: bool
    _evo_device: Incomplete
    _evo_broker: Incomplete
    _device_state_attrs: dict[str, Any]
    def __init__(self, evo_broker: EvoBroker, evo_device: evo.ControlSystem | evo.HotWater | evo.Zone) -> None: ...
    async def async_refresh(self, payload: dict | None = None) -> None: ...
    async def async_tcs_svc_request(self, service: str, data: dict[str, Any]) -> None: ...
    async def async_zone_svc_request(self, service: str, data: dict[str, Any]) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    async def async_added_to_hass(self) -> None: ...

class EvoChild(EvoDevice):
    _evo_id: str
    _evo_tcs: Incomplete
    _schedule: dict[str, Any]
    _setpoints: dict[str, Any]
    def __init__(self, evo_broker: EvoBroker, evo_device: evo.HotWater | evo.Zone) -> None: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def setpoints(self) -> dict[str, Any]: ...
    async def _update_schedule(self) -> None: ...
    _device_state_attrs: Incomplete
    async def async_update(self) -> None: ...
