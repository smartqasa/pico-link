from . import subscription as subscription
from .config import MQTT_RW_SCHEMA as MQTT_RW_SCHEMA
from .const import CONF_COMMAND_TEMPLATE as CONF_COMMAND_TEMPLATE, CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_OPTIONS as CONF_OPTIONS, CONF_STATE_TOPIC as CONF_STATE_TOPIC
from .entity import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import select as select
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.service_info.mqtt import ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.typing import ConfigType as ConfigType, VolSchemaType as VolSchemaType

_LOGGER: Incomplete
PARALLEL_UPDATES: int
DEFAULT_NAME: str
MQTT_SELECT_ATTRIBUTES_BLOCKED: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttSelect(MqttEntity, SelectEntity, RestoreEntity):
    _attr_current_option: str | None
    _default_name = DEFAULT_NAME
    _entity_id_format: Incomplete
    _attributes_extra_blocked = MQTT_SELECT_ATTRIBUTES_BLOCKED
    _command_template: Callable[[PublishPayloadType], PublishPayloadType]
    _value_template: Callable[[ReceivePayloadType], ReceivePayloadType]
    _optimistic: bool
    @staticmethod
    def config_schema() -> VolSchemaType: ...
    _attr_assumed_state: Incomplete
    _attr_options: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    @callback
    def _message_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
