from . import OTBRConfigEntry as OTBRConfigEntry
from .const import DOMAIN as DOMAIN
from .util import OTBRData as OTBRData
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.homeassistant_hardware.silabs_multiprotocol_addon import is_multiprotocol_url as is_multiprotocol_url
from homeassistant.components.thread import async_add_dataset as async_add_dataset
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate

_LOGGER: Incomplete

def async_get_otbr_data[**_P, _R, _R_Def](retval: _R_Def) -> Callable[[Callable[Concatenate[HomeAssistant, OTBRData, _P], Coroutine[Any, Any, _R]]], Callable[Concatenate[HomeAssistant, _P], Coroutine[Any, Any, _R | _R_Def]]]: ...
async def async_change_channel(hass: HomeAssistant, data: OTBRData, channel: int, delay: float) -> None: ...
async def async_get_channel(hass: HomeAssistant, data: OTBRData) -> int | None: ...
async def async_using_multipan(hass: HomeAssistant, data: OTBRData) -> bool: ...
