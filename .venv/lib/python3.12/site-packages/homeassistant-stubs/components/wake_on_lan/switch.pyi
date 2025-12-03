from .const import CONF_OFF_ACTION as CONF_OFF_ACTION, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_PING_TIMEOUT as DEFAULT_PING_TIMEOUT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.const import CONF_BROADCAST_ADDRESS as CONF_BROADCAST_ADDRESS, CONF_BROADCAST_PORT as CONF_BROADCAST_PORT, CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.script import Script as Script
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class WolSwitch(SwitchEntity):
    _attr_name: Incomplete
    _host: Incomplete
    _mac_address: Incomplete
    _broadcast_address: Incomplete
    _broadcast_port: Incomplete
    _off_script: Incomplete
    _state: bool
    _attr_assumed_state: Incomplete
    _attr_should_poll: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, hass: HomeAssistant, name: str, host: str | None, mac_address: str, off_action: list[Any] | None, broadcast_address: str | None, broadcast_port: int | None) -> None: ...
    @property
    def is_on(self) -> bool: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    def update(self) -> None: ...
