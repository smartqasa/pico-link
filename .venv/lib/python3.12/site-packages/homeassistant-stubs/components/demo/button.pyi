from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components import persistent_notification as persistent_notification
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DemoButton(ButtonEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_should_poll: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, unique_id: str, device_name: str) -> None: ...
    async def async_press(self) -> None: ...
