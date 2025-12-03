from . import debug_info as debug_info, discovery as discovery
from .client import MQTT as MQTT, async_publish as async_publish, async_subscribe as async_subscribe, async_subscribe_internal as async_subscribe_internal, publish as publish, subscribe as subscribe
from .config import MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA, MQTT_RO_SCHEMA as MQTT_RO_SCHEMA, MQTT_RW_SCHEMA as MQTT_RW_SCHEMA
from .config_integration import CONFIG_SCHEMA_BASE as CONFIG_SCHEMA_BASE
from .const import ATTR_PAYLOAD as ATTR_PAYLOAD, ATTR_QOS as ATTR_QOS, ATTR_RETAIN as ATTR_RETAIN, ATTR_TOPIC as ATTR_TOPIC, CONF_BIRTH_MESSAGE as CONF_BIRTH_MESSAGE, CONF_BROKER as CONF_BROKER, CONF_CERTIFICATE as CONF_CERTIFICATE, CONF_CLIENT_CERT as CONF_CLIENT_CERT, CONF_CLIENT_KEY as CONF_CLIENT_KEY, CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_DISCOVERY_PREFIX as CONF_DISCOVERY_PREFIX, CONF_KEEPALIVE as CONF_KEEPALIVE, CONF_QOS as CONF_QOS, CONF_STATE_TOPIC as CONF_STATE_TOPIC, CONF_TLS_INSECURE as CONF_TLS_INSECURE, CONF_TOPIC as CONF_TOPIC, CONF_TRANSPORT as CONF_TRANSPORT, CONF_WILL_MESSAGE as CONF_WILL_MESSAGE, CONF_WS_HEADERS as CONF_WS_HEADERS, CONF_WS_PATH as CONF_WS_PATH, DEFAULT_DISCOVERY as DEFAULT_DISCOVERY, DEFAULT_ENCODING as DEFAULT_ENCODING, DEFAULT_PREFIX as DEFAULT_PREFIX, DEFAULT_QOS as DEFAULT_QOS, DEFAULT_RETAIN as DEFAULT_RETAIN, DOMAIN as DOMAIN, ENTITY_PLATFORMS as ENTITY_PLATFORMS, MQTT_CONNECTION_STATE as MQTT_CONNECTION_STATE, TEMPLATE_ERRORS as TEMPLATE_ERRORS
from .models import DATA_MQTT as DATA_MQTT, DATA_MQTT_AVAILABLE as DATA_MQTT_AVAILABLE, MqttCommandTemplate as MqttCommandTemplate, MqttData as MqttData, MqttValueTemplate as MqttValueTemplate, PayloadSentinel as PayloadSentinel, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage, convert_outgoing_mqtt_payload as convert_outgoing_mqtt_payload
from .subscription import EntitySubscription as EntitySubscription, async_prepare_subscribe_topics as async_prepare_subscribe_topics, async_subscribe_topics as async_subscribe_topics, async_unsubscribe_topics as async_unsubscribe_topics
from .util import async_create_certificate_temp_files as async_create_certificate_temp_files, async_forward_entry_setup_and_setup_discovery as async_forward_entry_setup_and_setup_discovery, async_wait_for_mqtt_client as async_wait_for_mqtt_client, mqtt_config_entry_enabled as mqtt_config_entry_enabled, platforms_from_config as platforms_from_config, valid_publish_topic as valid_publish_topic, valid_qos_schema as valid_qos_schema, valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from collections.abc import Callable
from homeassistant.components import websocket_api as websocket_api
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DISCOVERY as CONF_DISCOVERY, CONF_PAYLOAD as CONF_PAYLOAD, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ConfigValidationError as ConfigValidationError, ServiceValidationError as ServiceValidationError, Unauthorized as Unauthorized
from homeassistant.helpers import template as template
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import async_get_platforms as async_get_platforms
from homeassistant.helpers.reload import async_integration_yaml_config as async_integration_yaml_config
from homeassistant.helpers.service import async_register_admin_service as async_register_admin_service
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import async_get_integration as async_get_integration, async_get_loaded_integration as async_get_loaded_integration
from homeassistant.setup import SetupPhases as SetupPhases, async_pause_setup as async_pause_setup
from homeassistant.util.async_ import create_eager_task as create_eager_task
from typing import Any

_LOGGER: Incomplete
SERVICE_PUBLISH: str
SERVICE_DUMP: str
ATTR_TOPIC_TEMPLATE: str
ATTR_PAYLOAD_TEMPLATE: str
ATTR_EVALUATE_PAYLOAD: str
MAX_RECONNECT_WAIT: int
CONNECTION_SUCCESS: str
CONNECTION_FAILED: str
CONNECTION_FAILED_RECOVERABLE: str
CONFIG_SCHEMA: Incomplete
MQTT_PUBLISH_SCHEMA: Incomplete

async def _async_config_entry_updated(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
@callback
def _async_remove_mqtt_issues(hass: HomeAssistant, mqtt_data: MqttData) -> None: ...
async def async_check_config_schema(hass: HomeAssistant, config_yaml: ConfigType) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
@callback
def websocket_mqtt_info(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def websocket_subscribe(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
type ConnectionStatusCallback = Callable[[bool], None]
@callback
def async_subscribe_connection_status(hass: HomeAssistant, connection_status_callback: ConnectionStatusCallback) -> Callable[[], None]: ...
def is_connected(hass: HomeAssistant) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: ConfigEntry, device_entry: DeviceEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
