from .const import CONNECTED_PLC_DEVICES as CONNECTED_PLC_DEVICES, CONNECTED_WIFI_CLIENTS as CONNECTED_WIFI_CLIENTS, DOMAIN as DOMAIN, FIRMWARE_UPDATE_INTERVAL as FIRMWARE_UPDATE_INTERVAL, LAST_RESTART as LAST_RESTART, LONG_UPDATE_INTERVAL as LONG_UPDATE_INTERVAL, NEIGHBORING_WIFI_NETWORKS as NEIGHBORING_WIFI_NETWORKS, REGULAR_FIRMWARE as REGULAR_FIRMWARE, SHORT_UPDATE_INTERVAL as SHORT_UPDATE_INTERVAL, SWITCH_GUEST_WIFI as SWITCH_GUEST_WIFI, SWITCH_LEDS as SWITCH_LEDS
from .coordinator import DevoloDataUpdateCoordinator as DevoloDataUpdateCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from devolo_plc_api import Device
from devolo_plc_api.device_api import ConnectedStationInfo as ConnectedStationInfo, NeighborAPInfo as NeighborAPInfo, UpdateFirmwareCheck as UpdateFirmwareCheck, WifiGuestAccessGet as WifiGuestAccessGet
from devolo_plc_api.plcnet_api import LogicalNetwork as LogicalNetwork
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.update_coordinator import UpdateFailed as UpdateFailed
from typing import Any

_LOGGER: Incomplete
type DevoloHomeNetworkConfigEntry = ConfigEntry[DevoloHomeNetworkData]

@dataclass
class DevoloHomeNetworkData:
    device: Device
    coordinators: dict[str, DevoloDataUpdateCoordinator[Any]]

async def async_setup_entry(hass: HomeAssistant, entry: DevoloHomeNetworkConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: DevoloHomeNetworkConfigEntry) -> bool: ...
@callback
def platforms(device: Device) -> set[Platform]: ...
@callback
def update_sw_version(device_registry: dr.DeviceRegistry, device: Device) -> None: ...
