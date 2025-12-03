import abc
from . import subscription as subscription
from .config import DEFAULT_RETAIN as DEFAULT_RETAIN, MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from .const import CONF_ACTION_TEMPLATE as CONF_ACTION_TEMPLATE, CONF_ACTION_TOPIC as CONF_ACTION_TOPIC, CONF_CURRENT_HUMIDITY_TEMPLATE as CONF_CURRENT_HUMIDITY_TEMPLATE, CONF_CURRENT_HUMIDITY_TOPIC as CONF_CURRENT_HUMIDITY_TOPIC, CONF_CURRENT_TEMP_TEMPLATE as CONF_CURRENT_TEMP_TEMPLATE, CONF_CURRENT_TEMP_TOPIC as CONF_CURRENT_TEMP_TOPIC, CONF_MODE_COMMAND_TEMPLATE as CONF_MODE_COMMAND_TEMPLATE, CONF_MODE_COMMAND_TOPIC as CONF_MODE_COMMAND_TOPIC, CONF_MODE_LIST as CONF_MODE_LIST, CONF_MODE_STATE_TEMPLATE as CONF_MODE_STATE_TEMPLATE, CONF_MODE_STATE_TOPIC as CONF_MODE_STATE_TOPIC, CONF_POWER_COMMAND_TEMPLATE as CONF_POWER_COMMAND_TEMPLATE, CONF_POWER_COMMAND_TOPIC as CONF_POWER_COMMAND_TOPIC, CONF_PRECISION as CONF_PRECISION, CONF_RETAIN as CONF_RETAIN, CONF_TEMP_COMMAND_TEMPLATE as CONF_TEMP_COMMAND_TEMPLATE, CONF_TEMP_COMMAND_TOPIC as CONF_TEMP_COMMAND_TOPIC, CONF_TEMP_INITIAL as CONF_TEMP_INITIAL, CONF_TEMP_MAX as CONF_TEMP_MAX, CONF_TEMP_MIN as CONF_TEMP_MIN, CONF_TEMP_STATE_TEMPLATE as CONF_TEMP_STATE_TEMPLATE, CONF_TEMP_STATE_TOPIC as CONF_TEMP_STATE_TOPIC, DEFAULT_OPTIMISTIC as DEFAULT_OPTIMISTIC, PAYLOAD_NONE as PAYLOAD_NONE
from .entity import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from .util import valid_publish_topic as valid_publish_topic, valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Callable as Callable
from homeassistant.components import climate as climate
from homeassistant.components.climate import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, DEFAULT_MAX_HUMIDITY as DEFAULT_MAX_HUMIDITY, DEFAULT_MIN_HUMIDITY as DEFAULT_MIN_HUMIDITY, FAN_AUTO as FAN_AUTO, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MEDIUM as FAN_MEDIUM, HVACAction as HVACAction, HVACMode as HVACMode, PRESET_NONE as PRESET_NONE, SWING_OFF as SWING_OFF, SWING_ON as SWING_ON
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_PAYLOAD_OFF as CONF_PAYLOAD_OFF, CONF_PAYLOAD_ON as CONF_PAYLOAD_ON, CONF_TEMPERATURE_UNIT as CONF_TEMPERATURE_UNIT, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, PRECISION_HALVES as PRECISION_HALVES, PRECISION_TENTHS as PRECISION_TENTHS, PRECISION_WHOLE as PRECISION_WHOLE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.service_info.mqtt import ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import ConfigType as ConfigType, VolSchemaType as VolSchemaType
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int
DEFAULT_NAME: str
CONF_FAN_MODE_COMMAND_TEMPLATE: str
CONF_FAN_MODE_COMMAND_TOPIC: str
CONF_FAN_MODE_LIST: str
CONF_FAN_MODE_STATE_TEMPLATE: str
CONF_FAN_MODE_STATE_TOPIC: str
CONF_HUMIDITY_COMMAND_TEMPLATE: str
CONF_HUMIDITY_COMMAND_TOPIC: str
CONF_HUMIDITY_STATE_TEMPLATE: str
CONF_HUMIDITY_STATE_TOPIC: str
CONF_HUMIDITY_MAX: str
CONF_HUMIDITY_MIN: str
CONF_PRESET_MODE_STATE_TOPIC: str
CONF_PRESET_MODE_COMMAND_TOPIC: str
CONF_PRESET_MODE_VALUE_TEMPLATE: str
CONF_PRESET_MODE_COMMAND_TEMPLATE: str
CONF_PRESET_MODES_LIST: str
CONF_SWING_MODE_COMMAND_TEMPLATE: str
CONF_SWING_MODE_COMMAND_TOPIC: str
CONF_SWING_MODE_LIST: str
CONF_SWING_MODE_STATE_TEMPLATE: str
CONF_SWING_MODE_STATE_TOPIC: str
CONF_TEMP_HIGH_COMMAND_TEMPLATE: str
CONF_TEMP_HIGH_COMMAND_TOPIC: str
CONF_TEMP_HIGH_STATE_TEMPLATE: str
CONF_TEMP_HIGH_STATE_TOPIC: str
CONF_TEMP_LOW_COMMAND_TEMPLATE: str
CONF_TEMP_LOW_COMMAND_TOPIC: str
CONF_TEMP_LOW_STATE_TEMPLATE: str
CONF_TEMP_LOW_STATE_TOPIC: str
CONF_TEMP_STEP: str
DEFAULT_INITIAL_TEMPERATURE: float
MQTT_CLIMATE_ATTRIBUTES_BLOCKED: Incomplete
VALUE_TEMPLATE_KEYS: Incomplete
COMMAND_TEMPLATE_KEYS: Incomplete
TOPIC_KEYS: Incomplete

