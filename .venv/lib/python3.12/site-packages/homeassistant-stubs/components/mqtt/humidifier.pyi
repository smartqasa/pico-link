from . import subscription as subscription
from .config import MQTT_RW_SCHEMA as MQTT_RW_SCHEMA
from .const import CONF_ACTION_TEMPLATE as CONF_ACTION_TEMPLATE, CONF_ACTION_TOPIC as CONF_ACTION_TOPIC, CONF_COMMAND_TEMPLATE as CONF_COMMAND_TEMPLATE, CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_CURRENT_HUMIDITY_TEMPLATE as CONF_CURRENT_HUMIDITY_TEMPLATE, CONF_CURRENT_HUMIDITY_TOPIC as CONF_CURRENT_HUMIDITY_TOPIC, CONF_STATE_TOPIC as CONF_STATE_TOPIC, CONF_STATE_VALUE_TEMPLATE as CONF_STATE_VALUE_TEMPLATE, PAYLOAD_NONE as PAYLOAD_NONE
from .entity import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from .util import valid_publish_topic as valid_publish_topic, valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import humidifier as humidifier
from homeassistant.components.humidifier import ATTR_ACTION as ATTR_ACTION, ATTR_CURRENT_HUMIDITY as ATTR_CURRENT_HUMIDITY, ATTR_HUMIDITY as ATTR_HUMIDITY, ATTR_MODE as ATTR_MODE, DEFAULT_MAX_HUMIDITY as DEFAULT_MAX_HUMIDITY, DEFAULT_MIN_HUMIDITY as DEFAULT_MIN_HUMIDITY, HumidifierAction as HumidifierAction, HumidifierDeviceClass as HumidifierDeviceClass, HumidifierEntity as HumidifierEntity, HumidifierEntityFeature as HumidifierEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_PAYLOAD_OFF as CONF_PAYLOAD_OFF, CONF_PAYLOAD_ON as CONF_PAYLOAD_ON, CONF_STATE as CONF_STATE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.service_info.mqtt import ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import ConfigType as ConfigType, VolSchemaType as VolSchemaType
from typing import Any

PARALLEL_UPDATES: int
CONF_AVAILABLE_MODES_LIST: str
CONF_DEVICE_CLASS: str
CONF_MODE_COMMAND_TEMPLATE: str
CONF_MODE_COMMAND_TOPIC: str
CONF_MODE_STATE_TOPIC: str
CONF_MODE_STATE_TEMPLATE: str
CONF_PAYLOAD_RESET_MODE: str
CONF_PAYLOAD_RESET_HUMIDITY: str
CONF_TARGET_HUMIDITY_COMMAND_TEMPLATE: str
CONF_TARGET_HUMIDITY_COMMAND_TOPIC: str
CONF_TARGET_HUMIDITY_MIN: str
CONF_TARGET_HUMIDITY_MAX: str
CONF_TARGET_HUMIDITY_STATE_TEMPLATE: str
CONF_TARGET_HUMIDITY_STATE_TOPIC: str
DEFAULT_NAME: str
DEFAULT_PAYLOAD_ON: str
DEFAULT_PAYLOAD_OFF: str
DEFAULT_PAYLOAD_RESET: str
MQTT_HUMIDIFIER_ATTRIBUTES_BLOCKED: Incomplete
_LOGGER: Incomplete

def valid_mode_configuration(config: ConfigType) -> ConfigType: ...
def valid_humidity_range_configuration(config: ConfigType) -> ConfigType: ...

_PLATFORM_SCHEMA_BASE: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete
TOPICS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttHumidifier(MqttEntity, HumidifierEntity):
    _attr_mode: str | None
    _default_name = DEFAULT_NAME
    _entity_id_format: Incomplete
    _attributes_extra_blocked = MQTT_HUMIDIFIER_ATTRIBUTES_BLOCKED
    _command_templates: dict[str, Callable[[PublishPayloadType], PublishPayloadType]]
    _value_templates: dict[str, Callable[[ReceivePayloadType], ReceivePayloadType]]
    _optimistic: bool
    _optimistic_target_humidity: bool
    _optimistic_mode: bool
    _payload: dict[str, str]
    _topic: dict[str, Any]
    @staticmethod
    def config_schema() -> VolSchemaType: ...
    _attr_device_class: Incomplete
    _attr_min_humidity: Incomplete
    _attr_max_humidity: Incomplete
    _attr_available_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_assumed_state: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _attr_is_on: bool
    @callback
    def _state_received(self, msg: ReceiveMessage) -> None: ...
    _attr_action: Incomplete
    @callback
    def _action_received(self, msg: ReceiveMessage) -> None: ...
    _attr_current_humidity: Incomplete
    @callback
    def _current_humidity_received(self, msg: ReceiveMessage) -> None: ...
    _attr_target_humidity: Incomplete
    @callback
    def _target_humidity_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _mode_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_humidity(self, humidity: float) -> None: ...
    async def async_set_mode(self, mode: str) -> None: ...
