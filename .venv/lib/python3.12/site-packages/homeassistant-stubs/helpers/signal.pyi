import asyncio
from _typeshed import Incomplete
from homeassistant.const import RESTART_EXIT_CODE as RESTART_EXIT_CODE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.hass_dict import HassKey as HassKey

_LOGGER: Incomplete
KEY_HA_STOP: HassKey[asyncio.Task[None]]

@callback
@bind_hass
def async_register_signal_handling(hass: HomeAssistant) -> None: ...
