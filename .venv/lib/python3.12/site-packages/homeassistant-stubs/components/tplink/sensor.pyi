from . import TPLinkConfigEntry as TPLinkConfigEntry
from .const import UNIT_MAPPING as UNIT_MAPPING
from .deprecate import async_cleanup_deprecated as async_cleanup_deprecated
from .entity import CoordinatedTPLinkFeatureEntity as CoordinatedTPLinkFeatureEntity, TPLinkFeatureEntityDescription as TPLinkFeatureEntityDescription
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class TPLinkSensorEntityDescription(SensorEntityDescription, TPLinkFeatureEntityDescription): ...

SENSOR_DESCRIPTIONS: tuple[TPLinkSensorEntityDescription, ...]
SENSOR_DESCRIPTIONS_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: TPLinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TPLinkSensorEntity(CoordinatedTPLinkFeatureEntity, SensorEntity):
    entity_description: TPLinkSensorEntityDescription
    _attr_suggested_display_precision: Incomplete
    _attr_native_value: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    @callback
    def _async_update_attrs(self) -> bool: ...
