from . import OneWireConfigEntry as OneWireConfigEntry
from .const import DEVICE_KEYS_0_3 as DEVICE_KEYS_0_3, DEVICE_KEYS_0_7 as DEVICE_KEYS_0_7, DEVICE_KEYS_A_B as DEVICE_KEYS_A_B, READ_MODE_BOOL as READ_MODE_BOOL
from .entity import OneWireEntity as OneWireEntity, OneWireEntityDescription as OneWireEntityDescription
from .onewirehub import OneWireHub as OneWireHub
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True)
class OneWireBinarySensorEntityDescription(OneWireEntityDescription, BinarySensorEntityDescription): ...

DEVICE_BINARY_SENSORS: dict[str, tuple[OneWireBinarySensorEntityDescription, ...]]
HOBBYBOARD_EF: dict[str, tuple[OneWireBinarySensorEntityDescription, ...]]

def get_sensor_types(device_sub_type: str) -> dict[str, tuple[OneWireBinarySensorEntityDescription, ...]]: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: OneWireConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def get_entities(onewire_hub: OneWireHub) -> list[OneWireBinarySensor]: ...

class OneWireBinarySensor(OneWireEntity, BinarySensorEntity):
    entity_description: OneWireBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...
