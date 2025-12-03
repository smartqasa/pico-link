from . import subscription as subscription
from .config import MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from .const import CONF_COMMAND_TEMPLATE as CONF_COMMAND_TEMPLATE, CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_PAYLOAD_CLOSE as CONF_PAYLOAD_CLOSE, CONF_PAYLOAD_OPEN as CONF_PAYLOAD_OPEN, CONF_PAYLOAD_STOP as CONF_PAYLOAD_STOP, CONF_POSITION_CLOSED as CONF_POSITION_CLOSED, CONF_POSITION_OPEN as CONF_POSITION_OPEN, CONF_RETAIN as CONF_RETAIN, CONF_STATE_CLOSED as CONF_STATE_CLOSED, CONF_STATE_CLOSING as CONF_STATE_CLOSING, CONF_STATE_OPEN as CONF_STATE_OPEN, CONF_STATE_OPENING as CONF_STATE_OPENING, CONF_STATE_TOPIC as CONF_STATE_TOPIC, DEFAULT_OPTIMISTIC as DEFAULT_OPTIMISTIC, DEFAULT_PAYLOAD_CLOSE as DEFAULT_PAYLOAD_CLOSE, DEFAULT_PAYLOAD_OPEN as DEFAULT_PAYLOAD_OPEN, DEFAULT_POSITION_CLOSED as DEFAULT_POSITION_CLOSED, DEFAULT_POSITION_OPEN as DEFAULT_POSITION_OPEN, DEFAULT_RETAIN as DEFAULT_RETAIN, PAYLOAD_NONE as PAYLOAD_NONE
from .entity import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from .util import valid_publish_topic as valid_publish_topic, valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from homeassistant.components import valve as valve
from homeassistant.components.valve import DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA, ValveEntity as ValveEntity, ValveEntityFeature as ValveEntityFeature, ValveState as ValveState
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, VolSchemaType as VolSchemaType
from homeassistant.util.json import JSON_DECODE_EXCEPTIONS as JSON_DECODE_EXCEPTIONS, json_loads as json_loads
from homeassistant.util.percentage import percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage

_LOGGER: Incomplete
PARALLEL_UPDATES: int
CONF_REPORTS_POSITION: str
DEFAULT_NAME: str
MQTT_VALVE_ATTRIBUTES_BLOCKED: Incomplete
NO_POSITION_KEYS: Incomplete
DEFAULTS: Incomplete
RESET_CLOSING_OPENING: str

def _validate_and_add_defaults(config: ConfigType) -> ConfigType: ...

_PLATFORM_SCHEMA_BASE: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttValve(MqttEntity, ValveEntity):
    _attr_is_closed: bool | None
    _attributes_extra_blocked: frozenset[str]
    _default_name = DEFAULT_NAME
    _entity_id_format: str
    _optimistic: bool
    _range: tuple[int, int]
    _tilt_optimistic: bool
    @staticmethod
    def config_schema() -> VolSchemaType: ...
    _attr_reports_position: Incomplete
    _attr_assumed_state: Incomplete
    _value_template: Incomplete
    _command_template: Incomplete
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _attr_is_opening: Incomplete
    _attr_is_closing: Incomplete
    @callback
    def _update_state(self, state: str | None) -> None: ...
    @callback
    def _process_binary_valve_update(self, msg: ReceiveMessage, state_payload: str) -> None: ...
    _attr_current_valve_position: Incomplete
    @callback
    def _process_position_valve_update(self, msg: ReceiveMessage, position_payload: str, state_payload: str) -> None: ...
    @callback
    def _state_message_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def async_open_valve(self) -> None: ...
    async def async_close_valve(self) -> None: ...
    async def async_stop_valve(self) -> None: ...
    async def async_set_valve_position(self, position: int) -> None: ...
