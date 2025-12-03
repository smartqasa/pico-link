from .const import DOMAIN as DOMAIN
from aiohttp import web as web
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.auth.permissions.const import POLICY_EDIT as POLICY_EDIT
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.http.data_validator import RequestDataValidator as RequestDataValidator
from homeassistant.components.http.decorators import require_admin as require_admin
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import Unauthorized as Unauthorized
from homeassistant.helpers.data_entry_flow import FlowManagerIndexView as FlowManagerIndexView, FlowManagerResourceView as FlowManagerResourceView
from typing import Any

@callback
def async_setup(hass: HomeAssistant) -> None: ...
@callback
def ws_get_issue_data(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def ws_ignore_issue(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def ws_list_issues(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...

class RepairsFlowIndexView(FlowManagerIndexView):
    url: str
    name: str
    async def post(self, request: web.Request, data: dict[str, Any]) -> web.Response: ...

class RepairsFlowResourceView(FlowManagerResourceView):
    url: str
    name: str
    async def get(self, request: web.Request, /, flow_id: str) -> web.Response: ...
    async def post(self, request: web.Request, flow_id: str) -> web.Response: ...
