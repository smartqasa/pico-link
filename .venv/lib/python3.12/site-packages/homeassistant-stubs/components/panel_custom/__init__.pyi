from _typeshed import Incomplete
from homeassistant.components import frontend as frontend
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass

_LOGGER: Incomplete
DOMAIN: str
CONF_COMPONENT_NAME: str
CONF_SIDEBAR_TITLE: str
CONF_SIDEBAR_ICON: str
CONF_URL_PATH: str
CONF_CONFIG: str
CONF_JS_URL: str
CONF_MODULE_URL: str
CONF_EMBED_IFRAME: str
CONF_TRUST_EXTERNAL_SCRIPT: str
CONF_URL_EXCLUSIVE_GROUP: str
CONF_REQUIRE_ADMIN: str
DEFAULT_EMBED_IFRAME: bool
DEFAULT_TRUST_EXTERNAL: bool
DEFAULT_ICON: str
LEGACY_URL: str
PANEL_DIR: str
CONFIG_SCHEMA: Incomplete

@bind_hass
async def async_register_panel(hass: HomeAssistant, frontend_url_path: str, webcomponent_name: str, sidebar_title: str | None = None, sidebar_icon: str | None = None, js_url: str | None = None, module_url: str | None = None, embed_iframe: bool = ..., trust_external: bool = ..., config: ConfigType | None = None, require_admin: bool = False, config_panel_domain: str | None = None) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
