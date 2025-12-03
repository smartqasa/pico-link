from .const import ATTR_DEVICES as ATTR_DEVICES, DOMAIN as DOMAIN, DevId as DevId, DiscoveryInfo as DiscoveryInfo, MYSENSORS_DISCOVERED_NODES as MYSENSORS_DISCOVERED_NODES, MYSENSORS_GATEWAYS as MYSENSORS_GATEWAYS, MYSENSORS_ON_UNLOAD as MYSENSORS_ON_UNLOAD, PLATFORMS as PLATFORMS, SensorType as SensorType
from .entity import MySensorsChildEntity as MySensorsChildEntity, get_mysensors_devices as get_mysensors_devices
from .gateway import finish_setup as finish_setup, gw_stop as gw_stop, setup_gateway as setup_gateway
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from mysensors import BaseAsyncGateway as BaseAsyncGateway

_LOGGER: Incomplete
DATA_HASS_CONFIG: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: ConfigEntry, device_entry: DeviceEntry) -> bool: ...
@callback
def setup_mysensors_platform(hass: HomeAssistant, domain: Platform, discovery_info: DiscoveryInfo, device_class: type[MySensorsChildEntity] | Mapping[SensorType, type[MySensorsChildEntity]], device_args: tuple | None = None, async_add_entities: Callable | None = None) -> list[MySensorsChildEntity] | None: ...
