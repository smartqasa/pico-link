import voluptuous as vol
from .config import DEFAULT_RETAIN as DEFAULT_RETAIN, MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from .const import CONF_COMMAND_TEMPLATE as CONF_COMMAND_TEMPLATE, CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_RETAIN as CONF_RETAIN
from .entity import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import MqttCommandTemplate as MqttCommandTemplate
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from .util import valid_publish_topic as valid_publish_topic
from _typeshed import Incomplete
from homeassistant.components import button as button
from homeassistant.components.button import ButtonEntity as ButtonEntity, DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType

PARALLEL_UPDATES: int
CONF_PAYLOAD_PRESS: str
DEFAULT_NAME: str
DEFAULT_PAYLOAD_PRESS: str
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttButton(MqttEntity, ButtonEntity):
    _default_name = DEFAULT_NAME
    _entity_id_format: Incomplete
    @staticmethod
    def config_schema() -> vol.Schema: ...
    _command_template: Incomplete
    _attr_device_class: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def async_press(self) -> None: ...
