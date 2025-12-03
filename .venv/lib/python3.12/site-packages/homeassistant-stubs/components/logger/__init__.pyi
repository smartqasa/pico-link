import logging
import re
from . import websocket_api as websocket_api
from .const import ATTR_LEVEL as ATTR_LEVEL, DOMAIN as DOMAIN, LOGGER_DEFAULT as LOGGER_DEFAULT, LOGGER_FILTERS as LOGGER_FILTERS, LOGGER_LOGS as LOGGER_LOGS, LOGSEVERITY as LOGSEVERITY, SERVICE_SET_DEFAULT_LEVEL as SERVICE_SET_DEFAULT_LEVEL, SERVICE_SET_LEVEL as SERVICE_SET_LEVEL
from .helpers import LoggerDomainConfig as LoggerDomainConfig, LoggerSettings as LoggerSettings, set_default_log_level as set_default_log_level, set_log_levels as set_log_levels
from _typeshed import Incomplete
from homeassistant.const import EVENT_LOGGING_CHANGED as EVENT_LOGGING_CHANGED
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.typing import ConfigType as ConfigType

_VALID_LOG_LEVEL: Incomplete
SERVICE_SET_DEFAULT_LEVEL_SCHEMA: Incomplete
SERVICE_SET_LEVEL_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def _add_log_filter(logger: logging.Logger, patterns: list[re.Pattern]) -> None: ...
def _get_logger_class(hass_overrides: dict[str, int]) -> type[logging.Logger]: ...
