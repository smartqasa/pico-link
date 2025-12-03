from . import AquaLogicProcessor as AquaLogicProcessor, DOMAIN as DOMAIN, UPDATE_TOPIC as UPDATE_TOPIC
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.const import CONF_MONITORED_CONDITIONS as CONF_MONITORED_CONDITIONS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

SWITCH_TYPES: Incomplete
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class AquaLogicSwitch(SwitchEntity):
    _attr_should_poll: bool
    _processor: Incomplete
    _state_name: Incomplete
    _attr_name: Incomplete
    def __init__(self, processor: AquaLogicProcessor, switch_type: str) -> None: ...
    @property
    def is_on(self) -> bool: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    async def async_added_to_hass(self) -> None: ...
