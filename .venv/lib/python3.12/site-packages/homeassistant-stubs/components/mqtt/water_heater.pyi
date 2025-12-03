from .climate import MqttTemperatureControlEntity as MqttTemperatureControlEntity
from .config import DEFAULT_RETAIN as DEFAULT_RETAIN, MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from .const import CONF_CURRENT_TEMP_TEMPLATE as CONF_CURRENT_TEMP_TEMPLATE, CONF_CURRENT_TEMP_TOPIC as CONF_CURRENT_TEMP_TOPIC, CONF_MODE_COMMAND_TEMPLATE as CONF_MODE_COMMAND_TEMPLATE, CONF_MODE_COMMAND_TOPIC as CONF_MODE_COMMAND_TOPIC, CONF_MODE_LIST as CONF_MODE_LIST, CONF_MODE_STATE_TEMPLATE as CONF_MODE_STATE_TEMPLATE, CONF_MODE_STATE_TOPIC as CONF_MODE_STATE_TOPIC, CONF_POWER_COMMAND_TEMPLATE as CONF_POWER_COMMAND_TEMPLATE, CONF_POWER_COMMAND_TOPIC as CONF_POWER_COMMAND_TOPIC, CONF_PRECISION as CONF_PRECISION, CONF_RETAIN as CONF_RETAIN, CONF_TEMP_COMMAND_TEMPLATE as CONF_TEMP_COMMAND_TEMPLATE, CONF_TEMP_COMMAND_TOPIC as CONF_TEMP_COMMAND_TOPIC, CONF_TEMP_INITIAL as CONF_TEMP_INITIAL, CONF_TEMP_MAX as CONF_TEMP_MAX, CONF_TEMP_MIN as CONF_TEMP_MIN, CONF_TEMP_STATE_TEMPLATE as CONF_TEMP_STATE_TEMPLATE, CONF_TEMP_STATE_TOPIC as CONF_TEMP_STATE_TOPIC, DEFAULT_OPTIMISTIC as DEFAULT_OPTIMISTIC, PAYLOAD_NONE as PAYLOAD_NONE
from .entity import async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from .util import valid_publish_topic as valid_publish_topic, valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from homeassistant.components import water_heater as water_heater
from homeassistant.components.water_heater import ATTR_OPERATION_MODE as ATTR_OPERATION_MODE, DEFAULT_MIN_TEMP as DEFAULT_MIN_TEMP, STATE_ECO as STATE_ECO, STATE_ELECTRIC as STATE_ELECTRIC, STATE_GAS as STATE_GAS, STATE_HEAT_PUMP as STATE_HEAT_PUMP, STATE_HIGH_DEMAND as STATE_HIGH_DEMAND, STATE_PERFORMANCE as STATE_PERFORMANCE, WaterHeaterEntity as WaterHeaterEntity, WaterHeaterEntityFeature as WaterHeaterEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_PAYLOAD_OFF as CONF_PAYLOAD_OFF, CONF_PAYLOAD_ON as CONF_PAYLOAD_ON, CONF_TEMPERATURE_UNIT as CONF_TEMPERATURE_UNIT, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, PRECISION_HALVES as PRECISION_HALVES, PRECISION_TENTHS as PRECISION_TENTHS, PRECISION_WHOLE as PRECISION_WHOLE, STATE_OFF as STATE_OFF, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import ConfigType as ConfigType, VolSchemaType as VolSchemaType
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int
DEFAULT_NAME: str
MQTT_WATER_HEATER_ATTRIBUTES_BLOCKED: Incomplete
VALUE_TEMPLATE_KEYS: Incomplete
COMMAND_TEMPLATE_KEYS: Incomplete
TOPIC_KEYS: Incomplete
_PLATFORM_SCHEMA_BASE: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete
_DISCOVERY_SCHEMA_BASE: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttWaterHeater(MqttTemperatureControlEntity, WaterHeaterEntity):
    _default_name = DEFAULT_NAME
    _entity_id_format: Incomplete
    _attributes_extra_blocked = MQTT_WATER_HEATER_ATTRIBUTES_BLOCKED
    _attr_target_temperature_low: float | None
    _attr_target_temperature_high: float | None
    @staticmethod
    def config_schema() -> VolSchemaType: ...
    _attr_operation_list: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    _attr_precision: Incomplete
    _topic: Incomplete
    _optimistic: Incomplete
    _attr_target_temperature: Incomplete
    _attr_current_operation: Incomplete
    _value_templates: Incomplete
    _command_templates: Incomplete
    _attr_supported_features: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    @callback
    def _handle_current_mode_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_operation_mode(self, operation_mode: str) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
