from . import Airtouch5ConfigEntry as Airtouch5ConfigEntry
from .const import DOMAIN as DOMAIN
from .entity import Airtouch5Entity as Airtouch5Entity
from _typeshed import Incomplete
from airtouch5py.airtouch5_simple_client import Airtouch5SimpleClient as Airtouch5SimpleClient
from airtouch5py.packets.zone_name import ZoneName as ZoneName
from airtouch5py.packets.zone_status import ZoneStatusZone as ZoneStatusZone
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: Airtouch5ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class Airtouch5ZoneOpenPercentage(CoverEntity, Airtouch5Entity):
    _attr_device_class: Incomplete
    _attr_translation_key: str
    _attr_supported_features: Incomplete
    _zone_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, client: Airtouch5SimpleClient, zone_name: ZoneName, has_sensor: bool) -> None: ...
    _attr_current_cover_position: Incomplete
    _attr_is_closed: bool
    @callback
    def _async_update_attrs(self, data: dict[int, ZoneStatusZone]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    async def _set_cover_position(self, position_percent: float) -> None: ...
