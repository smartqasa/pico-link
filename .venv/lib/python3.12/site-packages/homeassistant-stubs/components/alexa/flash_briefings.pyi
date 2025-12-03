from .const import API_PASSWORD as API_PASSWORD, ATTR_MAIN_TEXT as ATTR_MAIN_TEXT, ATTR_REDIRECTION_URL as ATTR_REDIRECTION_URL, ATTR_STREAM_URL as ATTR_STREAM_URL, ATTR_TITLE_TEXT as ATTR_TITLE_TEXT, ATTR_UID as ATTR_UID, ATTR_UPDATE_DATE as ATTR_UPDATE_DATE, CONF_AUDIO as CONF_AUDIO, CONF_DISPLAY_URL as CONF_DISPLAY_URL, CONF_TEXT as CONF_TEXT, CONF_TITLE as CONF_TITLE, CONF_UID as CONF_UID, DATE_FORMAT as DATE_FORMAT
from _typeshed import Incomplete
from aiohttp.web_response import StreamResponse as StreamResponse
from homeassistant.components import http as http
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import template as template
from homeassistant.helpers.typing import ConfigType as ConfigType
from http import HTTPStatus

_LOGGER: Incomplete
FLASH_BRIEFINGS_API_ENDPOINT: str

@callback
def async_setup(hass: HomeAssistant, flash_briefing_config: ConfigType) -> None: ...

class AlexaFlashBriefingView(http.HomeAssistantView):
    url = FLASH_BRIEFINGS_API_ENDPOINT
    requires_auth: bool
    name: str
    flash_briefings: Incomplete
    def __init__(self, hass: HomeAssistant, flash_briefings: ConfigType) -> None: ...
    @callback
    def get(self, request: http.HomeAssistantRequest, briefing_id: str) -> StreamResponse | tuple[bytes, HTTPStatus]: ...
