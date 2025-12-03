from .const import CONF_ALWAYS_CONNECTED as CONF_ALWAYS_CONNECTED, CONF_KEY as CONF_KEY, CONF_LOCAL_NAME as CONF_LOCAL_NAME, CONF_SLOT as CONF_SLOT, DOMAIN as DOMAIN
from .util import async_find_existing_service_info as async_find_existing_service_info, human_readable_name as human_readable_name
from _typeshed import Incomplete
from bleak_retry_connector import BLEDevice as BLEDevice
from collections.abc import Mapping
from homeassistant.components.bluetooth import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak, async_ble_device_from_address as async_ble_device_from_address, async_discovered_service_info as async_discovered_service_info
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import AbortFlow as AbortFlow
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from typing import Any, Self
from yalexs_ble import ValidatedLockConfig

_LOGGER: Incomplete

async def async_validate_lock_or_error(local_name: str, device: BLEDevice, key: str, slot: int) -> dict[str, str]: ...

class YalexsConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _address: str | None
    _local_name_is_unique: bool
    active: bool
    local_name: str | None
    _discovery_info: BluetoothServiceInfoBleak | None
    _discovered_devices: dict[str, BluetoothServiceInfoBleak]
    _lock_cfg: ValidatedLockConfig | None
    def __init__(self) -> None: ...
    async def async_step_bluetooth(self, discovery_info: BluetoothServiceInfoBleak) -> ConfigFlowResult: ...
    async def async_step_integration_discovery(self, discovery_info: DiscoveryInfoType) -> ConfigFlowResult: ...
    def is_matching(self, other_flow: Self) -> bool: ...
    async def async_step_integration_discovery_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_validate(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> YaleXSBLEOptionsFlowHandler: ...

class YaleXSBLEOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_device_options(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
