from . import MyUplinkConfigEntry as MyUplinkConfigEntry, MyUplinkDataCoordinator as MyUplinkDataCoordinator
from .const import DOMAIN as DOMAIN, F_SERIES as F_SERIES
from .entity import MyUplinkEntity as MyUplinkEntity
from .helpers import find_matching_platform as find_matching_platform, skip_entity as skip_entity, transform_model_series as transform_model_series
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from myuplink import DevicePoint as DevicePoint
from typing import Any

CATEGORY_BASED_DESCRIPTIONS: dict[str, dict[str, SwitchEntityDescription]]

def get_description(device_point: DevicePoint) -> SwitchEntityDescription | None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: MyUplinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MyUplinkDevicePointSwitch(MyUplinkEntity, SwitchEntity):
    point_id: Incomplete
    _attr_name: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: MyUplinkDataCoordinator, device_id: str, device_point: DevicePoint, entity_description: SwitchEntityDescription | None, unique_id_suffix: str) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _async_turn_switch(self, mode: int) -> None: ...
