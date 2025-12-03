from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from zwave_js_server.model.driver import Driver as Driver

PARALLEL_UPDATES: int
NOTIFICATION_SMOKE_ALARM: str
NOTIFICATION_CARBON_MONOOXIDE: str
NOTIFICATION_CARBON_DIOXIDE: str
NOTIFICATION_HEAT: str
NOTIFICATION_WATER: str
NOTIFICATION_ACCESS_CONTROL: str
NOTIFICATION_HOME_SECURITY: str
NOTIFICATION_POWER_MANAGEMENT: str
NOTIFICATION_SYSTEM: str
NOTIFICATION_EMERGENCY: str
NOTIFICATION_CLOCK: str
NOTIFICATION_APPLIANCE: str
NOTIFICATION_HOME_HEALTH: str
NOTIFICATION_SIREN: str
NOTIFICATION_WATER_VALVE: str
NOTIFICATION_WEATHER: str
NOTIFICATION_IRRIGATION: str
NOTIFICATION_GAS: str

@dataclass(frozen=True)
class NotificationZWaveJSEntityDescription(BinarySensorEntityDescription):
    off_state: str = ...
    states: tuple[str, ...] | None = ...

@dataclass(frozen=True, kw_only=True)
class PropertyZWaveJSEntityDescription(BinarySensorEntityDescription):
    on_states: tuple[str, ...]

NOTIFICATION_SENSOR_MAPPINGS: tuple[NotificationZWaveJSEntityDescription, ...]
PROPERTY_SENSOR_MAPPINGS: dict[str, PropertyZWaveJSEntityDescription]
BOOLEAN_SENSOR_MAPPINGS: dict[int, BinarySensorEntityDescription]

@callback
def is_valid_notification_binary_sensor(info: ZwaveDiscoveryInfo) -> bool | NotificationZWaveJSEntityDescription: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ZWaveBooleanBinarySensor(ZWaveBaseEntity, BinarySensorEntity):
    _attr_name: Incomplete
    entity_description: Incomplete
    def __init__(self, config_entry: ConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo) -> None: ...
    @property
    def is_on(self) -> bool | None: ...

class ZWaveNotificationBinarySensor(ZWaveBaseEntity, BinarySensorEntity):
    state_key: Incomplete
    entity_description: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, config_entry: ConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo, state_key: str, description: NotificationZWaveJSEntityDescription | None = None) -> None: ...
    @property
    def is_on(self) -> bool | None: ...

class ZWavePropertyBinarySensor(ZWaveBaseEntity, BinarySensorEntity):
    entity_description: PropertyZWaveJSEntityDescription
    _attr_name: Incomplete
    def __init__(self, config_entry: ConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo, description: PropertyZWaveJSEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...

class ZWaveConfigParameterBinarySensor(ZWaveBooleanBinarySensor):
    _attr_entity_category: Incomplete
    _attr_name: Incomplete
    def __init__(self, config_entry: ConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo) -> None: ...
