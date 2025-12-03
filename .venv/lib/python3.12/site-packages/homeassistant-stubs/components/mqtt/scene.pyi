import voluptuous as vol
from .config import MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from .const import CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_RETAIN as CONF_RETAIN
from .entity import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from .util import valid_publish_topic as valid_publish_topic
from _typeshed import Incomplete
from homeassistant.components import scene as scene
from homeassistant.components.scene import Scene as Scene
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PAYLOAD_ON as CONF_PAYLOAD_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

PARALLEL_UPDATES: int
DEFAULT_NAME: str
DEFAULT_RETAIN: bool
ENTITY_ID_FORMAT: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttScene(MqttEntity, Scene):
    _default_name = DEFAULT_NAME
    _entity_id_format: Incomplete
    @staticmethod
    def config_schema() -> vol.Schema: ...
    def _setup_from_config(self, config: ConfigType) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def async_activate(self, **kwargs: Any) -> None: ...
