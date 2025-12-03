from . import subscription as subscription
from .config import MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from .const import CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_RETAIN as CONF_RETAIN, CONF_STATE_TOPIC as CONF_STATE_TOPIC
from .entity import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from .util import valid_publish_topic as valid_publish_topic
from _typeshed import Incomplete
from homeassistant.components import vacuum as vacuum
from homeassistant.components.vacuum import ENTITY_ID_FORMAT as ENTITY_ID_FORMAT, StateVacuumEntity as StateVacuumEntity, VacuumActivity as VacuumActivity, VacuumEntityFeature as VacuumEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.json import json_dumps as json_dumps
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, VolSchemaType as VolSchemaType
from homeassistant.util.json import json_loads_object as json_loads_object
from typing import Any

PARALLEL_UPDATES: int
BATTERY: str
FAN_SPEED: str
STATE: str
STATE_IDLE: str
STATE_DOCKED: str
STATE_ERROR: str
STATE_PAUSED: str
STATE_RETURNING: str
STATE_CLEANING: str
POSSIBLE_STATES: dict[str, VacuumActivity]
CONF_SUPPORTED_FEATURES = ATTR_SUPPORTED_FEATURES
CONF_PAYLOAD_TURN_ON: str
CONF_PAYLOAD_TURN_OFF: str
CONF_PAYLOAD_RETURN_TO_BASE: str
CONF_PAYLOAD_STOP: str
CONF_PAYLOAD_CLEAN_SPOT: str
CONF_PAYLOAD_LOCATE: str
CONF_PAYLOAD_START: str
CONF_PAYLOAD_PAUSE: str
CONF_SET_FAN_SPEED_TOPIC: str
CONF_FAN_SPEED_LIST: str
CONF_SEND_COMMAND_TOPIC: str
DEFAULT_NAME: str
DEFAULT_RETAIN: bool
DEFAULT_PAYLOAD_RETURN_TO_BASE: str
DEFAULT_PAYLOAD_STOP: str
DEFAULT_PAYLOAD_CLEAN_SPOT: str
DEFAULT_PAYLOAD_LOCATE: str
DEFAULT_PAYLOAD_START: str
DEFAULT_PAYLOAD_PAUSE: str
_LOGGER: Incomplete
SERVICE_TO_STRING: dict[VacuumEntityFeature, str]
STRING_TO_SERVICE: Incomplete
DEFAULT_SERVICES: Incomplete
ALL_SERVICES: Incomplete

def services_to_strings(services: VacuumEntityFeature, service_to_string: dict[VacuumEntityFeature, str]) -> list[str]: ...

DEFAULT_SERVICE_STRINGS: Incomplete
_FEATURE_PAYLOADS: Incomplete
MQTT_VACUUM_ATTRIBUTES_BLOCKED: Incomplete
MQTT_VACUUM_DOCS_URL: str
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttStateVacuum(MqttEntity, StateVacuumEntity):
    _default_name = DEFAULT_NAME
    _entity_id_format = ENTITY_ID_FORMAT
    _attributes_extra_blocked = MQTT_VACUUM_ATTRIBUTES_BLOCKED
    _command_topic: str | None
    _set_fan_speed_topic: str | None
    _send_command_topic: str | None
    _payloads: dict[str, str | None]
    _state_attrs: dict[str, Any]
    def __init__(self, hass: HomeAssistant, config: ConfigType, config_entry: ConfigEntry, discovery_data: DiscoveryInfoType | None) -> None: ...
    @staticmethod
    def config_schema() -> VolSchemaType: ...
    _attr_supported_features: Incomplete
    _attr_fan_speed_list: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _attr_fan_speed: Incomplete
    _attr_battery_level: Incomplete
    def _update_state_attributes(self, payload: dict[str, Any]) -> None: ...
    _attr_activity: Incomplete
    @callback
    def _state_message_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def _async_publish_command(self, feature: VacuumEntityFeature) -> None: ...
    async def async_start(self) -> None: ...
    async def async_pause(self) -> None: ...
    async def async_stop(self, **kwargs: Any) -> None: ...
    async def async_return_to_base(self, **kwargs: Any) -> None: ...
    async def async_clean_spot(self, **kwargs: Any) -> None: ...
    async def async_locate(self, **kwargs: Any) -> None: ...
    async def async_set_fan_speed(self, fan_speed: str, **kwargs: Any) -> None: ...
    async def async_send_command(self, command: str, params: dict[str, Any] | list[Any] | None = None, **kwargs: Any) -> None: ...
