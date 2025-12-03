from . import DsmrConfigEntry as DsmrConfigEntry
from .const import CONF_DSMR_VERSION as CONF_DSMR_VERSION, CONF_SERIAL_ID as CONF_SERIAL_ID, CONF_SERIAL_ID_GAS as CONF_SERIAL_ID_GAS, CONF_TIME_BETWEEN_UPDATE as CONF_TIME_BETWEEN_UPDATE, DEFAULT_PRECISION as DEFAULT_PRECISION, DEFAULT_RECONNECT_INTERVAL as DEFAULT_RECONNECT_INTERVAL, DEFAULT_TIME_BETWEEN_UPDATE as DEFAULT_TIME_BETWEEN_UPDATE, DEVICE_NAME_ELECTRICITY as DEVICE_NAME_ELECTRICITY, DEVICE_NAME_GAS as DEVICE_NAME_GAS, DEVICE_NAME_HEAT as DEVICE_NAME_HEAT, DEVICE_NAME_WATER as DEVICE_NAME_WATER, DOMAIN as DOMAIN, DSMR_PROTOCOL as DSMR_PROTOCOL, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Generator
from dataclasses import dataclass
from dsmr_parser.objects import DSMRObject as DSMRObject, MbusDevice as MbusDevice, Telegram as Telegram
from enum import IntEnum
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_PROTOCOL as CONF_PROTOCOL, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, EntityCategory as EntityCategory, UnitOfEnergy as UnitOfEnergy, UnitOfVolume as UnitOfVolume
from homeassistant.core import CoreState as CoreState, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util import Throttle as Throttle

EVENT_FIRST_TELEGRAM: str
UNIT_CONVERSION: Incomplete

@dataclass(frozen=True, kw_only=True)
class DSMRSensorEntityDescription(SensorEntityDescription):
    dsmr_versions: set[str] | None = ...
    is_gas: bool = ...
    is_water: bool = ...
    is_heat: bool = ...
    obis_reference: str

class MbusDeviceType(IntEnum):
    GAS = 3
    HEAT = 4
    WATER = 7

SENSORS: tuple[DSMRSensorEntityDescription, ...]
SENSORS_MBUS_DEVICE_TYPE: dict[int, tuple[DSMRSensorEntityDescription, ...]]

def device_class_and_uom(data: Telegram | MbusDevice, entity_description: DSMRSensorEntityDescription) -> tuple[SensorDeviceClass | None, str | None]: ...
def rename_old_gas_to_mbus(hass: HomeAssistant, entry: ConfigEntry, mbus_device_id: str) -> None: ...
def is_supported_description(data: Telegram | MbusDevice, description: DSMRSensorEntityDescription, dsmr_version: str) -> bool: ...
def create_mbus_entities(hass: HomeAssistant, telegram: Telegram, entry: ConfigEntry, dsmr_version: str) -> Generator[DSMREntity]: ...
def get_dsmr_object(telegram: Telegram | None, mbus_id: int, obis_reference: str) -> DSMRObject | None: ...
async def async_setup_entry(hass: HomeAssistant, entry: DsmrConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DSMREntity(SensorEntity):
    entity_description: DSMRSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _entry: Incomplete
    telegram: Telegram | None
    _attr_device_info: Incomplete
    _mbus_id: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, entity_description: DSMRSensorEntityDescription, entry: ConfigEntry, telegram: Telegram, device_class: SensorDeviceClass, native_unit_of_measurement: str | None, serial_id: str = '', mbus_id: int = 0) -> None: ...
    @callback
    def update_data(self, telegram: Telegram | None) -> None: ...
    def get_dsmr_object_attr(self, attribute: str) -> str | None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> StateType: ...
    @staticmethod
    def translate_tariff(value: str, dsmr_version: str) -> str | None: ...
