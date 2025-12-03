from . import subscription as subscription
from .config import MQTT_RO_SCHEMA as MQTT_RO_SCHEMA
from .const import CONF_STATE_TOPIC as CONF_STATE_TOPIC, PAYLOAD_EMPTY_JSON as PAYLOAD_EMPTY_JSON, PAYLOAD_NONE as PAYLOAD_NONE
from .entity import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import DATA_MQTT as DATA_MQTT, MqttValueTemplate as MqttValueTemplate, MqttValueTemplateException as MqttValueTemplateException, PayloadSentinel as PayloadSentinel, ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import event as event
from homeassistant.components.event import ENTITY_ID_FORMAT as ENTITY_ID_FORMAT, EventDeviceClass as EventDeviceClass, EventEntity as EventEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_NAME as CONF_NAME, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.service_info.mqtt import ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.typing import ConfigType as ConfigType, VolSchemaType as VolSchemaType
from homeassistant.util.json import JSON_DECODE_EXCEPTIONS as JSON_DECODE_EXCEPTIONS, json_loads_object as json_loads_object

_LOGGER: Incomplete
PARALLEL_UPDATES: int
CONF_EVENT_TYPES: str
MQTT_EVENT_ATTRIBUTES_BLOCKED: Incomplete
DEFAULT_NAME: str
DEFAULT_FORCE_UPDATE: bool
DEVICE_CLASS_SCHEMA: Incomplete
_PLATFORM_SCHEMA_BASE: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttEvent(MqttEntity, EventEntity):
    _default_name = DEFAULT_NAME
    _entity_id_format = ENTITY_ID_FORMAT
    _attributes_extra_blocked = MQTT_EVENT_ATTRIBUTES_BLOCKED
    _template: Callable[[ReceivePayloadType, PayloadSentinel], ReceivePayloadType]
    @staticmethod
    def config_schema() -> VolSchemaType: ...
    _attr_device_class: Incomplete
    _attr_event_types: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    @callback
    def _event_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
