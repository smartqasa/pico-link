import asyncio
from .client import MQTT as MQTT, Subscription as Subscription
from .const import DOMAIN as DOMAIN, TEMPLATE_ERRORS as TEMPLATE_ERRORS
from .debug_info import TimestampedPublishMessage as TimestampedPublishMessage
from .device_trigger import Trigger as Trigger
from .discovery import MQTTDiscoveryPayload as MQTTDiscoveryPayload
from .tag import MQTTTagScanner as MQTTTagScanner
from _typeshed import Incomplete
from collections import deque
from collections.abc import Callable
from dataclasses import dataclass, field
from enum import StrEnum
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_NAME as ATTR_NAME, Platform as Platform
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError, TemplateError as TemplateError
from homeassistant.helpers import template as template
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.service_info.mqtt import ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, TemplateVarsType as TemplateVarsType, VolSchemaType as VolSchemaType
from homeassistant.util.hass_dict import HassKey as HassKey
from paho.mqtt.client import MQTTMessage as MQTTMessage
from typing import TypedDict

class PayloadSentinel(StrEnum):
    NONE = 'none'
    DEFAULT = 'default'

_LOGGER: Incomplete
ATTR_THIS: str
type PublishPayloadType = str | bytes | int | float | None

def convert_outgoing_mqtt_payload(payload: PublishPayloadType) -> PublishPayloadType: ...

@dataclass
class PublishMessage:
    topic: str
    payload: PublishPayloadType
    qos: int
    retain: bool

@dataclass(slots=True, frozen=True, eq=False)
class ReceiveMessage:
    topic: str
    payload: ReceivePayloadType
    qos: int
    retain: bool
    subscribed_topic: str
    timestamp: float
type MessageCallbackType = Callable[[ReceiveMessage], None]

class SubscriptionDebugInfo(TypedDict):
    messages: deque[ReceiveMessage]
    count: int

class EntityDebugInfo(TypedDict):
    subscriptions: dict[str, SubscriptionDebugInfo]
    discovery_data: DiscoveryInfoType
    transmitted: dict[str, dict[str, deque[TimestampedPublishMessage]]]

class TriggerDebugInfo(TypedDict):
    device_id: str
    discovery_data: DiscoveryInfoType

class PendingDiscovered(TypedDict):
    pending: deque[MQTTDiscoveryPayload]
    unsub: CALLBACK_TYPE

class MqttOriginInfo(TypedDict, total=False):
    name: str
    manufacturer: str
    sw_version: str
    hw_version: str
    support_url: str

class MqttCommandTemplateException(ServiceValidationError):
    _message: str
    translation_domain: Incomplete
    translation_key: str
    translation_placeholders: Incomplete
    def __init__(self, *args: object, base_exception: Exception, command_template: str, value: PublishPayloadType, entity_id: str | None = None) -> None: ...
    def __str__(self) -> str: ...

class MqttCommandTemplate:
    _template_state: template.TemplateStateFromEntityId | None
    _command_template: Incomplete
    _entity: Incomplete
    def __init__(self, command_template: template.Template | None, *, entity: Entity | None = None) -> None: ...
    @callback
    def async_render(self, value: PublishPayloadType = None, variables: TemplateVarsType = None) -> PublishPayloadType: ...

class MqttValueTemplateException(TemplateError):
    _message: str
    def __init__(self, *args: object, base_exception: Exception, value_template: str, default: ReceivePayloadType | PayloadSentinel, payload: ReceivePayloadType, entity_id: str | None = None) -> None: ...
    def __str__(self) -> str: ...

class MqttValueTemplate:
    _template_state: template.TemplateStateFromEntityId | None
    _value_template: Incomplete
    _config_attributes: Incomplete
    _entity: Incomplete
    def __init__(self, value_template: template.Template | None, *, entity: Entity | None = None, config_attributes: TemplateVarsType = None) -> None: ...
    @callback
    def async_render_with_possible_json_value(self, payload: ReceivePayloadType, default: ReceivePayloadType | PayloadSentinel = ..., variables: TemplateVarsType = None) -> ReceivePayloadType: ...

class EntityTopicState:
    subscribe_calls: dict[str, Entity]
    def __init__(self) -> None: ...
    @callback
    def process_write_state_requests(self, msg: MQTTMessage) -> None: ...
    @callback
    def write_state_request(self, entity: Entity) -> None: ...

@dataclass
class MqttData:
    client: MQTT
    config: list[ConfigType]
    debug_info_entities: dict[str, EntityDebugInfo] = field(default_factory=dict)
    debug_info_triggers: dict[tuple[str, str], TriggerDebugInfo] = field(default_factory=dict)
    device_triggers: dict[str, Trigger] = field(default_factory=dict)
    data_config_flow_lock: asyncio.Lock = field(default_factory=asyncio.Lock)
    discovery_already_discovered: set[tuple[str, str]] = field(default_factory=set)
    discovery_pending_discovered: dict[tuple[str, str], PendingDiscovered] = field(default_factory=dict)
    discovery_registry_hooks: dict[tuple[str, str], CALLBACK_TYPE] = field(default_factory=dict)
    discovery_unsubscribe: list[CALLBACK_TYPE] = field(default_factory=list)
    integration_unsubscribe: dict[str, CALLBACK_TYPE] = field(default_factory=dict)
    last_discovery: float = ...
    platforms_loaded: set[Platform | str] = field(default_factory=set)
    reload_dispatchers: list[CALLBACK_TYPE] = field(default_factory=list)
    reload_handlers: dict[str, CALLBACK_TYPE] = field(default_factory=dict)
    reload_schema: dict[str, VolSchemaType] = field(default_factory=dict)
    state_write_requests: EntityTopicState = field(default_factory=EntityTopicState)
    subscriptions_to_restore: set[Subscription] = field(default_factory=set)
    tags: dict[str, dict[str, MQTTTagScanner]] = field(default_factory=dict)

@dataclass(slots=True)
class MqttComponentConfig:
    component: str
    object_id: str
    node_id: str | None
    discovery_payload: MQTTDiscoveryPayload

DATA_MQTT: HassKey[MqttData]
DATA_MQTT_AVAILABLE: HassKey[asyncio.Future[bool]]
