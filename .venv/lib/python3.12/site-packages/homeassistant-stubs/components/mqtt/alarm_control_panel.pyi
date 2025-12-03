import homeassistant.components.alarm_control_panel as alarm
import voluptuous as vol
from . import subscription as subscription
from .config import DEFAULT_RETAIN as DEFAULT_RETAIN, MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from .const import CONF_COMMAND_TEMPLATE as CONF_COMMAND_TEMPLATE, CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_RETAIN as CONF_RETAIN, CONF_STATE_TOPIC as CONF_STATE_TOPIC, CONF_SUPPORTED_FEATURES as CONF_SUPPORTED_FEATURES, PAYLOAD_NONE as PAYLOAD_NONE
from .entity import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from .util import valid_publish_topic as valid_publish_topic, valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, AlarmControlPanelState as AlarmControlPanelState
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_CODE as CONF_CODE, CONF_NAME as CONF_NAME, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
PARALLEL_UPDATES: int
_SUPPORTED_FEATURES: Incomplete
CONF_CODE_ARM_REQUIRED: str
CONF_CODE_DISARM_REQUIRED: str
CONF_CODE_TRIGGER_REQUIRED: str
CONF_PAYLOAD_DISARM: str
CONF_PAYLOAD_ARM_HOME: str
CONF_PAYLOAD_ARM_AWAY: str
CONF_PAYLOAD_ARM_NIGHT: str
CONF_PAYLOAD_ARM_VACATION: str
CONF_PAYLOAD_ARM_CUSTOM_BYPASS: str
CONF_PAYLOAD_TRIGGER: str
MQTT_ALARM_ATTRIBUTES_BLOCKED: Incomplete
DEFAULT_COMMAND_TEMPLATE: str
DEFAULT_ARM_NIGHT: str
DEFAULT_ARM_VACATION: str
DEFAULT_ARM_AWAY: str
DEFAULT_ARM_HOME: str
DEFAULT_ARM_CUSTOM_BYPASS: str
DEFAULT_DISARM: str
DEFAULT_TRIGGER: str
DEFAULT_NAME: str
REMOTE_CODE: str
REMOTE_CODE_TEXT: str
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttAlarm(MqttEntity, alarm.AlarmControlPanelEntity):
    _default_name = DEFAULT_NAME
    _entity_id_format: Incomplete
    _attributes_extra_blocked = MQTT_ALARM_ATTRIBUTES_BLOCKED
    @staticmethod
    def config_schema() -> vol.Schema: ...
    _value_template: Incomplete
    _command_template: Incomplete
    _attr_code_format: Incomplete
    _attr_code_arm_required: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _attr_alarm_state: Incomplete
    def _state_message_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def async_alarm_disarm(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_home(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_away(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_night(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_vacation(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_custom_bypass(self, code: str | None = None) -> None: ...
    async def async_alarm_trigger(self, code: str | None = None) -> None: ...
    async def _publish(self, code: str | None, action: str) -> None: ...
    def _validate_code(self, code: str | None, state: str) -> bool: ...
