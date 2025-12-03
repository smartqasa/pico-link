from ..const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.file_upload import process_uploaded_file as process_uploaded_file
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.storage import STORAGE_DIR as STORAGE_DIR
from typing import Final
from xknx.secure.keyring import Keyring as Keyring

_LOGGER: Incomplete
DEFAULT_KNX_KEYRING_FILENAME: Final[str]

async def save_uploaded_knxkeys_file(hass: HomeAssistant, uploaded_file_id: str, password: str) -> Keyring: ...
