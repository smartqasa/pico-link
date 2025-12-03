from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import time
from homeassistant.components.time import TimeEntity as TimeEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DemoTime(TimeEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_should_poll: bool
    _attr_assumed_state: Incomplete
    _attr_native_value: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, unique_id: str, device_name: str, state: time, assumed_state: bool) -> None: ...
    async def async_set_value(self, value: time) -> None: ...
