from . import Router as Router
from .const import UPDATE_SIGNAL as UPDATE_SIGNAL
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import Entity as Entity

SCAN_INTERVAL: Incomplete

class HuaweiLteBaseEntity(Entity):
    _available: bool
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    router: Incomplete
    _unsub_handlers: list[Callable]
    def __init__(self, router: Router) -> None: ...
    @property
    def _device_unique_id(self) -> str: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def available(self) -> bool: ...
    async def async_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def _async_maybe_update(self, config_entry_unique_id: str) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...

class HuaweiLteBaseEntityWithDevice(HuaweiLteBaseEntity):
    @property
    def device_info(self) -> DeviceInfo: ...
