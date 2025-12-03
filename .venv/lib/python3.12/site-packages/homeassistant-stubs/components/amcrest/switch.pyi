from . import AmcrestDevice as AmcrestDevice
from .const import DATA_AMCREST as DATA_AMCREST, DEVICES as DEVICES
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_SWITCHES as CONF_SWITCHES
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

PRIVACY_MODE_KEY: str
SWITCH_TYPES: tuple[SwitchEntityDescription, ...]
SWITCH_KEYS: list[str]

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class AmcrestSwitch(SwitchEntity):
    _api: Incomplete
    entity_description: Incomplete
    _attr_name: Incomplete
    def __init__(self, name: str, device: AmcrestDevice, entity_description: SwitchEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _async_turn_switch(self, mode: bool) -> None: ...
    _attr_is_on: Incomplete
    async def async_update(self) -> None: ...
