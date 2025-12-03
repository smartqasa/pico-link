from .common import TCP_PLATFORM_SCHEMA as TCP_PLATFORM_SCHEMA
from .const import CONF_VALUE_ON as CONF_VALUE_ON
from .entity import TcpEntity as TcpEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Final

PLATFORM_SCHEMA: Final[Incomplete]

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class TcpBinarySensor(TcpEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...
