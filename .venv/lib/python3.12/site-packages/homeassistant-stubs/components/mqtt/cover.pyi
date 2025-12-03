from . import subscription as subscription
from .config import MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from .const import CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_PAYLOAD_CLOSE as CONF_PAYLOAD_CLOSE, CONF_PAYLOAD_OPEN as CONF_PAYLOAD_OPEN, CONF_PAYLOAD_STOP as CONF_PAYLOAD_STOP, CONF_POSITION_CLOSED as CONF_POSITION_CLOSED, CONF_POSITION_OPEN as CONF_POSITION_OPEN, CONF_RETAIN as CONF_RETAIN, CONF_STATE_CLOSED as CONF_STATE_CLOSED, CONF_STATE_CLOSING as CONF_STATE_CLOSING, CONF_STATE_OPEN as CONF_STATE_OPEN, CONF_STATE_OPENING as CONF_STATE_OPENING, CONF_STATE_TOPIC as CONF_STATE_TOPIC, DEFAULT_OPTIMISTIC as DEFAULT_OPTIMISTIC, DEFAULT_PAYLOAD_CLOSE as DEFAULT_PAYLOAD_CLOSE, DEFAULT_PAYLOAD_OPEN as DEFAULT_PAYLOAD_OPEN, DEFAULT_POSITION_CLOSED as DEFAULT_POSITION_CLOSED, DEFAULT_POSITION_OPEN as DEFAULT_POSITION_OPEN, DEFAULT_RETAIN as DEFAULT_RETAIN, PAYLOAD_NONE as PAYLOAD_NONE
from .entity import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from .util import valid_publish_topic as valid_publish_topic, valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from homeassistant.components import cover as cover
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, ATTR_TILT_POSITION as ATTR_TILT_POSITION, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature, CoverState as CoverState, DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, STATE_CLOSED as STATE_CLOSED, STATE_CLOSING as STATE_CLOSING, STATE_OPEN as STATE_OPEN, STATE_OPENING as STATE_OPENING
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.service_info.mqtt import ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.typing import ConfigType as ConfigType, VolSchemaType as VolSchemaType
from homeassistant.util.json import JSON_DECODE_EXCEPTIONS as JSON_DECODE_EXCEPTIONS, json_loads as json_loads
from homeassistant.util.percentage import percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int
CONF_GET_POSITION_TOPIC: str
CONF_GET_POSITION_TEMPLATE: str
CONF_SET_POSITION_TOPIC: str
CONF_SET_POSITION_TEMPLATE: str
CONF_TILT_COMMAND_TOPIC: str
CONF_TILT_COMMAND_TEMPLATE: str
CONF_TILT_STATUS_TOPIC: str
CONF_TILT_STATUS_TEMPLATE: str
CONF_STATE_STOPPED: str
CONF_TILT_CLOSED_POSITION: str
CONF_TILT_MAX: str
CONF_TILT_MIN: str
CONF_TILT_OPEN_POSITION: str
CONF_TILT_STATE_OPTIMISTIC: str
TILT_PAYLOAD: str
COVER_PAYLOAD: str
DEFAULT_NAME: str
DEFAULT_STATE_STOPPED: str
DEFAULT_PAYLOAD_STOP: str
DEFAULT_TILT_CLOSED_POSITION: int
DEFAULT_TILT_MAX: int
DEFAULT_TILT_MIN: int
DEFAULT_TILT_OPEN_POSITION: int
DEFAULT_TILT_OPTIMISTIC: bool
TILT_FEATURES: Incomplete
MQTT_COVER_ATTRIBUTES_BLOCKED: Incomplete

def validate_options(config: ConfigType) -> ConfigType: ...

_PLATFORM_SCHEMA_BASE: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttCover(MqttEntity, CoverEntity):
    _attr_is_closed: bool | None
    _attributes_extra_blocked: frozenset[str]
    _default_name = DEFAULT_NAME
    _entity_id_format: str
    _optimistic: bool
    _tilt_optimistic: bool
    _tilt_closed_percentage: int
    _tilt_open_percentage: int
    _pos_range: tuple[int, int]
    _tilt_range: tuple[int, int]
    @staticmethod
    def config_schema() -> VolSchemaType: ...
    _attr_assumed_state: Incomplete
    _value_template: Incomplete
    _set_position_template: Incomplete
    _get_position_template: Incomplete
    _set_tilt_template: Incomplete
    _tilt_status_template: Incomplete
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _attr_is_opening: Incomplete
    _attr_is_closing: Incomplete
    @callback
    def _update_state(self, state: str | None) -> None: ...
    @callback
    def _tilt_message_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _state_message_received(self, msg: ReceiveMessage) -> None: ...
    _attr_current_cover_position: Incomplete
    @callback
    def _position_message_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    _attr_current_cover_tilt_position: Incomplete
    async def async_open_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_close_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_set_cover_tilt_position(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    async def async_toggle_tilt(self, **kwargs: Any) -> None: ...
    @callback
    def tilt_payload_received(self, _payload: Any) -> None: ...
