from . import AmbientStationConfigEntry as AmbientStationConfigEntry
from .const import ATTR_LAST_DATA as ATTR_LAST_DATA
from .entity import AmbientWeatherEntity as AmbientWeatherEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import ATTR_NAME as ATTR_NAME, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Literal

TYPE_BATT1: str
TYPE_BATT10: str
TYPE_BATT2: str
TYPE_BATT3: str
TYPE_BATT4: str
TYPE_BATT5: str
TYPE_BATT6: str
TYPE_BATT7: str
TYPE_BATT8: str
TYPE_BATT9: str
TYPE_BATTIN: str
TYPE_BATTOUT: str
TYPE_BATT_CO2: str
TYPE_BATT_LEAK1: str
TYPE_BATT_LEAK2: str
TYPE_BATT_LEAK3: str
TYPE_BATT_LEAK4: str
TYPE_BATT_LIGHTNING: str
TYPE_BATT_SM1: str
TYPE_BATT_SM10: str
TYPE_BATT_SM2: str
TYPE_BATT_SM3: str
TYPE_BATT_SM4: str
TYPE_BATT_SM5: str
TYPE_BATT_SM6: str
TYPE_BATT_SM7: str
TYPE_BATT_SM8: str
TYPE_BATT_SM9: str
TYPE_LEAK1: str
TYPE_LEAK2: str
TYPE_LEAK3: str
TYPE_LEAK4: str
TYPE_PM25IN_BATT: str
TYPE_PM25_BATT: str
TYPE_RELAY1: str
TYPE_RELAY10: str
TYPE_RELAY2: str
TYPE_RELAY3: str
TYPE_RELAY4: str
TYPE_RELAY5: str
TYPE_RELAY6: str
TYPE_RELAY7: str
TYPE_RELAY8: str
TYPE_RELAY9: str

@dataclass(frozen=True, kw_only=True)
class AmbientBinarySensorDescription(BinarySensorEntityDescription):
    on_state: Literal[0, 1]

BINARY_SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AmbientStationConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AmbientWeatherBinarySensor(AmbientWeatherEntity, BinarySensorEntity):
    entity_description: AmbientBinarySensorDescription
    _attr_is_on: Incomplete
    @callback
    def update_from_latest_data(self) -> None: ...
