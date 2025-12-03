from .common import TCP_PLATFORM_SCHEMA as TCP_PLATFORM_SCHEMA
from .entity import TcpEntity as TcpEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.const import CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, StateType as StateType
from typing import Final

PLATFORM_SCHEMA: Final[Incomplete]

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class TcpSensor(TcpEntity, SensorEntity):
    @property
    def native_value(self) -> StateType: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
