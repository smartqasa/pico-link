from _typeshed import Incomplete
from aiohttp import web
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import ConfigType as ConfigType

CONTENT_TYPE_XML: str
DOMAIN: str
CONFIG_SCHEMA: Incomplete

def setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class RssView(HomeAssistantView):
    name: str
    url: Incomplete
    requires_auth: Incomplete
    _title: Incomplete
    _items: Incomplete
    def __init__(self, url: str, requires_auth: bool, title: Template | None, items: list[dict[str, Template]]) -> None: ...
    async def get(self, request: web.Request) -> web.Response: ...
