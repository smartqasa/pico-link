from _typeshed import Incomplete
from homeassistant.components import frontend as frontend
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType

DOMAIN: str
URL_PATH: str
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
