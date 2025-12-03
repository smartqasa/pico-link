from _typeshed import Incomplete
from homeassistant.components import mqtt as mqtt
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.const import DEGREE as DEGREE, UnitOfPrecipitationDepth as UnitOfPrecipitationDepth, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util import slugify as slugify
from homeassistant.util.json import json_loads_object as json_loads_object
from typing import Any

_LOGGER: Incomplete
DOMAIN: str
DATA_ARWN: str
TOPIC: str

def discover_sensors(topic: str, payload: dict[str, Any]) -> list[ArwnSensor] | None: ...
def _slug(name: str) -> str: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class ArwnSensor(SensorEntity):
    _attr_should_poll: bool
    entity_id: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _state_key: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_icon: Incomplete
    _attr_device_class: Incomplete
    def __init__(self, topic: str, name: str, state_key: str, units: str, icon: str | None = None, device_class: SensorDeviceClass | None = None) -> None: ...
    _attr_extra_state_attributes: Incomplete
    _attr_native_value: Incomplete
    def set_event(self, event: dict[str, Any]) -> None: ...
