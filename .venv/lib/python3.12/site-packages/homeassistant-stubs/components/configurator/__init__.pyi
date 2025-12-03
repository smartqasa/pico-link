from _typeshed import Incomplete
from collections.abc import Callable
from homeassistant.const import ATTR_ENTITY_PICTURE as ATTR_ENTITY_PICTURE, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME
from homeassistant.core import HassJob as HassJob, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as async_callback
from homeassistant.helpers.entity import async_generate_entity_id as async_generate_entity_id
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.async_ import run_callback_threadsafe as run_callback_threadsafe
from typing import Any

_KEY_INSTANCE: str
DATA_REQUESTS: str
ATTR_CONFIGURE_ID: str
ATTR_DESCRIPTION: str
ATTR_DESCRIPTION_IMAGE: str
ATTR_ERRORS: str
ATTR_FIELDS: str
ATTR_LINK_NAME: str
ATTR_LINK_URL: str
ATTR_SUBMIT_CAPTION: str
DOMAIN: str
ENTITY_ID_FORMAT: Incomplete
SERVICE_CONFIGURE: str
STATE_CONFIGURE: str
STATE_CONFIGURED: str
type ConfiguratorCallback = Callable[[list[dict[str, str]]], None]
CONFIG_SCHEMA: Incomplete

@bind_hass
@async_callback
def async_request_config(hass: HomeAssistant, name: str, callback: ConfiguratorCallback | None = None, description: str | None = None, description_image: str | None = None, submit_caption: str | None = None, fields: list[dict[str, str]] | None = None, link_name: str | None = None, link_url: str | None = None, entity_picture: str | None = None) -> str: ...
@bind_hass
def request_config(hass: HomeAssistant, *args: Any, **kwargs: Any) -> str: ...
@bind_hass
@async_callback
def async_notify_errors(hass: HomeAssistant, request_id: str, error: str) -> None: ...
@bind_hass
def notify_errors(hass: HomeAssistant, request_id: str, error: str) -> None: ...
@bind_hass
@async_callback
def async_request_done(hass: HomeAssistant, request_id: str) -> None: ...
@bind_hass
def request_done(hass: HomeAssistant, request_id: str) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def _get_requests(hass: HomeAssistant) -> dict[str, Configurator]: ...

class Configurator:
    hass: Incomplete
    _cur_id: int
    _requests: dict[str, tuple[str, list[dict[str, str]], ConfiguratorCallback | None]]
    def __init__(self, hass: HomeAssistant) -> None: ...
    @async_callback
    def async_request_config(self, name: str, callback: ConfiguratorCallback | None, description: str | None, submit_caption: str | None, fields: list[dict[str, str]] | None, entity_picture: str | None) -> str: ...
    @async_callback
    def async_notify_errors(self, request_id: str, error: str) -> None: ...
    @async_callback
    def async_request_done(self, request_id: str) -> None: ...
    async def async_handle_service_call(self, call: ServiceCall) -> None: ...
    def _generate_unique_id(self) -> str: ...
    def _validate_request_id(self, request_id: str) -> bool: ...
