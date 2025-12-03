import voluptuous as vol
from . import subscription as subscription
from .config import MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from .const import CONF_TOPIC as CONF_TOPIC
from .entity import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from .util import valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from homeassistant.components import camera as camera
from homeassistant.components.camera import Camera as Camera
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

_LOGGER: Incomplete
PARALLEL_UPDATES: int
CONF_IMAGE_ENCODING: str
DEFAULT_NAME: str
MQTT_CAMERA_ATTRIBUTES_BLOCKED: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttCamera(MqttEntity, Camera):
    _default_name = DEFAULT_NAME
    _entity_id_format: str
    _attributes_extra_blocked: frozenset[str]
    _last_image: bytes | None
    def __init__(self, hass: HomeAssistant, config: ConfigType, config_entry: ConfigEntry, discovery_data: DiscoveryInfoType | None) -> None: ...
    @staticmethod
    def config_schema() -> vol.Schema: ...
    @callback
    def _image_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
