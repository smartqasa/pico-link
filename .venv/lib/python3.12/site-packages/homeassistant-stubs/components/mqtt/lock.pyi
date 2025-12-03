import re
import voluptuous as vol
from . import subscription as subscription
from .config import MQTT_RW_SCHEMA as MQTT_RW_SCHEMA
from .const import CONF_COMMAND_TEMPLATE as CONF_COMMAND_TEMPLATE, CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_PAYLOAD_RESET as CONF_PAYLOAD_RESET, CONF_STATE_OPEN as CONF_STATE_OPEN, CONF_STATE_OPENING as CONF_STATE_OPENING, CONF_STATE_TOPIC as CONF_STATE_TOPIC
from .entity import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import lock as lock
from homeassistant.components.lock import LockEntity as LockEntity, LockEntityFeature as LockEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_CODE as ATTR_CODE, CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.service_info.mqtt import ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int
CONF_CODE_FORMAT: str
CONF_PAYLOAD_LOCK: str
CONF_PAYLOAD_UNLOCK: str
CONF_PAYLOAD_OPEN: str
CONF_STATE_LOCKED: str
CONF_STATE_LOCKING: str
CONF_STATE_UNLOCKED: str
CONF_STATE_UNLOCKING: str
CONF_STATE_JAMMED: str
DEFAULT_NAME: str
DEFAULT_PAYLOAD_LOCK: str
DEFAULT_PAYLOAD_UNLOCK: str
DEFAULT_PAYLOAD_OPEN: str
DEFAULT_PAYLOAD_RESET: str
DEFAULT_STATE_LOCKED: str
DEFAULT_STATE_LOCKING: str
DEFAULT_STATE_OPEN: str
DEFAULT_STATE_OPENING: str
DEFAULT_STATE_UNLOCKED: str
DEFAULT_STATE_UNLOCKING: str
DEFAULT_STATE_JAMMED: str
MQTT_LOCK_ATTRIBUTES_BLOCKED: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete
STATE_CONFIG_KEYS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttLock(MqttEntity, LockEntity):
    _default_name = DEFAULT_NAME
    _entity_id_format: Incomplete
    _attributes_extra_blocked = MQTT_LOCK_ATTRIBUTES_BLOCKED
    _compiled_pattern: re.Pattern[Any] | None
    _optimistic: bool
    _valid_states: list[str]
    _command_template: Callable[[PublishPayloadType, TemplateVarsType], PublishPayloadType]
    _value_template: Callable[[ReceivePayloadType], ReceivePayloadType]
    @staticmethod
    def config_schema() -> vol.Schema: ...
    _attr_is_locked: bool
    _attr_assumed_state: Incomplete
    _attr_code_format: Incomplete
    _attr_supported_features: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _attr_is_locking: Incomplete
    _attr_is_open: Incomplete
    _attr_is_opening: Incomplete
    _attr_is_unlocking: Incomplete
    _attr_is_jammed: Incomplete
    @callback
    def _message_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    async def async_open(self, **kwargs: Any) -> None: ...
