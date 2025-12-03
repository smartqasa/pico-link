from _typeshed import Incomplete
from anel_pwrctrl import Device as Device, Switch as Switch
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util import Throttle as Throttle
from typing import Any

_LOGGER: Incomplete
CONF_PORT_RECV: str
CONF_PORT_SEND: str
MIN_TIME_BETWEEN_UPDATES: Incomplete
PLATFORM_SCHEMA: Incomplete

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class PwrCtrlSwitch(SwitchEntity):
    _port: Incomplete
    _parent_device: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, port: Switch, parent_device: PwrCtrlDevice) -> None: ...
    _attr_is_on: Incomplete
    def update(self) -> None: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...

class PwrCtrlDevice:
    _device: Incomplete
    def __init__(self, device: Device) -> None: ...
    def update(self) -> None: ...
