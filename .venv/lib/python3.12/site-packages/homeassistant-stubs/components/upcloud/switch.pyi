from .const import DATA_UPCLOUD as DATA_UPCLOUD
from .entity import UpCloudServerEntity as UpCloudServerEntity
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_USERNAME as CONF_USERNAME, STATE_OFF as STATE_OFF
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import dispatcher_send as dispatcher_send
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SIGNAL_UPDATE_UPCLOUD: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class UpCloudSwitch(UpCloudServerEntity, SwitchEntity):
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
