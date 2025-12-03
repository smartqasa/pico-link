from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.components import blueprint as blueprint
from homeassistant.const import SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.singleton import singleton as singleton

DATA_BLUEPRINTS: str

def _blueprint_in_use(hass: HomeAssistant, blueprint_path: str) -> bool: ...
async def _reload_blueprint_automations(hass: HomeAssistant, blueprint_path: str) -> None: ...
@callback
def async_get_blueprints(hass: HomeAssistant) -> blueprint.DomainBlueprints: ...
