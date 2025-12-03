from .const import CONF_OVERRIDE_MQTT_URL as CONF_OVERRIDE_MQTT_URL, CONF_OVERRIDE_REST_URL as CONF_OVERRIDE_REST_URL, CONF_VERIFY_MQTT_CERTIFICATE as CONF_VERIFY_MQTT_CERTIFICATE, DOMAIN as DOMAIN, InstanceMode as InstanceMode
from .util import get_client_device_id as get_client_device_id
from _typeshed import Incomplete
from deebot_client.const import UndefinedType as UndefinedType
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_COUNTRY as CONF_COUNTRY, CONF_MODE as CONF_MODE, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client, selector as selector
from homeassistant.helpers.typing import VolDictType as VolDictType
from homeassistant.util.ssl import get_default_no_verify_context as get_default_no_verify_context
from typing import Any

_LOGGER: Incomplete

def _validate_url(value: str, field_name: str, schema_list: set[str]) -> dict[str, str]: ...
async def _validate_input(hass: HomeAssistant, user_input: dict[str, Any]) -> dict[str, str]: ...

class EcovacsConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _mode: InstanceMode
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_auth(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
