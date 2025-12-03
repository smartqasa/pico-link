from .const import DOMAIN as DOMAIN, UPLOAD_SCOPE as UPLOAD_SCOPE
from .types import GooglePhotosConfigEntry as GooglePhotosConfigEntry
from _typeshed import Incomplete
from homeassistant.const import CONF_FILENAME as CONF_FILENAME
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError

CONF_CONFIG_ENTRY_ID: str
CONF_ALBUM: str
UPLOAD_SERVICE: str
UPLOAD_SERVICE_SCHEMA: Incomplete
CONTENT_SIZE_LIMIT: Incomplete

def _read_file_contents(hass: HomeAssistant, filenames: list[str]) -> list[tuple[str, bytes]]: ...
def async_register_services(hass: HomeAssistant) -> None: ...
