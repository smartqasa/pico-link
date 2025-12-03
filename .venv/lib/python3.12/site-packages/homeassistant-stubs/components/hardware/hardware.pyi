from .const import DOMAIN as DOMAIN
from .models import HardwareProtocol as HardwareProtocol
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.integration_platform import async_process_integration_platforms as async_process_integration_platforms

async def async_process_hardware_platforms(hass: HomeAssistant) -> None: ...
@callback
def _register_hardware_platform(hass: HomeAssistant, integration_domain: str, platform: HardwareProtocol) -> None: ...
