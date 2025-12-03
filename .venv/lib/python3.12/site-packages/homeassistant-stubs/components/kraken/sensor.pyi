from . import KrakenData as KrakenData
from .const import CONF_TRACKED_ASSET_PAIRS as CONF_TRACKED_ASSET_PAIRS, DISPATCH_CONFIG_UPDATED as DISPATCH_CONFIG_UPDATED, DOMAIN as DOMAIN, KrakenResponse as KrakenResponse
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class KrakenSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[DataUpdateCoordinator[KrakenResponse], str], float | int]

SENSOR_TYPES: tuple[KrakenSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class KrakenSensor(CoordinatorEntity[DataUpdateCoordinator[KrakenResponse | None]], SensorEntity):
    entity_description: KrakenSensorEntityDescription
    _attr_state_class: Incomplete
    _attr_has_entity_name: bool
    tracked_asset_pair_wsname: Incomplete
    _target_asset: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _device_name: Incomplete
    _attr_unique_id: Incomplete
    _received_data_at_least_once: bool
    _available: bool
    _attr_device_info: Incomplete
    def __init__(self, kraken_data: KrakenData, tracked_asset_pair: str, description: KrakenSensorEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    _attr_native_value: Incomplete
    def _update_internal_state(self) -> None: ...
    @property
    def icon(self) -> str: ...
    @property
    def available(self) -> bool: ...

def create_device_name(tracked_asset_pair: str) -> str: ...
