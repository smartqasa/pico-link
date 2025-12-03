from .const import ATTR_EVENT_TYPE as ATTR_EVENT_TYPE, ATTR_FACE_URL as ATTR_FACE_URL, ATTR_HOME_ID as ATTR_HOME_ID, ATTR_IS_KNOWN as ATTR_IS_KNOWN, ATTR_PERSONS as ATTR_PERSONS, DATA_DEVICE_IDS as DATA_DEVICE_IDS, DATA_PERSONS as DATA_PERSONS, DEFAULT_PERSON as DEFAULT_PERSON, DOMAIN as DOMAIN, EVENT_ID_MAP as EVENT_ID_MAP, NETATMO_EVENT as NETATMO_EVENT
from _typeshed import Incomplete
from aiohttp.web import Request as Request
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ID as ATTR_ID, ATTR_NAME as ATTR_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send

_LOGGER: Incomplete
SUBEVENT_TYPE_MAP: Incomplete

async def async_handle_webhook(hass: HomeAssistant, webhook_id: str, request: Request) -> None: ...
def async_evaluate_event(hass: HomeAssistant, event_data: dict) -> None: ...
def async_send_event(hass: HomeAssistant, event_type: str, data: dict) -> None: ...
