from . import TPLinkConfigEntry as TPLinkConfigEntry
from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from .entity import CoordinatedTPLinkEntity as CoordinatedTPLinkEntity, async_refresh_after as async_refresh_after
from _typeshed import Incomplete
from homeassistant.components.siren import SirenEntity as SirenEntity, SirenEntityFeature as SirenEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from kasa import Device as Device
from kasa.smart.modules.alarm import Alarm as Alarm
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: TPLinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TPLinkSirenEntity(CoordinatedTPLinkEntity, SirenEntity):
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _alarm_module: Alarm
    def __init__(self, device: Device, coordinator: TPLinkDataUpdateCoordinator) -> None: ...
    @async_refresh_after
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @async_refresh_after
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def _async_update_attrs(self) -> bool: ...
