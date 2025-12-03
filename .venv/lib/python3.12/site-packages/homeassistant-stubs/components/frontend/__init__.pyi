import jinja2
import pathlib
from .storage import async_setup_frontend_storage as async_setup_frontend_storage
from _typeshed import Incomplete
from aiohttp import web, web_urldispatcher
from collections.abc import Callable as Callable, Iterator
from homeassistant.components import onboarding as onboarding, websocket_api as websocket_api
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS, StaticPathConfig as StaticPathConfig
from homeassistant.components.websocket_api import ActiveConnection as ActiveConnection
from homeassistant.config import async_hass_config_yaml as async_hass_config_yaml
from homeassistant.const import CONF_MODE as CONF_MODE, CONF_NAME as CONF_NAME, EVENT_PANELS_UPDATED as EVENT_PANELS_UPDATED, EVENT_THEMES_UPDATED as EVENT_THEMES_UPDATED
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers import service as service
from homeassistant.helpers.icon import async_get_icons as async_get_icons
from homeassistant.helpers.json import json_dumps_sorted as json_dumps_sorted
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.translation import async_get_translations as async_get_translations
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import async_get_integration as async_get_integration, bind_hass as bind_hass
from homeassistant.util.hass_dict import HassKey as HassKey
from propcache import cached_property
from typing import Any, TypedDict
from yarl import URL

DOMAIN: str
CONF_THEMES: str
CONF_THEMES_MODES: str
CONF_THEMES_LIGHT: str
CONF_THEMES_DARK: str
CONF_EXTRA_HTML_URL: str
CONF_EXTRA_HTML_URL_ES5: str
CONF_EXTRA_MODULE_URL: str
CONF_EXTRA_JS_URL_ES5: str
CONF_FRONTEND_REPO: str
CONF_JS_VERSION: str
DEFAULT_THEME_COLOR: str
DATA_PANELS: str
DATA_JS_VERSION: str
DATA_EXTRA_MODULE_URL: str
DATA_EXTRA_JS_URL_ES5: str
DATA_WS_SUBSCRIBERS: HassKey[set[tuple[websocket_api.ActiveConnection, int]]]
THEMES_STORAGE_KEY: Incomplete
THEMES_STORAGE_VERSION: int
THEMES_SAVE_DELAY: int
DATA_THEMES_STORE: str
DATA_THEMES: str
DATA_DEFAULT_THEME: str
DATA_DEFAULT_DARK_THEME: str
DEFAULT_THEME: str
VALUE_NO_THEME: str
PRIMARY_COLOR: str
_LOGGER: Incomplete
EXTENDED_THEME_SCHEMA: Incomplete
THEME_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete
SERVICE_SET_THEME: str
SERVICE_RELOAD_THEMES: str

class Manifest:
    manifest: Incomplete
    def __init__(self, data: dict) -> None: ...
    def __getitem__(self, key: str) -> Any: ...
    @property
    def json(self) -> str: ...
    _serialized: Incomplete
    def _serialize(self) -> None: ...
    def update_key(self, key: str, val: str) -> None: ...

MANIFEST_JSON: Incomplete

class UrlManager:
    _on_change: Incomplete
    urls: Incomplete
    def __init__(self, on_change: Callable[[str, str], None], urls: list[str]) -> None: ...
    def add(self, url: str) -> None: ...
    def remove(self, url: str) -> None: ...

class Panel:
    component_name: str
    sidebar_icon: str | None
    sidebar_title: str | None
    frontend_url_path: str | None
    config: dict[str, Any] | None
    require_admin: bool
    config_panel_domain: str | None
    def __init__(self, component_name: str, sidebar_title: str | None, sidebar_icon: str | None, frontend_url_path: str | None, config: dict[str, Any] | None, require_admin: bool, config_panel_domain: str | None) -> None: ...
    @callback
    def to_response(self) -> PanelRespons: ...

@bind_hass
@callback
def async_register_built_in_panel(hass: HomeAssistant, component_name: str, sidebar_title: str | None = None, sidebar_icon: str | None = None, frontend_url_path: str | None = None, config: dict[str, Any] | None = None, require_admin: bool = False, *, update: bool = False, config_panel_domain: str | None = None) -> None: ...
@bind_hass
@callback
def async_remove_panel(hass: HomeAssistant, frontend_url_path: str, *, warn_if_unknown: bool = True) -> None: ...
def add_extra_js_url(hass: HomeAssistant, url: str, es5: bool = False) -> None: ...
def remove_extra_js_url(hass: HomeAssistant, url: str, es5: bool = False) -> None: ...
def add_manifest_json_key(key: str, val: Any) -> None: ...
def _frontend_root(dev_repo_path: str | None) -> pathlib.Path: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def _async_setup_themes(hass: HomeAssistant, themes: dict[str, Any] | None) -> None: ...
@callback
def _async_render_index_cached(template: jinja2.Template, **kwargs: Any) -> str: ...

class IndexView(web_urldispatcher.AbstractResource):
    repo_path: Incomplete
    hass: Incomplete
    _template_cache: jinja2.Template | None
    def __init__(self, repo_path: str | None, hass: HomeAssistant) -> None: ...
    @cached_property
    def canonical(self) -> str: ...
    @cached_property
    def _route(self) -> web_urldispatcher.ResourceRoute: ...
    def url_for(self, **kwargs: str) -> URL: ...
    async def resolve(self, request: web.Request) -> tuple[web_urldispatcher.UrlMappingMatchInfo | None, set[str]]: ...
    def add_prefix(self, prefix: str) -> None: ...
    def get_info(self) -> dict[str, list[str]]: ...
    def raw_match(self, path: str) -> bool: ...
    def get_template(self) -> jinja2.Template: ...
    async def get(self, request: web.Request) -> web.Response: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[web_urldispatcher.ResourceRoute]: ...

class ManifestJSONView(HomeAssistantView):
    requires_auth: bool
    url: str
    name: str
    @callback
    def get(self, request: web.Request) -> web.Response: ...

@websocket_api.async_response
async def websocket_get_icons(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def websocket_get_panels(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def websocket_get_themes(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def websocket_get_translations(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def websocket_get_version(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def websocket_subscribe_extra_js(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...

class PanelRespons(TypedDict):
    component_name: str
    icon: str | None
    title: str | None
    config: dict[str, Any] | None
    url_path: str | None
    require_admin: bool
    config_panel_domain: str | None
