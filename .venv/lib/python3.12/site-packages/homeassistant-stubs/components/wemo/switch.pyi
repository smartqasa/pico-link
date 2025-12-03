from . import async_wemo_dispatcher_connect as async_wemo_dispatcher_connect
from .coordinator import DeviceCoordinator as DeviceCoordinator
from .entity import WemoBinaryStateEntity as WemoBinaryStateEntity
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_STANDBY as STATE_STANDBY, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pywemo import Switch as Switch
from typing import Any

SCAN_INTERVAL: Incomplete
PARALLEL_UPDATES: int
ATTR_COFFEMAKER_MODE: str
ATTR_CURRENT_STATE_DETAIL: str
ATTR_ON_LATEST_TIME: str
ATTR_ON_TODAY_TIME: str
ATTR_ON_TOTAL_TIME: str
ATTR_POWER_THRESHOLD: str
ATTR_SENSOR_STATE: str
ATTR_SWITCH_MODE: str
MAKER_SWITCH_MOMENTARY: str
MAKER_SWITCH_TOGGLE: str

async def async_setup_entry(hass: HomeAssistant, _config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WemoSwitch(WemoBinaryStateEntity, SwitchEntity):
    wemo: Switch
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @staticmethod
    def as_uptime(_seconds: int) -> str: ...
    @property
    def detail_state(self) -> str: ...
    @property
    def icon(self) -> str | None: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
