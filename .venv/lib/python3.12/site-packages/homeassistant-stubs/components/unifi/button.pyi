import aiounifi
from . import UnifiConfigEntry as UnifiConfigEntry
from .entity import HandlerT as HandlerT, UnifiEntity as UnifiEntity, UnifiEntityDescription as UnifiEntityDescription, async_device_available_fn as async_device_available_fn, async_device_device_info_fn as async_device_device_info_fn, async_wlan_available_fn as async_wlan_available_fn, async_wlan_device_info_fn as async_wlan_device_info_fn
from .hub import UnifiHub as UnifiHub
from aiounifi.interfaces.api_handlers import ItemEvent as ItemEvent
from aiounifi.models.api import ApiItemT
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@callback
def async_port_power_cycle_available_fn(hub: UnifiHub, obj_id: str) -> bool: ...
async def async_restart_device_control_fn(api: aiounifi.Controller, obj_id: str) -> None: ...
async def async_power_cycle_port_control_fn(api: aiounifi.Controller, obj_id: str) -> None: ...
async def async_regenerate_password_control_fn(api: aiounifi.Controller, obj_id: str) -> None: ...

@dataclass(frozen=True, kw_only=True)
class UnifiButtonEntityDescription(ButtonEntityDescription, UnifiEntityDescription[HandlerT, ApiItemT]):
    control_fn: Callable[[aiounifi.Controller, str], Coroutine[Any, Any, None]]

ENTITY_DESCRIPTIONS: tuple[UnifiButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: UnifiConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class UnifiButtonEntity(UnifiEntity[HandlerT, ApiItemT], ButtonEntity):
    entity_description: UnifiButtonEntityDescription[HandlerT, ApiItemT]
    async def async_press(self) -> None: ...
    @callback
    def async_update_state(self, event: ItemEvent, obj_id: str) -> None: ...
