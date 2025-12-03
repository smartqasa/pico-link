from .const import CONTROLLER as CONTROLLER
from .storage import async_get_entity_storage as async_get_entity_storage
from aiohomekit import Controller
from functools import lru_cache
from homeassistant.components import bluetooth as bluetooth, zeroconf as zeroconf
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant

type IidTuple = tuple[int, int | None, int | None]
def unique_id_to_iids(unique_id: str) -> IidTuple | None: ...
@lru_cache
def folded_name(name: str) -> str: ...
async def async_get_controller(hass: HomeAssistant) -> Controller: ...
