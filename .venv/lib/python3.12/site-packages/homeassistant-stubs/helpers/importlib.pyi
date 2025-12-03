import asyncio
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.util.hass_dict import HassKey as HassKey
from types import ModuleType

_LOGGER: Incomplete
DATA_IMPORT_CACHE: HassKey[dict[str, ModuleType]]
DATA_IMPORT_FUTURES: HassKey[dict[str, asyncio.Future[ModuleType]]]
DATA_IMPORT_FAILURES: HassKey[dict[str, bool]]

def _get_module(cache: dict[str, ModuleType], name: str) -> ModuleType: ...
async def async_import_module(hass: HomeAssistant, name: str) -> ModuleType: ...
