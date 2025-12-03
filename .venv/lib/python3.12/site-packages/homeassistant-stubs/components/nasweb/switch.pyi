from . import NASwebConfigEntry as NASwebConfigEntry
from .const import DOMAIN as DOMAIN, STATUS_UPDATE_MAX_TIME_INTERVAL as STATUS_UPDATE_MAX_TIME_INTERVAL
from .coordinator import NASwebCoordinator as NASwebCoordinator
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import BaseCoordinatorEntity as BaseCoordinatorEntity, BaseDataUpdateCoordinatorProtocol as BaseDataUpdateCoordinatorProtocol
from typing import Any
from webio_api import Output as NASwebOutput

OUTPUT_TRANSLATION_KEY: str
_LOGGER: Incomplete

def _get_output(coordinator: NASwebCoordinator, index: int) -> NASwebOutput | None: ...
async def async_setup_entry(hass: HomeAssistant, config: NASwebConfigEntry, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class RelaySwitch(SwitchEntity, BaseCoordinatorEntity):
    _output: Incomplete
    _attr_icon: str
    _attr_has_entity_name: bool
    _attr_translation_key: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: BaseDataUpdateCoordinatorProtocol, nasweb_output: NASwebOutput) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_is_on: Incomplete
    _attr_available: bool
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def async_update(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
