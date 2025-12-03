from .entity import PowerWallEntity as PowerWallEntity
from .models import PowerwallConfigEntry as PowerwallConfigEntry
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

CONNECTED_GRID_STATUSES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: PowerwallConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PowerWallRunningSensor(PowerWallEntity, BinarySensorEntity):
    _attr_translation_key: str
    _attr_device_class: Incomplete
    @property
    def unique_id(self) -> str: ...
    @property
    def is_on(self) -> bool: ...

class PowerWallConnectedSensor(PowerWallEntity, BinarySensorEntity):
    _attr_translation_key: str
    _attr_device_class: Incomplete
    @property
    def unique_id(self) -> str: ...
    @property
    def is_on(self) -> bool: ...

class PowerWallGridServicesActiveSensor(PowerWallEntity, BinarySensorEntity):
    _attr_translation_key: str
    _attr_device_class: Incomplete
    @property
    def unique_id(self) -> str: ...
    @property
    def is_on(self) -> bool: ...

class PowerWallGridStatusSensor(PowerWallEntity, BinarySensorEntity):
    _attr_translation_key: str
    _attr_device_class: Incomplete
    @property
    def unique_id(self) -> str: ...
    @property
    def is_on(self) -> bool: ...

class PowerWallChargingStatusSensor(PowerWallEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
    @property
    def available(self) -> bool: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def is_on(self) -> bool: ...
