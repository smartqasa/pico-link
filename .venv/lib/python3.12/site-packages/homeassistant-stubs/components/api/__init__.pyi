import homeassistant.core as ha
from _typeshed import Incomplete
from aiohttp import web
from functools import lru_cache
from homeassistant.auth.models import User as User
from homeassistant.auth.permissions.const import POLICY_READ as POLICY_READ
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS, KEY_HASS_USER as KEY_HASS_USER, require_admin as require_admin
from homeassistant.const import CONTENT_TYPE_JSON as CONTENT_TYPE_JSON, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, EVENT_STATE_CHANGED as EVENT_STATE_CHANGED, MATCH_ALL as MATCH_ALL, URL_API as URL_API, URL_API_COMPONENTS as URL_API_COMPONENTS, URL_API_CONFIG as URL_API_CONFIG, URL_API_CORE_STATE as URL_API_CORE_STATE, URL_API_ERROR_LOG as URL_API_ERROR_LOG, URL_API_EVENTS as URL_API_EVENTS, URL_API_SERVICES as URL_API_SERVICES, URL_API_STATES as URL_API_STATES, URL_API_STREAM as URL_API_STREAM, URL_API_TEMPLATE as URL_API_TEMPLATE
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant
from homeassistant.exceptions import InvalidEntityFormatError as InvalidEntityFormatError, InvalidStateError as InvalidStateError, ServiceNotFound as ServiceNotFound, TemplateError as TemplateError, Unauthorized as Unauthorized
from homeassistant.helpers import recorder as recorder, template as template
from homeassistant.helpers.json import json_dumps as json_dumps, json_fragment as json_fragment
from homeassistant.helpers.service import async_get_all_descriptions as async_get_all_descriptions
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.event_type import EventType as EventType
from homeassistant.util.json import json_loads as json_loads
from typing import Any

_LOGGER: Incomplete
ATTR_BASE_URL: str
ATTR_EXTERNAL_URL: str
ATTR_INTERNAL_URL: str
ATTR_LOCATION_NAME: str
ATTR_INSTALLATION_TYPE: str
ATTR_REQUIRES_API_PASSWORD: str
ATTR_UUID: str
ATTR_VERSION: str
DOMAIN: str
STREAM_PING_PAYLOAD: str
STREAM_PING_INTERVAL: int
SERVICE_WAIT_TIMEOUT: int
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class APIStatusView(HomeAssistantView):
    url = URL_API
    name: str
    @ha.callback
    def get(self, request: web.Request) -> web.Response: ...

class APICoreStateView(HomeAssistantView):
    url = URL_API_CORE_STATE
    name: str
    @ha.callback
    def get(self, request: web.Request) -> web.Response: ...

class APIEventStream(HomeAssistantView):
    url = URL_API_STREAM
    name: str
    @require_admin
    async def get(self, request: web.Request) -> web.StreamResponse: ...

class APIConfigView(HomeAssistantView):
    url = URL_API_CONFIG
    name: str
    @ha.callback
    def get(self, request: web.Request) -> web.Response: ...

class APIStatesView(HomeAssistantView):
    url = URL_API_STATES
    name: str
    @ha.callback
    def get(self, request: web.Request) -> web.Response: ...

class APIEntityStateView(HomeAssistantView):
    url: str
    name: str
    @ha.callback
    def get(self, request: web.Request, entity_id: str) -> web.Response: ...
    async def post(self, request: web.Request, entity_id: str) -> web.Response: ...
    @ha.callback
    def delete(self, request: web.Request, entity_id: str) -> web.Response: ...

class APIEventListenersView(HomeAssistantView):
    url = URL_API_EVENTS
    name: str
    @ha.callback
    def get(self, request: web.Request) -> web.Response: ...

class APIEventView(HomeAssistantView):
    url: str
    name: str
    @require_admin
    async def post(self, request: web.Request, event_type: str) -> web.Response: ...

class APIServicesView(HomeAssistantView):
    url = URL_API_SERVICES
    name: str
    async def get(self, request: web.Request) -> web.Response: ...

class APIDomainServicesView(HomeAssistantView):
    url: str
    name: str
    async def post(self, request: web.Request, domain: str, service: str) -> web.Response: ...

class APIComponentsView(HomeAssistantView):
    url = URL_API_COMPONENTS
    name: str
    @ha.callback
    def get(self, request: web.Request) -> web.Response: ...

@lru_cache
def _cached_template(template_str: str, hass: HomeAssistant) -> template.Template: ...

class APITemplateView(HomeAssistantView):
    url = URL_API_TEMPLATE
    name: str
    @require_admin
    async def post(self, request: web.Request) -> web.Response: ...

class APIErrorLog(HomeAssistantView):
    url = URL_API_ERROR_LOG
    name: str
    @require_admin
    async def get(self, request: web.Request) -> web.FileResponse: ...

async def async_services_json(hass: HomeAssistant) -> list[dict[str, Any]]: ...
@ha.callback
def async_events_json(hass: HomeAssistant) -> list[dict[str, Any]]: ...
