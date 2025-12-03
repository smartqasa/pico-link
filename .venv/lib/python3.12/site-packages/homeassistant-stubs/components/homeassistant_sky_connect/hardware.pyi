from .const import DOMAIN as DOMAIN
from .util import get_hardware_variant as get_hardware_variant
from homeassistant.components.hardware.models import HardwareInfo as HardwareInfo, USBInfo as USBInfo
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

DOCUMENTATION_URL: str

@callback
def async_info(hass: HomeAssistant) -> list[HardwareInfo]: ...
