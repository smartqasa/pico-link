from .const import DOMAIN as DOMAIN
from homeassistant.components.hardware.models import BoardInfo as BoardInfo, HardwareInfo as HardwareInfo
from homeassistant.components.hassio import get_os_info as get_os_info
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

BOARD_NAME: str
DOCUMENTATION_URL: str
MANUFACTURER: str
MODEL: str

@callback
def async_info(hass: HomeAssistant) -> list[HardwareInfo]: ...
