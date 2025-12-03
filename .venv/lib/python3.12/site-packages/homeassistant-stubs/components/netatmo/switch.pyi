from .const import CONF_URL_CONTROL as CONF_URL_CONTROL, NETATMO_CREATE_SWITCH as NETATMO_CREATE_SWITCH
from .data_handler import HOME as HOME, NetatmoDevice as NetatmoDevice, SIGNAL_NAME as SIGNAL_NAME
from .entity import NetatmoModuleEntity as NetatmoModuleEntity
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyatmo import modules as NaModules
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NetatmoSwitch(NetatmoModuleEntity, SwitchEntity):
    _attr_name: Incomplete
    _attr_configuration_url = CONF_URL_CONTROL
    device: NaModules.Switch
    _signal_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_is_on: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice) -> None: ...
    @callback
    def async_update_callback(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
