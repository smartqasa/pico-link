from . import subscription as subscription
from .config import MQTT_RO_SCHEMA as MQTT_RO_SCHEMA
from .const import CONF_OPTIONS as CONF_OPTIONS, CONF_STATE_TOPIC as CONF_STATE_TOPIC, PAYLOAD_NONE as PAYLOAD_NONE
from .entity import MqttAvailabilityMixin as MqttAvailabilityMixin, MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import MqttValueTemplate as MqttValueTemplate, PayloadSentinel as PayloadSentinel, ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from .util import check_state_too_long as check_state_too_long
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components import sensor as sensor
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA, ENTITY_ID_FORMAT as ENTITY_ID_FORMAT, RestoreSensor as RestoreSensor, STATE_CLASSES_SCHEMA as STATE_CLASSES_SCHEMA, SensorDeviceClass as SensorDeviceClass, SensorExtraStoredData as SensorExtraStoredData, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_FORCE_UPDATE as CONF_FORCE_UPDATE, CONF_NAME as CONF_NAME, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.service_info.mqtt import ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.typing import ConfigType as ConfigType, VolSchemaType as VolSchemaType

_LOGGER: Incomplete
PARALLEL_UPDATES: int
CONF_EXPIRE_AFTER: str
CONF_LAST_RESET_VALUE_TEMPLATE: str
CONF_SUGGESTED_DISPLAY_PRECISION: str
MQTT_SENSOR_ATTRIBUTES_BLOCKED: Incomplete
DEFAULT_NAME: str
DEFAULT_FORCE_UPDATE: bool
_PLATFORM_SCHEMA_BASE: Incomplete

def validate_sensor_state_and_device_class_config(config: ConfigType) -> ConfigType: ...

PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttSensor(MqttEntity, RestoreSensor):
    _default_name = DEFAULT_NAME
    _entity_id_format = ENTITY_ID_FORMAT
    _attr_last_reset: datetime | None
    _attributes_extra_blocked = MQTT_SENSOR_ATTRIBUTES_BLOCKED
    _expiration_trigger: CALLBACK_TYPE | None
    _expire_after: int | None
    _expired: bool | None
    _template: Callable[[ReceivePayloadType, PayloadSentinel], ReceivePayloadType] | None
    _last_reset_template: Callable[[ReceivePayloadType], ReceivePayloadType] | None
    _attr_native_value: Incomplete
    async def mqtt_async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @staticmethod
    def config_schema() -> VolSchemaType: ...
    _attr_device_class: Incomplete
    _attr_force_update: Incomplete
    _attr_suggested_display_precision: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_options: Incomplete
    _attr_state_class: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    @callback
    def _update_state(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _update_last_reset(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _state_message_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    @callback
    def _value_is_expired(self, *_: datetime) -> None: ...
    @property
    def available(self) -> bool: ...
