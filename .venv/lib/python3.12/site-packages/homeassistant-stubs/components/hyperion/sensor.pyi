from . import get_hyperion_device_id as get_hyperion_device_id, get_hyperion_unique_id as get_hyperion_unique_id, listen_for_instance_updates as listen_for_instance_updates
from .const import CONF_INSTANCE_CLIENTS as CONF_INSTANCE_CLIENTS, DOMAIN as DOMAIN, HYPERION_MANUFACTURER_NAME as HYPERION_MANUFACTURER_NAME, HYPERION_MODEL_NAME as HYPERION_MODEL_NAME, SIGNAL_ENTITY_REMOVE as SIGNAL_ENTITY_REMOVE, TYPE_HYPERION_SENSOR_BASE as TYPE_HYPERION_SENSOR_BASE, TYPE_HYPERION_SENSOR_VISIBLE_PRIORITY as TYPE_HYPERION_SENSOR_VISIBLE_PRIORITY
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from hyperion import client as client
from typing import Any

SENSORS: Incomplete
PRIORITY_SENSOR_DESCRIPTION: Incomplete

def _sensor_unique_id(server_id: str, instance_num: int, suffix: str) -> str: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HyperionSensor(SensorEntity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    entity_description: Incomplete
    _client: Incomplete
    _attr_native_value: Incomplete
    _client_callbacks: dict[str, Any]
    _attr_device_info: Incomplete
    def __init__(self, server_id: str, instance_num: int, instance_name: str, hyperion_client: client.HyperionClient, entity_description: SensorEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...

class HyperionVisiblePrioritySensor(HyperionSensor):
    _attr_unique_id: Incomplete
    _client_callbacks: Incomplete
    def __init__(self, server_id: str, instance_num: int, instance_name: str, hyperion_client: client.HyperionClient, entity_description: SensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    _attr_extra_state_attributes: Incomplete
    @callback
    def _update_priorities(self, _: dict[str, Any] | None = None) -> None: ...
