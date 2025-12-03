from . import subscription as subscription
from .config import MQTT_RW_SCHEMA as MQTT_RW_SCHEMA
from .const import CONF_COMMAND_TEMPLATE as CONF_COMMAND_TEMPLATE, CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_PAYLOAD_RESET as CONF_PAYLOAD_RESET, CONF_STATE_TOPIC as CONF_STATE_TOPIC
from .entity import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import number as number
from homeassistant.components.number import DEFAULT_MAX_VALUE as DEFAULT_MAX_VALUE, DEFAULT_MIN_VALUE as DEFAULT_MIN_VALUE, DEFAULT_STEP as DEFAULT_STEP, NumberDeviceClass as NumberDeviceClass, NumberMode as NumberMode, RestoreNumber as RestoreNumber
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_MODE as CONF_MODE, CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.service_info.mqtt import ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.typing import ConfigType as ConfigType, VolSchemaType as VolSchemaType

_LOGGER: Incomplete
PARALLEL_UPDATES: int
CONF_MIN: str
CONF_MAX: str
CONF_STEP: str
DEFAULT_NAME: str
DEFAULT_PAYLOAD_RESET: str
MQTT_NUMBER_ATTRIBUTES_BLOCKED: Incomplete

def validate_config(config: ConfigType) -> ConfigType: ...

_PLATFORM_SCHEMA_BASE: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttNumber(MqttEntity, RestoreNumber):
    _default_name = DEFAULT_NAME
    _entity_id_format: Incomplete
    _attributes_extra_blocked = MQTT_NUMBER_ATTRIBUTES_BLOCKED
    _optimistic: bool
    _command_template: Callable[[PublishPayloadType], PublishPayloadType]
    _value_template: Callable[[ReceivePayloadType], ReceivePayloadType]
    @staticmethod
    def config_schema() -> VolSchemaType: ...
    _config: Incomplete
    _attr_assumed_state: Incomplete
    _attr_device_class: Incomplete
    _attr_mode: Incomplete
    _attr_native_max_value: Incomplete
    _attr_native_min_value: Incomplete
    _attr_native_step: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def _message_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
