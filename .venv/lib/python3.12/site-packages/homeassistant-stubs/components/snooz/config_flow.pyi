import asyncio
from .const import DOMAIN as DOMAIN
from dataclasses import dataclass
from homeassistant.components.bluetooth import BluetoothScanningMode as BluetoothScanningMode, BluetoothServiceInfo as BluetoothServiceInfo, async_discovered_service_info as async_discovered_service_info, async_process_advertisements as async_process_advertisements
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_NAME as CONF_NAME, CONF_TOKEN as CONF_TOKEN
from pysnooz.advertisement import SnoozAdvertisementData
from typing import Any

WAIT_FOR_PAIRING_TIMEOUT: int

@dataclass
class DiscoveredSnooz:
    info: BluetoothServiceInfo
    device: SnoozAdvertisementData

class SnoozConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _discovery: DiscoveredSnooz | None
    _discovered_devices: dict[str, DiscoveredSnooz]
    _pairing_task: asyncio.Task | None
    def __init__(self) -> None: ...
    async def async_step_bluetooth(self, discovery_info: BluetoothServiceInfo) -> ConfigFlowResult: ...
    async def async_step_bluetooth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_wait_for_pairing_mode(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_pairing_complete(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_pairing_timeout(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    def _create_snooz_entry(self, discovery: DiscoveredSnooz) -> ConfigFlowResult: ...
    async def _async_wait_for_pairing_mode(self) -> None: ...
