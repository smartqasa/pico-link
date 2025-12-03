from . import WLEDConfigEntry as WLEDConfigEntry
from .const import ATTR_DURATION as ATTR_DURATION, ATTR_TARGET_BRIGHTNESS as ATTR_TARGET_BRIGHTNESS, ATTR_UDP_PORT as ATTR_UDP_PORT
from .coordinator import WLEDDataUpdateCoordinator as WLEDDataUpdateCoordinator
from .entity import WLEDEntity as WLEDEntity
from .helpers import wled_exception_handler as wled_exception_handler
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: WLEDConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WLEDNightlightSwitch(WLEDEntity, SwitchEntity):
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    @property
    def is_on(self) -> bool: ...
    @wled_exception_handler
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @wled_exception_handler
    async def async_turn_on(self, **kwargs: Any) -> None: ...

class WLEDSyncSendSwitch(WLEDEntity, SwitchEntity):
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    @property
    def is_on(self) -> bool: ...
    @wled_exception_handler
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @wled_exception_handler
    async def async_turn_on(self, **kwargs: Any) -> None: ...

class WLEDSyncReceiveSwitch(WLEDEntity, SwitchEntity):
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    @property
    def is_on(self) -> bool: ...
    @wled_exception_handler
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @wled_exception_handler
    async def async_turn_on(self, **kwargs: Any) -> None: ...

class WLEDReverseSwitch(WLEDEntity, SwitchEntity):
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _segment: int
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator, segment: int) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool: ...
    @wled_exception_handler
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @wled_exception_handler
    async def async_turn_on(self, **kwargs: Any) -> None: ...

@callback
def async_update_segments(coordinator: WLEDDataUpdateCoordinator, current_ids: set[int], async_add_entities: AddEntitiesCallback) -> None: ...
