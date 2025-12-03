from . import get_hub as get_hub
from .entity import BaseSwitch as BaseSwitch
from .modbus import ModbusHub as ModbusHub
from _typeshed import Incomplete
from homeassistant.components.light import ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.const import CONF_LIGHTS as CONF_LIGHTS, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class ModbusLight(BaseSwitch, LightEntity):
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    async def async_turn_on(self, **kwargs: Any) -> None: ...
