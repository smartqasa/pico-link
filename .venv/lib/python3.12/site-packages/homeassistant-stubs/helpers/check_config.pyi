from .typing import ConfigType as ConfigType
from collections import OrderedDict
from homeassistant import loader as loader
from homeassistant.config import CONF_PACKAGES as CONF_PACKAGES, YAML_CONFIG_FILE as YAML_CONFIG_FILE, config_per_platform as config_per_platform, extract_domain_configs as extract_domain_configs, format_homeassistant_error as format_homeassistant_error, format_schema_error as format_schema_error, load_yaml_config_file as load_yaml_config_file, merge_packages_config as merge_packages_config
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.core_config import CORE_CONFIG_SCHEMA as CORE_CONFIG_SCHEMA
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.requirements import RequirementsNotFound as RequirementsNotFound, async_clear_install_history as async_clear_install_history, async_get_integration_with_requirements as async_get_integration_with_requirements
from typing import NamedTuple, Self

class CheckConfigError(NamedTuple):
    message: str
    domain: str | None
    config: ConfigType | None

class HomeAssistantConfig(OrderedDict):
    errors: list[CheckConfigError]
    warnings: list[CheckConfigError]
    def __init__(self) -> None: ...
    def add_error(self, message: str, domain: str | None = None, config: ConfigType | None = None) -> Self: ...
    @property
    def error_str(self) -> str: ...
    def add_warning(self, message: str, domain: str | None = None, config: ConfigType | None = None) -> Self: ...
    @property
    def warning_str(self) -> str: ...

async def async_check_ha_config_file(hass: HomeAssistant) -> HomeAssistantConfig: ...
