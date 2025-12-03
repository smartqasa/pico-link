from .helpers import async_determine_event_types as async_determine_event_types
from .processor import EventProcessor as EventProcessor
from _typeshed import Incomplete
from aiohttp import web as web
from collections.abc import Callable as Callable
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS
from homeassistant.components.recorder import get_instance as get_instance
from homeassistant.components.recorder.filters import Filters as Filters
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import InvalidEntityFormatError as InvalidEntityFormatError
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

@callback
def async_setup(hass: HomeAssistant, conf: ConfigType, filters: Filters | None, entities_filter: Callable[[str], bool] | None) -> None: ...

class LogbookView(HomeAssistantView):
    url: str
    name: str
    extra_urls: Incomplete
    config: Incomplete
    filters: Incomplete
    entities_filter: Incomplete
    def __init__(self, config: dict[str, Any], filters: Filters | None, entities_filter: Callable[[str], bool] | None) -> None: ...
    async def get(self, request: web.Request, datetime: str | None = None) -> web.Response: ...
