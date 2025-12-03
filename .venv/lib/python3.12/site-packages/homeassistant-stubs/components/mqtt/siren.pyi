from . import subscription as subscription
from .config import MQTT_RW_SCHEMA as MQTT_RW_SCHEMA
from .const import CONF_COMMAND_TEMPLATE as CONF_COMMAND_TEMPLATE, CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_STATE_TOPIC as CONF_STATE_TOPIC, CONF_STATE_VALUE_TEMPLATE as CONF_STATE_VALUE_TEMPLATE, PAYLOAD_EMPTY_JSON as PAYLOAD_EMPTY_JSON, PAYLOAD_NONE as PAYLOAD_NONE
from .entity import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import siren as siren
from homeassistant.components.siren import ATTR_AVAILABLE_TONES as ATTR_AVAILABLE_TONES, ATTR_DURATION as ATTR_DURATION, ATTR_TONE as ATTR_TONE, ATTR_VOLUME_LEVEL as ATTR_VOLUME_LEVEL, SirenEntity as SirenEntity, SirenEntityFeature as SirenEntityFeature, SirenTurnOnServiceParameters as SirenTurnOnServiceParameters, TURN_ON_SCHEMA as TURN_ON_SCHEMA, process_turn_on_params as process_turn_on_params
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_PAYLOAD_OFF as CONF_PAYLOAD_OFF, CONF_PAYLOAD_ON as CONF_PAYLOAD_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.json import json_dumps as json_dumps
from homeassistant.helpers.service_info.mqtt import ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType, VolSchemaType as VolSchemaType
from homeassistant.util.json import JSON_DECODE_EXCEPTIONS as JSON_DECODE_EXCEPTIONS, json_loads_object as json_loads_object
from typing import Any

PARALLEL_UPDATES: int
DEFAULT_NAME: str
DEFAULT_PAYLOAD_ON: str
DEFAULT_PAYLOAD_OFF: str
ENTITY_ID_FORMAT: Incomplete
CONF_AVAILABLE_TONES: str
CONF_COMMAND_OFF_TEMPLATE: str
CONF_STATE_ON: str
CONF_STATE_OFF: str
CONF_SUPPORT_DURATION: str
CONF_SUPPORT_VOLUME_SET: str
STATE: str
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete
MQTT_SIREN_ATTRIBUTES_BLOCKED: Incomplete
SUPPORTED_BASE: Incomplete
SUPPORTED_ATTRIBUTES: Incomplete
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttSiren(MqttEntity, SirenEntity):
    _default_name = DEFAULT_NAME
    _entity_id_format = ENTITY_ID_FORMAT
    _attributes_extra_blocked = MQTT_SIREN_ATTRIBUTES_BLOCKED
    _extra_attributes: dict[str, Any]
    _command_templates: dict[str, Callable[[PublishPayloadType, TemplateVarsType], PublishPayloadType] | None]
    _value_template: Callable[[ReceivePayloadType], ReceivePayloadType]
    _state_on: str
    _state_off: str
    _optimistic: bool
    @staticmethod
    def config_schema() -> VolSchemaType: ...
    _attr_available_tones: Incomplete
    _attr_supported_features: Incomplete
    _attr_assumed_state: Incomplete
    _attr_is_on: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    @callback
    def _state_message_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    async def _async_publish(self, topic: str, template: str, value: Any, variables: dict[str, Any] | None = None) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _update(self, data: SirenTurnOnServiceParameters) -> None: ...
