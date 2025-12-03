from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from zwave_js_server.model.value import ConfigurationValue as ConfigurationValue

NODE_STATUSES: Incomplete
CONF_SUBTYPE: str
CONF_VALUE_ID: str
VALUE_ID_REGEX: str

def generate_config_parameter_subtype(config_value: ConfigurationValue) -> str: ...
@callback
def async_bypass_dynamic_config_validation(hass: HomeAssistant, device_id: str) -> bool: ...
