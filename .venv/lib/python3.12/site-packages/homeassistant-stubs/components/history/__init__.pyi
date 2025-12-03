from . import websocket_api as websocket_api
from .const import DOMAIN as DOMAIN
from .helpers import entities_may_have_state_changes_after as entities_may_have_state_changes_after, has_states_before as has_states_before
from _typeshed import Incomplete
from aiohttp import web
from datetime import datetime as dt
from homeassistant.components import frontend as frontend
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS
from homeassistant.components.recorder import get_instance as get_instance, history as history
from homeassistant.components.recorder.util import session_scope as session_scope
from homeassistant.const import CONF_EXCLUDE as CONF_EXCLUDE, CONF_INCLUDE as CONF_INCLUDE
from homeassistant.core import HomeAssistant as HomeAssistant, valid_entity_id as valid_entity_id
from homeassistant.helpers.entityfilter import INCLUDE_EXCLUDE_BASE_FILTER_SCHEMA as INCLUDE_EXCLUDE_BASE_FILTER_SCHEMA
from homeassistant.helpers.typing import ConfigType as ConfigType

CONF_ORDER: str
_ONE_DAY: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class HistoryPeriodView(HomeAssistantView):
    url: str
    name: str
    extra_urls: Incomplete
    async def get(self, request: web.Request, datetime: str | None = None) -> web.Response: ...
    def _sorted_significant_states_json(self, hass: HomeAssistant, start_time: dt, end_time: dt, entity_ids: list[str], include_start_time_state: bool, significant_changes_only: bool, minimal_response: bool, no_attributes: bool) -> web.Response: ...
