from .const import CONF_DOWNLOAD_DIR as CONF_DOWNLOAD_DIR, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, _LOGGER as _LOGGER
from homeassistant import exceptions as exceptions
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from typing import Any

class DownloaderConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _validate_input(self, user_input: dict[str, Any]) -> None: ...

class DirectoryDoesNotExist(exceptions.HomeAssistantError): ...
