from .const import DOMAIN as DOMAIN, EXPECTED_SERVICE_UUID as EXPECTED_SERVICE_UUID
from _typeshed import Incomplete
from homeassistant.components.bluetooth import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak, async_discovered_service_info as async_discovered_service_info
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS
from typing import Any

_LOGGER: Incomplete

class IdasenDeskConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _discovery_info: BluetoothServiceInfoBleak | None
    _discovered_devices: dict[str, BluetoothServiceInfoBleak]
    def __init__(self) -> None: ...
    async def async_step_bluetooth(self, discovery_info: BluetoothServiceInfoBleak) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
