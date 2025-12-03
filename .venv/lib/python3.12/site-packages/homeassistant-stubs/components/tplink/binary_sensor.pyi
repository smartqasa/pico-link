from . import TPLinkConfigEntry as TPLinkConfigEntry
from .entity import CoordinatedTPLinkFeatureEntity as CoordinatedTPLinkFeatureEntity, TPLinkFeatureEntityDescription as TPLinkFeatureEntityDescription
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Final

@dataclass(frozen=True, kw_only=True)
class TPLinkBinarySensorEntityDescription(BinarySensorEntityDescription, TPLinkFeatureEntityDescription): ...

BINARY_SENSOR_DESCRIPTIONS: Final[Incomplete]
BINARYSENSOR_DESCRIPTIONS_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: TPLinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TPLinkBinarySensorEntity(CoordinatedTPLinkFeatureEntity, BinarySensorEntity):
    entity_description: TPLinkBinarySensorEntityDescription
    _attr_is_on: Incomplete
    @callback
    def _async_update_attrs(self) -> bool: ...
