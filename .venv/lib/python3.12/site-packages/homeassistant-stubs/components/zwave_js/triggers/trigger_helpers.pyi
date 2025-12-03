from ..const import ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID, DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.typing import ConfigType as ConfigType

@callback
def async_bypass_dynamic_config_validation(hass: HomeAssistant, config: ConfigType) -> bool: ...
