from . import MyUplinkConfigEntry as MyUplinkConfigEntry, MyUplinkDataCoordinator as MyUplinkDataCoordinator
from .const import DOMAIN as DOMAIN
from .entity import MyUplinkEntity as MyUplinkEntity
from .helpers import find_matching_platform as find_matching_platform, skip_entity as skip_entity
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from myuplink import DevicePoint as DevicePoint

async def async_setup_entry(hass: HomeAssistant, config_entry: MyUplinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MyUplinkSelect(MyUplinkEntity, SelectEntity):
    point_id: Incomplete
    _attr_name: Incomplete
    _attr_options: Incomplete
    options_map: Incomplete
    options_rev: Incomplete
    def __init__(self, coordinator: MyUplinkDataCoordinator, device_id: str, device_point: DevicePoint, unique_id_suffix: str) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
