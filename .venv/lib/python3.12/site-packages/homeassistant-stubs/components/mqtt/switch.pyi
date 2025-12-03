import voluptuous as vol
from . import subscription as subscription
from .config import MQTT_RW_SCHEMA as MQTT_RW_SCHEMA
from .const import CONF_COMMAND_TEMPLATE as CONF_COMMAND_TEMPLATE, CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_STATE_TOPIC as CONF_STATE_TOPIC, PAYLOAD_NONE as PAYLOAD_NONE
from .entity import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import switch as switch
from homeassistant.components.switch import DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA, SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_PAYLOAD_OFF as CONF_PAYLOAD_OFF, CONF_PAYLOAD_ON as CONF_PAYLOAD_ON, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.service_info.mqtt import ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

PARALLEL_UPDATES: int
DEFAULT_NAME: str
DEFAULT_PAYLOAD_ON: str
DEFAULT_PAYLOAD_OFF: str
CONF_STATE_ON: str
CONF_STATE_OFF: str
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttSwitch(MqttEntity, SwitchEntity, RestoreEntity):
    _default_name = DEFAULT_NAME
    _entity_id_format: Incomplete
    _optimistic: bool
    _is_on_map: dict[str | bytes | bytearray, bool | None]
    _command_template: Callable[[PublishPayloadType], PublishPayloadType]
    _value_template: Callable[[ReceivePayloadType], ReceivePayloadType]
    @staticmethod
    def config_schema() -> vol.Schema: ...
    _attr_device_class: Incomplete
    _attr_assumed_state: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def _state_message_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
