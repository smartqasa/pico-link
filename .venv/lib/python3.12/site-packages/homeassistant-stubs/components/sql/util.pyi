from .const import DB_URL_RE as DB_URL_RE
from _typeshed import Incomplete
from homeassistant.components.recorder import get_instance as get_instance
from homeassistant.core import HomeAssistant as HomeAssistant

_LOGGER: Incomplete

def redact_credentials(data: str | None) -> str: ...
def resolve_db_url(hass: HomeAssistant, db_url: str | None) -> str: ...
