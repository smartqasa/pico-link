from .const import CONF_URL_CONTROL as CONF_URL_CONTROL, NETATMO_CREATE_COVER as NETATMO_CREATE_COVER
from .data_handler import HOME as HOME, NetatmoDevice as NetatmoDevice, SIGNAL_NAME as SIGNAL_NAME
from .entity import NetatmoModuleEntity as NetatmoModuleEntity
from _typeshed import Incomplete
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyatmo import modules as NaModules
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NetatmoCover(NetatmoModuleEntity, CoverEntity):
    _attr_supported_features: Incomplete
    _attr_configuration_url = CONF_URL_CONTROL
    _attr_device_class: Incomplete
    _attr_name: Incomplete
    device: NaModules.Shutter
    _attr_is_closed: Incomplete
    _signal_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    _attr_current_cover_position: Incomplete
    @callback
    def async_update_callback(self) -> None: ...
