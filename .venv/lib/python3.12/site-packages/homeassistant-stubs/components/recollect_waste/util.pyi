from aiorecollect.client import PickupType as PickupType
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_FRIENDLY_NAME as CONF_FRIENDLY_NAME
from homeassistant.core import callback as callback

@callback
def async_get_pickup_type_names(entry: ConfigEntry, pickup_types: list[PickupType]) -> list[str]: ...
