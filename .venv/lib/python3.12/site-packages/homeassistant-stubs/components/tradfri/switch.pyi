from .const import CONF_GATEWAY_ID as CONF_GATEWAY_ID, COORDINATOR as COORDINATOR, COORDINATOR_LIST as COORDINATOR_LIST, DOMAIN as DOMAIN, KEY_API as KEY_API
from .coordinator import TradfriDeviceDataUpdateCoordinator as TradfriDeviceDataUpdateCoordinator
from .entity import TradfriBaseEntity as TradfriBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pytradfri.command import Command as Command
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TradfriSwitch(TradfriBaseEntity, SwitchEntity):
    _attr_name: Incomplete
    _device_control: Incomplete
    _device_data: Incomplete
    def __init__(self, device_coordinator: TradfriDeviceDataUpdateCoordinator, api: Callable[[Command | list[Command]], Any], gateway_id: str) -> None: ...
    def _refresh(self) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
