from .abbreviations import ABBREVIATIONS as ABBREVIATIONS, DEVICE_ABBREVIATIONS as DEVICE_ABBREVIATIONS, ORIGIN_ABBREVIATIONS as ORIGIN_ABBREVIATIONS
from .client import async_subscribe_internal as async_subscribe_internal
from .const import ATTR_DISCOVERY_HASH as ATTR_DISCOVERY_HASH, ATTR_DISCOVERY_PAYLOAD as ATTR_DISCOVERY_PAYLOAD, ATTR_DISCOVERY_TOPIC as ATTR_DISCOVERY_TOPIC, CONF_AVAILABILITY as CONF_AVAILABILITY, CONF_COMPONENTS as CONF_COMPONENTS, CONF_ORIGIN as CONF_ORIGIN, CONF_TOPIC as CONF_TOPIC, DOMAIN as DOMAIN, SUPPORTED_COMPONENTS as SUPPORTED_COMPONENTS
from .models import DATA_MQTT as DATA_MQTT, MqttComponentConfig as MqttComponentConfig, MqttOriginInfo as MqttOriginInfo, ReceiveMessage as ReceiveMessage
from .schemas import DEVICE_DISCOVERY_SCHEMA as DEVICE_DISCOVERY_SCHEMA, MQTT_ORIGIN_INFO_SCHEMA as MQTT_ORIGIN_INFO_SCHEMA, SHARED_OPTIONS as SHARED_OPTIONS
from .util import async_forward_entry_setup_and_setup_discovery as async_forward_entry_setup_and_setup_discovery
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_MQTT as SOURCE_MQTT, signal_discovered_config_entry_removed as signal_discovered_config_entry_removed
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import HassJobType as HassJobType, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import discovery_flow as discovery_flow
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.service_info.mqtt import MqttServiceInfo as MqttServiceInfo, ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from homeassistant.loader import async_get_mqtt as async_get_mqtt
from homeassistant.util.json import json_loads_object as json_loads_object
from homeassistant.util.signal_type import SignalTypeFormat as SignalTypeFormat
from typing import Any

ABBREVIATIONS_SET: Incomplete
DEVICE_ABBREVIATIONS_SET: Incomplete
ORIGIN_ABBREVIATIONS_SET: Incomplete
_LOGGER: Incomplete
TOPIC_MATCHER: Incomplete
MQTT_DISCOVERY_UPDATED: SignalTypeFormat[MQTTDiscoveryPayload]
MQTT_DISCOVERY_NEW: SignalTypeFormat[MQTTDiscoveryPayload]
MQTT_DISCOVERY_DONE: SignalTypeFormat[Any]
TOPIC_BASE: str
CONF_MIGRATE_DISCOVERY: str
MIGRATE_DISCOVERY_SCHEMA: Incomplete

class MQTTDiscoveryPayload(dict[str, Any]):
    device_discovery: bool
    migrate_discovery: bool
    discovery_data: DiscoveryInfoType

@dataclass(frozen=True)
class MQTTIntegrationDiscoveryConfig:
    integration: str
    msg: ReceiveMessage

@callback
def _async_process_discovery_migration(payload: MQTTDiscoveryPayload) -> bool: ...
def clear_discovery_hash(hass: HomeAssistant, discovery_hash: tuple[str, str]) -> None: ...
def set_discovery_hash(hass: HomeAssistant, discovery_hash: tuple[str, str]) -> None: ...
@callback
def get_origin_log_string(discovery_payload: MQTTDiscoveryPayload, *, include_url: bool) -> str: ...
@callback
def get_origin_support_url(discovery_payload: MQTTDiscoveryPayload) -> str | None: ...
@callback
def async_log_discovery_origin_info(message: str, discovery_payload: MQTTDiscoveryPayload, level: int = ...) -> None: ...
@callback
def _replace_abbreviations(payload: dict[str, Any] | str, abbreviations: dict[str, str], abbreviations_set: set[str]) -> None: ...
@callback
def _replace_all_abbreviations(discovery_payload: dict[str, Any], component_only: bool = False) -> None: ...
@callback
def _replace_topic_base(discovery_payload: MQTTDiscoveryPayload) -> None: ...
@callback
def _generate_device_config(hass: HomeAssistant, object_id: str, node_id: str | None, migrate_discovery: bool = False) -> MQTTDiscoveryPayload: ...
@callback
def _parse_device_payload(hass: HomeAssistant, payload: ReceivePayloadType, object_id: str, node_id: str | None) -> MQTTDiscoveryPayload: ...
@callback
def _valid_origin_info(discovery_payload: MQTTDiscoveryPayload) -> bool: ...
@callback
def _merge_common_device_options(component_config: MQTTDiscoveryPayload, device_config: dict[str, Any]) -> None: ...
async def async_start(hass: HomeAssistant, discovery_topic: str, config_entry: ConfigEntry) -> None: ...
async def async_stop(hass: HomeAssistant) -> None: ...
