import voluptuous as vol
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_TOKEN as CONF_TOKEN

CONFIG_SCHEMA: Incomplete

def get_config_schema_with_default_host(host: str) -> vol.Schema: ...
