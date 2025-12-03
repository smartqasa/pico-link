import evohomeasync2 as evo
from . import EvoSession as EvoSession
from .const import CONF_LOCATION_IDX as CONF_LOCATION_IDX, DOMAIN as DOMAIN, GWS as GWS, TCS as TCS, UTC_OFFSET as UTC_OFFSET
from .helpers import handle_evo_exception as handle_evo_exception
from _typeshed import Incomplete
from collections.abc import Awaitable
from datetime import timedelta
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from typing import Any

_LOGGER: Incomplete

class EvoBroker:
    loc_idx: int
    loc: evo.Location
    loc_utc_offset: timedelta
    tcs: evo.ControlSystem
    _sess: Incomplete
    hass: Incomplete
    client: Incomplete
    client_v1: Incomplete
    temps: dict[str, float | None]
    def __init__(self, sess: EvoSession) -> None: ...
    def validate_location(self, loc_idx: int) -> bool: ...
    async def call_client_api(self, client_api: Awaitable[dict[str, Any] | None], update_state: bool = True) -> dict[str, Any] | None: ...
    async def _update_v1_api_temps(self) -> None: ...
    async def _update_v2_api_state(self, *args: Any) -> None: ...
    async def async_update(self, *args: Any) -> None: ...
