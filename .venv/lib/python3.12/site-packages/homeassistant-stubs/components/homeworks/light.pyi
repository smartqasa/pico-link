from . import HomeworksData as HomeworksData
from .const import CONF_ADDR as CONF_ADDR, CONF_CONTROLLER_ID as CONF_CONTROLLER_ID, CONF_DIMMERS as CONF_DIMMERS, CONF_RATE as CONF_RATE, DOMAIN as DOMAIN
from .entity import HomeworksEntity as HomeworksEntity
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyhomeworks.pyhomeworks import Homeworks as Homeworks
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HomeworksLight(HomeworksEntity, LightEntity):
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_device_info: Incomplete
    _rate: Incomplete
    _level: int
    _prev_level: int
    def __init__(self, controller: Homeworks, controller_id: str, addr: str, name: str, rate: float) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    @property
    def brightness(self) -> int: ...
    def _set_brightness(self, level: int) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @callback
    def _update_callback(self, msg_type: str, values: list[Any]) -> None: ...
