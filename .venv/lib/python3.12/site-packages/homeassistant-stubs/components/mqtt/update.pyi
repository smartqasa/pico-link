from . import subscription as subscription
from .config import DEFAULT_RETAIN as DEFAULT_RETAIN, MQTT_RO_SCHEMA as MQTT_RO_SCHEMA
from .const import CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_RETAIN as CONF_RETAIN, CONF_STATE_TOPIC as CONF_STATE_TOPIC, PAYLOAD_EMPTY_JSON as PAYLOAD_EMPTY_JSON
from .entity import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import MqttValueTemplate as MqttValueTemplate, ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from .util import valid_publish_topic as valid_publish_topic, valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from homeassistant.components import update as update
from homeassistant.components.update import DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA, UpdateEntity as UpdateEntity, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_NAME as CONF_NAME, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, VolSchemaType as VolSchemaType
from homeassistant.util.json import JSON_DECODE_EXCEPTIONS as JSON_DECODE_EXCEPTIONS, json_loads as json_loads
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int
DEFAULT_NAME: str
CONF_DISPLAY_PRECISION: str
CONF_LATEST_VERSION_TEMPLATE: str
CONF_LATEST_VERSION_TOPIC: str
CONF_PAYLOAD_INSTALL: str
CONF_RELEASE_SUMMARY: str
CONF_RELEASE_URL: str
CONF_TITLE: str
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete
MQTT_JSON_UPDATE_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttUpdate(MqttEntity, UpdateEntity, RestoreEntity):
    _default_name = DEFAULT_NAME
    _entity_id_format: Incomplete
    @property
    def entity_picture(self) -> str | None: ...
    @staticmethod
    def config_schema() -> VolSchemaType: ...
    _attr_device_class: Incomplete
    _attr_display_precision: Incomplete
    _attr_release_summary: Incomplete
    _attr_release_url: Incomplete
    _attr_title: Incomplete
    _templates: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _attr_installed_version: Incomplete
    _attr_latest_version: Incomplete
    _attr_entity_picture: Incomplete
    _attr_update_percentage: Incomplete
    _attr_in_progress: Incomplete
    @callback
    def _handle_state_message_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _handle_latest_version_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
    @property
    def supported_features(self) -> UpdateEntityFeature: ...
