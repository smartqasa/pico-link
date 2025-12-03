from .const import DOMAIN as DOMAIN, INTENT_CLOSE_COVER as INTENT_CLOSE_COVER, INTENT_OPEN_COVER as INTENT_OPEN_COVER
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from enum import IntFlag, StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import SERVICE_CLOSE_COVER as SERVICE_CLOSE_COVER, SERVICE_CLOSE_COVER_TILT as SERVICE_CLOSE_COVER_TILT, SERVICE_OPEN_COVER as SERVICE_OPEN_COVER, SERVICE_OPEN_COVER_TILT as SERVICE_OPEN_COVER_TILT, SERVICE_SET_COVER_POSITION as SERVICE_SET_COVER_POSITION, SERVICE_SET_COVER_TILT_POSITION as SERVICE_SET_COVER_TILT_POSITION, SERVICE_STOP_COVER as SERVICE_STOP_COVER, SERVICE_STOP_COVER_TILT as SERVICE_STOP_COVER_TILT, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TOGGLE_COVER_TILT as SERVICE_TOGGLE_COVER_TILT, STATE_CLOSED as STATE_CLOSED, STATE_CLOSING as STATE_CLOSING, STATE_OPEN as STATE_OPEN, STATE_OPENING as STATE_OPENING
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.deprecation import DeprecatedConstantEnum as DeprecatedConstantEnum, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.hass_dict import HassKey as HassKey
from propcache import cached_property
from typing import Any, final

_LOGGER: Incomplete
DATA_COMPONENT: HassKey[EntityComponent[CoverEntity]]
ENTITY_ID_FORMAT: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete

class CoverState(StrEnum):
    CLOSED = 'closed'
    CLOSING = 'closing'
    OPEN = 'open'
    OPENING = 'opening'

_DEPRECATED_STATE_CLOSED: Incomplete
_DEPRECATED_STATE_CLOSING: Incomplete
_DEPRECATED_STATE_OPEN: Incomplete
_DEPRECATED_STATE_OPENING: Incomplete

class CoverDeviceClass(StrEnum):
    AWNING = 'awning'
    BLIND = 'blind'
    CURTAIN = 'curtain'
    DAMPER = 'damper'
    DOOR = 'door'
    GARAGE = 'garage'
    GATE = 'gate'
    SHADE = 'shade'
    SHUTTER = 'shutter'
    WINDOW = 'window'

DEVICE_CLASSES_SCHEMA: Incomplete
DEVICE_CLASSES: Incomplete

class CoverEntityFeature(IntFlag):
    OPEN = 1
    CLOSE = 2
    SET_POSITION = 4
    STOP = 8
    OPEN_TILT = 16
    CLOSE_TILT = 32
    STOP_TILT = 64
    SET_TILT_POSITION = 128

ATTR_CURRENT_POSITION: str
ATTR_CURRENT_TILT_POSITION: str
ATTR_POSITION: str
ATTR_TILT_POSITION: str

@bind_hass
def is_closed(hass: HomeAssistant, entity_id: str) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class CoverEntityDescription(EntityDescription, frozen_or_thawed=True):
    device_class: CoverDeviceClass | None = ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class CoverEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: CoverEntityDescription
    _attr_current_cover_position: int | None
    _attr_current_cover_tilt_position: int | None
    _attr_device_class: CoverDeviceClass | None
    _attr_is_closed: bool | None
    _attr_is_closing: bool | None
    _attr_is_opening: bool | None
    _attr_state: None
    _attr_supported_features: CoverEntityFeature | None
    _cover_is_last_toggle_direction_open: bool
    @cached_property
    def current_cover_position(self) -> int | None: ...
    @cached_property
    def current_cover_tilt_position(self) -> int | None: ...
    @cached_property
    def device_class(self) -> CoverDeviceClass | None: ...
    @property
    @final
    def state(self) -> str | None: ...
    @final
    @property
    def state_attributes(self) -> dict[str, Any]: ...
    @property
    def supported_features(self) -> CoverEntityFeature: ...
    @cached_property
    def is_opening(self) -> bool | None: ...
    @cached_property
    def is_closing(self) -> bool | None: ...
    @cached_property
    def is_closed(self) -> bool | None: ...
    def open_cover(self, **kwargs: Any) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    def close_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    def toggle(self, **kwargs: Any) -> None: ...
    async def async_toggle(self, **kwargs: Any) -> None: ...
    def set_cover_position(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    def stop_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    def open_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_open_cover_tilt(self, **kwargs: Any) -> None: ...
    def close_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_close_cover_tilt(self, **kwargs: Any) -> None: ...
    def set_cover_tilt_position(self, **kwargs: Any) -> None: ...
    async def async_set_cover_tilt_position(self, **kwargs: Any) -> None: ...
    def stop_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_stop_cover_tilt(self, **kwargs: Any) -> None: ...
    def toggle_tilt(self, **kwargs: Any) -> None: ...
    async def async_toggle_tilt(self, **kwargs: Any) -> None: ...
    def _get_toggle_function[**_P, _R](self, fns: dict[str, Callable[_P, _R]]) -> Callable[_P, _R]: ...

__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
