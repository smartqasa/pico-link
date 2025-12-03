from . import get_hyperion_device_id as get_hyperion_device_id, get_hyperion_unique_id as get_hyperion_unique_id, listen_for_instance_updates as listen_for_instance_updates
from .const import CONF_INSTANCE_CLIENTS as CONF_INSTANCE_CLIENTS, DOMAIN as DOMAIN, HYPERION_MANUFACTURER_NAME as HYPERION_MANUFACTURER_NAME, HYPERION_MODEL_NAME as HYPERION_MODEL_NAME, SIGNAL_ENTITY_REMOVE as SIGNAL_ENTITY_REMOVE, TYPE_HYPERION_COMPONENT_SWITCH_BASE as TYPE_HYPERION_COMPONENT_SWITCH_BASE
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import slugify as slugify
from hyperion import client as client
from typing import Any

COMPONENT_SWITCHES: Incomplete

def _component_to_unique_id(server_id: str, component: str, instance_num: int) -> str: ...
def _component_to_translation_key(component: str) -> str: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HyperionComponentSwitch(SwitchEntity):
    _attr_entity_category: Incomplete
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    _attr_entity_registry_enabled_default: bool
    _attr_unique_id: Incomplete
    _device_id: Incomplete
    _attr_translation_key: Incomplete
    _instance_name: Incomplete
    _component_name: Incomplete
    _client: Incomplete
    _client_callbacks: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, server_id: str, instance_num: int, instance_name: str, component_name: str, hyperion_client: client.HyperionClient) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    async def _async_send_set_component(self, value: bool) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @callback
    def _update_components(self, _: dict[str, Any] | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
