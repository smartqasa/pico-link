import logging
from .const import DOMAIN as DOMAIN, LOGGER_DEFAULT as LOGGER_DEFAULT, LOGGER_LOGS as LOGGER_LOGS, LOGSEVERITY as LOGSEVERITY, LOGSEVERITY_NOTSET as LOGSEVERITY_NOTSET, STORAGE_KEY as STORAGE_KEY, STORAGE_LOG_KEY as STORAGE_LOG_KEY, STORAGE_VERSION as STORAGE_VERSION
from _typeshed import Incomplete
from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.const import EVENT_LOGGING_CHANGED as EVENT_LOGGING_CHANGED
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import IntegrationNotFound as IntegrationNotFound, async_get_integration as async_get_integration
from typing import Any

SAVE_DELAY: float
SAVE_DELAY_LONG: float

@callback
def async_get_domain_config(hass: HomeAssistant) -> LoggerDomainConfig: ...
@callback
def set_default_log_level(hass: HomeAssistant, level: int) -> None: ...
@callback
def set_log_levels(hass: HomeAssistant, logpoints: Mapping[str, int]) -> None: ...
def _set_log_level(logger: logging.Logger, level: int) -> None: ...
def _chattiest_log_level(level1: int, level2: int) -> int: ...
async def get_integration_loggers(hass: HomeAssistant, domain: str) -> set[str]: ...

@dataclass(slots=True)
class LoggerSetting:
    level: str
    persistence: str
    type: str

@dataclass(slots=True)
class LoggerDomainConfig:
    overrides: dict[str, Any]
    settings: LoggerSettings

class LogPersistance(StrEnum):
    NONE = 'none'
    ONCE = 'once'
    PERMANENT = 'permanent'

class LogSettingsType(StrEnum):
    INTEGRATION = 'integration'
    MODULE = 'module'

class LoggerSettings:
    _stored_config: dict[str, dict[str, LoggerSetting]]
    _yaml_config: Incomplete
    _default_level: Incomplete
    _store: Store[dict[str, dict[str, dict[str, Any]]]]
    def __init__(self, hass: HomeAssistant, yaml_config: ConfigType) -> None: ...
    async def async_load(self) -> None: ...
    @callback
    def _async_data_to_save(self) -> dict[str, dict[str, dict[str, str]]]: ...
    @callback
    def async_save(self, delay: float = ...) -> None: ...
    @callback
    def _async_get_logger_logs(self) -> dict[str, int]: ...
    async def async_update(self, hass: HomeAssistant, domain: str, settings: LoggerSetting) -> None: ...
    async def async_get_levels(self, hass: HomeAssistant) -> dict[str, int]: ...

get_logger: Incomplete
