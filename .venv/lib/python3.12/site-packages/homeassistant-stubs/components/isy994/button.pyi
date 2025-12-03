from .const import CONF_NETWORK as CONF_NETWORK, DOMAIN as DOMAIN
from .models import IsyData as IsyData
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyisy import ISY as ISY
from pyisy.helpers import EventListener as EventListener, NodeProperty as NodeProperty
from pyisy.networking import NetworkCommand as NetworkCommand
from pyisy.nodes import Node as Node

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ISYNodeButtonEntity(ButtonEntity):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    _node: Incomplete
    _attr_name: Incomplete
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _node_enabled: Incomplete
    _availability_handler: EventListener | None
    def __init__(self, node: Node | ISY | NetworkCommand, name: str, unique_id: str, device_info: DeviceInfo, entity_category: EntityCategory | None = None) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def async_on_update(self, event: NodeProperty, key: str) -> None: ...

class ISYNodeQueryButtonEntity(ISYNodeButtonEntity):
    async def async_press(self) -> None: ...

class ISYNodeBeepButtonEntity(ISYNodeButtonEntity):
    async def async_press(self) -> None: ...

class ISYNetworkResourceButtonEntity(ISYNodeButtonEntity):
    _attr_has_entity_name: bool
    async def async_press(self) -> None: ...