def valid_preset_mode_configuration(config: ConfigType) -> ConfigType: ...
def valid_humidity_range_configuration(config: ConfigType) -> ConfigType: ...
def valid_humidity_state_configuration(config: ConfigType) -> ConfigType: ...

_PLATFORM_SCHEMA_BASE: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete
_DISCOVERY_SCHEMA_BASE: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttTemperatureControlEntity(MqttEntity, ABC, metaclass=abc.ABCMeta):
    _attr_target_temperature_low: float | None
    _attr_target_temperature_high: float | None
    _feature_preset_mode: bool
    _optimistic: bool
    _topic: dict[str, Any]
    _command_templates: dict[str, Callable[[PublishPayloadType], PublishPayloadType]]
    _value_templates: dict[str, Callable[[ReceivePayloadType], ReceivePayloadType]]
    def render_template(self, msg: ReceiveMessage, template_name: str) -> ReceivePayloadType: ...
    @callback
    def handle_climate_attribute_received(self, template_name: str, attr: str, msg: ReceiveMessage) -> None: ...
    @callback
    def prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def _publish(self, topic: str, payload: PublishPayloadType) -> None: ...
    async def _set_climate_attribute(self, temp: float | None, cmnd_topic: str, cmnd_template: str, state_topic: str, attr: str) -> bool: ...
    @abstractmethod
    async def async_set_temperature(self, **kwargs: Any) -> None: ...

class MqttClimate(MqttTemperatureControlEntity, ClimateEntity):
    _attr_fan_mode: str | None
    _attr_hvac_mode: HVACMode | None
    _attr_swing_mode: str | None
    _default_name = DEFAULT_NAME
    _entity_id_format: Incomplete
    _attributes_extra_blocked = MQTT_CLIMATE_ATTRIBUTES_BLOCKED
    _attr_target_temperature_low: float | None
    _attr_target_temperature_high: float | None
    @staticmethod
    def config_schema() -> VolSchemaType: ...
    _attr_hvac_modes: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    _attr_min_humidity: Incomplete
    _attr_max_humidity: Incomplete
    _attr_precision: Incomplete
    _attr_fan_modes: Incomplete
    _attr_swing_modes: Incomplete
    _attr_target_temperature_step: Incomplete
    _topic: Incomplete
    _optimistic: Incomplete
    _attr_target_temperature: Incomplete
    _feature_preset_mode: Incomplete
    _attr_preset_modes: Incomplete
    _attr_preset_mode: Incomplete
    _optimistic_preset_mode: Incomplete
    _value_templates: Incomplete
    _command_templates: Incomplete
    _attr_supported_features: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _attr_hvac_action: Incomplete
    @callback
    def _handle_action_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _handle_mode_received(self, template_name: str, attr: str, mode_list: str, msg: ReceiveMessage) -> None: ...
    @callback
    def _handle_preset_mode_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_humidity(self, humidity: float) -> None: ...
    async def async_set_swing_mode(self, swing_mode: str) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_turn_on(self) -> None: ...
    async def async_turn_off(self) -> None: ...
