from _typeshed import Incomplete
from homeassistant.util.json import json_loads as json_loads
from typing import Any

_LOGGER: Incomplete

def parse_json_attributes(value: str | None, json_attrs: list[str], json_attrs_path: str | None) -> dict[str, Any]: ...
