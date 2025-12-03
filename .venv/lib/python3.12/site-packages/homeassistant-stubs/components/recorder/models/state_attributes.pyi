from _typeshed import Incomplete
from homeassistant.util.json import json_loads_object as json_loads_object
from typing import Any

EMPTY_JSON_OBJECT: str
_LOGGER: Incomplete

def decode_attributes_from_source(source: Any, attr_cache: dict[str, dict[str, Any]]) -> dict[str, Any]: ...
