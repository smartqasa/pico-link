from .const import CONF_ENCODING as CONF_ENCODING, CONF_PAYLOAD_TEMPLATE as CONF_PAYLOAD_TEMPLATE, CONF_SSL_CIPHER_LIST as CONF_SSL_CIPHER_LIST, COORDINATOR as COORDINATOR, DEFAULT_SSL_CIPHER_LIST as DEFAULT_SSL_CIPHER_LIST, DOMAIN as DOMAIN, PLATFORM_IDX as PLATFORM_IDX, REST as REST, REST_DATA as REST_DATA, REST_IDX as REST_IDX
from .data import RestData as RestData
from .schema import CONFIG_SCHEMA as CONFIG_SCHEMA, RESOURCE_SCHEMA as RESOURCE_SCHEMA
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.const import CONF_AUTHENTICATION as CONF_AUTHENTICATION, CONF_HEADERS as CONF_HEADERS, CONF_METHOD as CONF_METHOD, CONF_PARAMS as CONF_PARAMS, CONF_PASSWORD as CONF_PASSWORD, CONF_PAYLOAD as CONF_PAYLOAD, CONF_RESOURCE as CONF_RESOURCE, CONF_RESOURCE_TEMPLATE as CONF_RESOURCE_TEMPLATE, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_TIMEOUT as CONF_TIMEOUT, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, HTTP_DIGEST_AUTHENTICATION as HTTP_DIGEST_AUTHENTICATION, Platform as Platform, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import discovery as discovery, template as template
from homeassistant.helpers.entity_component import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL
from homeassistant.helpers.reload import async_integration_yaml_config as async_integration_yaml_config, async_reload_integration_platforms as async_reload_integration_platforms
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from homeassistant.util.async_ import create_eager_task as create_eager_task

_LOGGER: Incomplete
PLATFORMS: Incomplete
COORDINATOR_AWARE_PLATFORMS: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
@callback
def _async_setup_shared_data(hass: HomeAssistant) -> None: ...
async def _async_process_config(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_get_config_and_coordinator(hass: HomeAssistant, platform_domain: str, discovery_info: DiscoveryInfoType) -> tuple[ConfigType, DataUpdateCoordinator[None], RestData]: ...
def _rest_coordinator(hass: HomeAssistant, rest: RestData, resource_template: template.Template | None, payload_template: template.Template | None, update_interval: timedelta) -> DataUpdateCoordinator[None]: ...
def create_rest_data_from_config(hass: HomeAssistant, config: ConfigType) -> RestData: ...
