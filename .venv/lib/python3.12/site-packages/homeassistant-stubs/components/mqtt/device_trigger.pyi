from . import debug_info as debug_info
from .config import MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from .const import ATTR_DISCOVERY_HASH as ATTR_DISCOVERY_HASH, CONF_ENCODING as CONF_ENCODING, CONF_PAYLOAD as CONF_PAYLOAD, CONF_QOS as CONF_QOS, CONF_TOPIC as CONF_TOPIC, DOMAIN as DOMAIN
from .discovery import MQTTDiscoveryPayload as MQTTDiscoveryPayload, clear_discovery_hash as clear_discovery_hash
from .entity import MqttDiscoveryDeviceUpdateMixin as MqttDiscoveryDeviceUpdateMixin, send_discovery_done as send_discovery_done, update_device as update_device
from .models import DATA_MQTT as DATA_MQTT
from .schemas import MQTT_ENTITY_DEVICE_INFO_SCHEMA as MQTT_ENTITY_DEVICE_INFO_SCHEMA
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass, field
from homeassistant.components.device_automation import DEVICE_TRIGGER_BASE_SCHEMA as DEVICE_TRIGGER_BASE_SCHEMA
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

_LOGGER: Incomplete
CONF_AUTOMATION_TYPE: str
CONF_DISCOVERY_ID: str
CONF_SUBTYPE: str
DEFAULT_ENCODING: str
DEVICE: str
MQTT_TRIGGER_BASE: Incomplete
TRIGGER_SCHEMA: Incomplete
TRIGGER_DISCOVERY_SCHEMA: Incomplete
LOG_NAME: str

@dataclass(slots=True)
class TriggerInstance:
    action: TriggerActionType
    trigger_info: TriggerInfo
    trigger: Trigger
    remove: CALLBACK_TYPE | None = ...
    async def async_attach_trigger(self) -> None: ...

@dataclass(slots=True, kw_only=True)
class Trigger:
    device_id: str
    discovery_data: DiscoveryInfoType | None = ...
    discovery_id: str | None = ...
    hass: HomeAssistant
    payload: str | None
    qos: int | None
    subtype: str
    topic: str | None
    type: str
    value_template: str | None
    trigger_instances: list[TriggerInstance] = field(default_factory=list)
    async def add_trigger(self, action: TriggerActionType, trigger_info: TriggerInfo) -> Callable[[], None]: ...
    async def update_trigger(self, config: ConfigType) -> None: ...
    def detach_trigger(self) -> None: ...

class MqttDeviceTrigger(MqttDiscoveryDeviceUpdateMixin):
    _config: Incomplete
    _config_entry: Incomplete
    device_id: Incomplete
    discovery_data: Incomplete
    hass: Incomplete
    _mqtt_data: Incomplete
    trigger_id: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConfigType, device_id: str, discovery_data: DiscoveryInfoType, config_entry: ConfigEntry) -> None: ...
    async def async_setup(self) -> None: ...
    async def async_update(self, discovery_data: MQTTDiscoveryPayload) -> None: ...
    async def async_tear_down(self) -> None: ...

async def async_setup_trigger(hass: HomeAssistant, config: ConfigType, config_entry: ConfigEntry, discovery_data: DiscoveryInfoType) -> None: ...
async def async_removed_from_device(hass: HomeAssistant, device_id: str) -> None: ...
async def async_get_triggers(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
