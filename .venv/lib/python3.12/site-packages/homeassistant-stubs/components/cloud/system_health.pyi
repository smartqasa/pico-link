from .const import DATA_CLOUD as DATA_CLOUD
from homeassistant.components import system_health as system_health
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

@callback
def async_register(hass: HomeAssistant, register: system_health.SystemHealthRegistration) -> None: ...
async def system_health_info(hass: HomeAssistant) -> dict[str, Any]: ...
