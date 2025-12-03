from . import AmbientStation as AmbientStation
from .const import ATTR_LAST_DATA as ATTR_LAST_DATA, DOMAIN as DOMAIN, TYPE_SOLARRADIATION as TYPE_SOLARRADIATION, TYPE_SOLARRADIATION_LX as TYPE_SOLARRADIATION_LX
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription

class AmbientWeatherEntity(Entity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _ambient: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _mac_address: Incomplete
    entity_description: Incomplete
    def __init__(self, ambient: AmbientStation, mac_address: str, station_name: str, description: EntityDescription) -> None: ...
    _attr_available: Incomplete
    @callback
    def _async_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def update_from_latest_data(self) -> None: ...
