from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET
from homeassistant.core import callback as callback
from typing import Any

STORAGE_ACCESS_TOKEN: str
STORAGE_REFRESH_TOKEN: str
TO_REDACT_LWA: Incomplete
TO_REDACT_AUTH: Incomplete

@callback
def async_redact_lwa_params(lwa_params: dict[str, str]) -> dict[str, str]: ...
@callback
def async_redact_auth_data(mapping: Mapping[Any, Any]) -> dict[str, str]: ...
