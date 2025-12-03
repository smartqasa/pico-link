from . import subscription as subscription
from .config import MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from .const import CONF_PAYLOAD_RESET as CONF_PAYLOAD_RESET, CONF_STATE_TOPIC as CONF_STATE_TOPIC
from .entity import CONF_JSON_ATTRS_TOPIC as CONF_JSON_ATTRS_TOPIC, MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import MqttValueTemplate as MqttValueTemplate, ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from .util import valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import device_tracker as device_tracker
from homeassistant.components.device_tracker import SourceType as SourceType, TrackerEntity as TrackerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_GPS_ACCURACY as ATTR_GPS_ACCURACY, ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONF_NAME as CONF_NAME, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, STATE_HOME as STATE_HOME, STATE_NOT_HOME as STATE_NOT_HOME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.service_info.mqtt import ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.typing import ConfigType as ConfigType, VolSchemaType as VolSchemaType

_LOGGER: Incomplete
PARALLEL_UPDATES: int
CONF_PAYLOAD_HOME: str
CONF_PAYLOAD_NOT_HOME: str
CONF_SOURCE_TYPE: str
DEFAULT_PAYLOAD_RESET: str
DEFAULT_SOURCE_TYPE: Incomplete

def valid_config(config: ConfigType) -> ConfigType: ...

PLATFORM_SCHEMA_MODERN_BASE: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttDeviceTracker(MqttEntity, TrackerEntity):
    _default_name: Incomplete
    _entity_id_format: Incomplete
    _location_name: str | None
    _value_template: Callable[[ReceivePayloadType], ReceivePayloadType]
    @staticmethod
    def config_schema() -> VolSchemaType: ...
    def _setup_from_config(self, config: ConfigType) -> None: ...
    @callback
    def _tracker_message_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    @property
    def force_update(self) -> bool: ...
    async def _subscribe_topics(self) -> None: ...
    @property
    def latitude(self) -> float | None: ...
    @property
    def location_accuracy(self) -> int: ...
    @property
    def longitude(self) -> float | None: ...
    @property
    def location_name(self) -> str | None: ...
    @property
    def source_type(self) -> SourceType: ...
