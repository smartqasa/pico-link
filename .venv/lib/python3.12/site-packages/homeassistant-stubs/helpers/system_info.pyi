from .hassio import is_hassio as is_hassio
from .importlib import async_import_module as async_import_module
from .singleton import singleton as singleton
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.package import is_docker_env as is_docker_env, is_virtual_env as is_virtual_env
from homeassistant.util.system_info import is_official_image as is_official_image
from typing import Any

_LOGGER: Incomplete
_DATA_MAC_VER: str

async def async_get_mac_ver(hass: HomeAssistant) -> str: ...

cached_get_user: Incomplete

@bind_hass
async def async_get_system_info(hass: HomeAssistant) -> dict[str, Any]: ...
