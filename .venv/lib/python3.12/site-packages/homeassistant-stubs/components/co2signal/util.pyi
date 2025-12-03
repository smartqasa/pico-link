from collections.abc import Mapping
from homeassistant.const import CONF_COUNTRY_CODE as CONF_COUNTRY_CODE, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from typing import Any

def get_extra_name(config: Mapping[str, Any]) -> str | None: ...
