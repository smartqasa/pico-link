from .const import CONF_RESTORE_LIGHT_STATE as CONF_RESTORE_LIGHT_STATE, DOMAIN as DOMAIN, UOM_PERCENTAGE as UOM_PERCENTAGE, _LOGGER as _LOGGER
from .entity import ISYNodeEntity as ISYNodeEntity
from .models import IsyData as IsyData
from _typeshed import Incomplete
from homeassistant.components.light import ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from pyisy.helpers import NodeProperty as NodeProperty
from pyisy.nodes import Node as Node
from typing import Any

ATTR_LAST_BRIGHTNESS: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ISYLightEntity(ISYNodeEntity, LightEntity, RestoreEntity):
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _last_brightness: int | None
    _restore_light_state: Incomplete
    def __init__(self, node: Node, restore_light_state: bool, device_info: DeviceInfo | None = None) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def brightness(self) -> int | None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @callback
    def async_on_update(self, event: NodeProperty) -> None: ...
    async def async_turn_on(self, brightness: int | None = None, **kwargs: Any) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    async def async_added_to_hass(self) -> None: ...
