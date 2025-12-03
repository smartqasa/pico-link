from .const import ATTR_BLOCKS as ATTR_BLOCKS, ATTR_BLOCKS_TEMPLATE as ATTR_BLOCKS_TEMPLATE, ATTR_FILE as ATTR_FILE, ATTR_PASSWORD as ATTR_PASSWORD, ATTR_PATH as ATTR_PATH, ATTR_THREAD_TS as ATTR_THREAD_TS, ATTR_URL as ATTR_URL, ATTR_USERNAME as ATTR_USERNAME, CONF_DEFAULT_CHANNEL as CONF_DEFAULT_CHANNEL, DATA_CLIENT as DATA_CLIENT, SLACK_DATA as SLACK_DATA
from _typeshed import Incomplete
from aiohttp import BasicAuth
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_TARGET as ATTR_TARGET, ATTR_TITLE as ATTR_TITLE, BaseNotificationService as BaseNotificationService
from homeassistant.const import ATTR_ICON as ATTR_ICON, CONF_PATH as CONF_PATH
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import aiohttp_client as aiohttp_client, template as template
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from slack import WebClient as WebClient
from typing import Any, TypedDict

_LOGGER: Incomplete
FILE_PATH_SCHEMA: Incomplete
FILE_URL_SCHEMA: Incomplete
DATA_FILE_SCHEMA: Incomplete
DATA_TEXT_ONLY_SCHEMA: Incomplete
DATA_SCHEMA: Incomplete

class AuthDictT(TypedDict, total=False):
    auth: BasicAuth

class FormDataT(TypedDict, total=False):
    channels: str
    filename: str
    initial_comment: str
    title: str
    token: str
    thread_ts: str

class MessageT(TypedDict, total=False):
    link_names: bool
    text: str
    username: str
    icon_url: str
    icon_emoji: str
    blocks: list[Any]
    thread_ts: str

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> SlackNotificationService | None: ...
@callback
def _async_get_filename_from_url(url: str) -> str: ...
@callback
def _async_sanitize_channel_names(channel_list: list[str]) -> list[str]: ...

class SlackNotificationService(BaseNotificationService):
    _hass: Incomplete
    _client: Incomplete
    _config: Incomplete
    def __init__(self, hass: HomeAssistant, client: WebClient, config: dict[str, str]) -> None: ...
    async def _async_send_local_file_message(self, path: str, targets: list[str], message: str, title: str | None, thread_ts: str | None) -> None: ...
    async def _async_send_remote_file_message(self, url: str, targets: list[str], message: str, title: str | None, thread_ts: str | None, *, username: str | None = None, password: str | None = None) -> None: ...
    async def _async_send_text_only_message(self, targets: list[str], message: str, title: str | None, thread_ts: str | None, *, username: str | None = None, icon: str | None = None, blocks: Any | None = None) -> None: ...
    async def async_send_message(self, message: str, **kwargs: Any) -> None: ...
