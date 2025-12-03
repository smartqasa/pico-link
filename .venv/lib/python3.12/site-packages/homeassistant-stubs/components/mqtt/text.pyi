import re
from . import subscription as subscription
from .config import MQTT_RW_SCHEMA as MQTT_RW_SCHEMA
from .const import CONF_COMMAND_TEMPLATE as CONF_COMMAND_TEMPLATE, CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_STATE_TOPIC as CONF_STATE_TOPIC
from .entity import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from .util import check_state_too_long as check_state_too_long
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import text as text
from homeassistant.components.text import TextEntity as TextEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_MODE as CONF_MODE, CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, MAX_LENGTH_STATE_STATE as MAX_LENGTH_STATE_STATE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.service_info.mqtt import ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.typing import ConfigType as ConfigType, VolSchemaType as VolSchemaType
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int
CONF_MAX: str
CONF_MIN: str
CONF_PATTERN: str
DEFAULT_NAME: str
DEFAULT_PAYLOAD_RESET: str
MQTT_TEXT_ATTRIBUTES_BLOCKED: Incomplete

def valid_text_size_configuration(config: ConfigType) -> ConfigType: ...

_PLATFORM_SCHEMA_BASE: Incomplete
DISCOVERY_SCHEMA: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttTextEntity(MqttEntity, TextEntity):
    _attr_native_value: str | None
    _attributes_extra_blocked = MQTT_TEXT_ATTRIBUTES_BLOCKED
    _default_name = DEFAULT_NAME
    _entity_id_format: Incomplete
    _compiled_pattern: re.Pattern[Any] | None
    _optimistic: bool
    _command_template: Callable[[PublishPayloadType], PublishPayloadType]
    _value_template: Callable[[ReceivePayloadType], ReceivePayloadType]
    @staticmethod
    def config_schema() -> VolSchemaType: ...
    _attr_native_max: Incomplete
    _attr_native_min: Incomplete
    _attr_mode: Incomplete
    _attr_pattern: Incomplete
    _attr_assumed_state: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    @callback
    def _handle_state_message_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def async_set_value(self, value: str) -> None: ...
