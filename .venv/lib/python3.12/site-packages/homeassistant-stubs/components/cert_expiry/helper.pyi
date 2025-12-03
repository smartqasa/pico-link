import datetime
from .const import TIMEOUT as TIMEOUT
from .errors import ConnectionRefused as ConnectionRefused, ConnectionTimeout as ConnectionTimeout, ResolveFailed as ResolveFailed, ValidationFailure as ValidationFailure
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.util.ssl import get_default_context as get_default_context
from typing import Any

async def async_get_cert(hass: HomeAssistant, host: str, port: int) -> dict[str, Any]: ...
async def get_cert_expiry_timestamp(hass: HomeAssistant, hostname: str, port: int) -> datetime.datetime: ...
