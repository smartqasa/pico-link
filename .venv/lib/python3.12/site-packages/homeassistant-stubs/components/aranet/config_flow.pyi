from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aranet4.client import Aranet4Advertisement
from homeassistant.components.bluetooth import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak, async_discovered_service_info as async_discovered_service_info
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS
from homeassistant.data_entry_flow import AbortFlow as AbortFlow
from typing import Any

MIN_VERSION: Incomplete

def _title(discovery_info: BluetoothServiceInfoBleak) -> str: ...

class AranetConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _discovery_info: BluetoothServiceInfoBleak | None
    _discovered_device: Aranet4Advertisement | None
    _discovered_devices: dict[str, tuple[str, Aranet4Advertisement]]
    def __init__(self) -> None: ...
    def _raise_for_advertisement_errors(self, adv: Aranet4Advertisement) -> None: ...
    async def async_step_bluetooth(self, discovery_info: BluetoothServiceInfoBleak) -> ConfigFlowResult: ...
    async def async_step_bluetooth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
