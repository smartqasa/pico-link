from .const import DOMAIN as DOMAIN
from .schemas import SCHEMA_MAC as SCHEMA_MAC
from homeassistant.components.bluetooth import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_MAC as CONF_MAC
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.util import slugify as slugify
from typing import Any

class EQ3ConfigFlow(ConfigFlow, domain=DOMAIN):
    mac_address: str
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_bluetooth(self, discovery_info: BluetoothServiceInfoBleak) -> ConfigFlowResult: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

def validate_mac(mac: str) -> bool: ...
