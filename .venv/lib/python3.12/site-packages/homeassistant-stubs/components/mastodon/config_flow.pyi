from .const import CONF_BASE_URL as CONF_BASE_URL, DEFAULT_URL as DEFAULT_URL, DOMAIN as DOMAIN, LOGGER as LOGGER
from .utils import construct_mastodon_username as construct_mastodon_username, create_mastodon_client as create_mastodon_client
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_NAME as CONF_NAME
from homeassistant.helpers.selector import TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from homeassistant.util import slugify as slugify
from typing import Any

STEP_USER_DATA_SCHEMA: Incomplete

def base_url_from_url(url: str) -> str: ...

class MastodonConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    def check_connection(self, base_url: str, client_id: str, client_secret: str, access_token: str) -> tuple[dict[str, str] | None, dict[str, str] | None, dict[str, str]]: ...
    def show_user_form(self, user_input: dict[str, Any] | None = None, errors: dict[str, str] | None = None, description_placeholders: dict[str, str] | None = None, step_id: str = 'user') -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_import(self, import_data: dict[str, Any]) -> ConfigFlowResult: ...
