from . import AquaLogicProcessor as AquaLogicProcessor, DOMAIN as DOMAIN, UPDATE_TOPIC as UPDATE_TOPIC
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import CONF_MONITORED_CONDITIONS as CONF_MONITORED_CONDITIONS, PERCENTAGE as PERCENTAGE, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

@dataclass(frozen=True)
class AquaLogicSensorEntityDescription(SensorEntityDescription):
    unit_metric: str | None = ...
    unit_imperial: str | None = ...

SENSOR_TYPES: tuple[AquaLogicSensorEntityDescription, ...]
SENSOR_KEYS: list[str]
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class AquaLogicSensor(SensorEntity):
    entity_description: AquaLogicSensorEntityDescription
    _attr_should_poll: bool
    _processor: Incomplete
    _attr_name: Incomplete
    def __init__(self, processor: AquaLogicProcessor, description: AquaLogicSensorEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_native_unit_of_measurement: Incomplete
    _attr_native_value: Incomplete
    @callback
    def async_update_callback(self) -> None: ...
