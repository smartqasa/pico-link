from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant import core as core, loader as loader
from homeassistant.config import get_default_config_dir as get_default_config_dir
from homeassistant.config_entries import ConfigEntries as ConfigEntries
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.check_config import async_check_ha_config_file as async_check_ha_config_file
from homeassistant.util.yaml import Secrets as Secrets
from typing import Any

REQUIREMENTS: Incomplete
_LOGGER: Incomplete
MOCKS: dict[str, tuple[str, Callable]]
PATCHES: dict[str, Any]
C_HEAD: str
ERROR_STR: str
WARNING_STR: str

def color(the_color, *args, reset: Incomplete | None = None): ...
def run(script_args: list) -> int: ...
def check(config_dir, secrets: bool = False): ...
async def async_check_config(config_dir): ...
def line_info(obj, **kwargs): ...
def dump_dict(layer, indent_count: int = 3, listi: bool = False, **kwargs): ...
