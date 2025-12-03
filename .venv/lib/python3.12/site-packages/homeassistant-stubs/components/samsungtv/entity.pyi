from .const import CONF_MANUFACTURER as CONF_MANUFACTURER, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import SamsungTVDataUpdateCoordinator as SamsungTVDataUpdateCoordinator
from .triggers.turn_on import async_get_turn_on_trigger as async_get_turn_on_trigger
from _typeshed import Incomplete
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS, ATTR_IDENTIFIERS as ATTR_IDENTIFIERS, CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_MODEL as CONF_MODEL, CONF_NAME as CONF_NAME
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.trigger import PluggableAction as PluggableAction
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class SamsungTVEntity(CoordinatorEntity[SamsungTVDataUpdateCoordinator], Entity):
    _attr_has_entity_name: bool
    _bridge: Incomplete
    _mac: str | None
    _host: str | None
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _turn_on_action: Incomplete
    def __init__(self, *, coordinator: SamsungTVDataUpdateCoordinator) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
    def _wake_on_lan(self) -> None: ...
    async def _async_turn_off(self) -> None: ...
    async def _async_turn_on(self) -> None: ...
