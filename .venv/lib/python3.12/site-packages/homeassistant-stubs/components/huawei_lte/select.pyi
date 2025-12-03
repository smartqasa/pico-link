from . import Router as Router
from .const import DOMAIN as DOMAIN, KEY_NET_NET_MODE as KEY_NET_NET_MODE
from .entity import HuaweiLteBaseEntityWithDevice as HuaweiLteBaseEntityWithDevice
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class HuaweiSelectEntityDescription(SelectEntityDescription):
    setter_fn: Callable[[str], None]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HuaweiLteSelectEntity(HuaweiLteBaseEntityWithDevice, SelectEntity):
    entity_description: HuaweiSelectEntityDescription
    _raw_state: str | None
    key: Incomplete
    item: Incomplete
    _attr_name: Incomplete
    def __init__(self, router: Router, entity_description: HuaweiSelectEntityDescription, key: str, item: str) -> None: ...
    def select_option(self, option: str) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    @property
    def _device_unique_id(self) -> str: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    _available: bool
    async def async_update(self) -> None: ...
