from . import util as util
from .const import DOMAIN as DOMAIN, IPV4_BROADCAST_ADDR as IPV4_BROADCAST_ADDR, LOOPBACK_TARGET_IP as LOOPBACK_TARGET_IP, MDNS_TARGET_IP as MDNS_TARGET_IP, PUBLIC_TARGET_IP as PUBLIC_TARGET_IP
from .models import Adapter as Adapter
from .network import Network as Network, async_get_network as async_get_network
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.typing import ConfigType as ConfigType, UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from homeassistant.loader import bind_hass as bind_hass
from ipaddress import IPv4Address, IPv6Address

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

@bind_hass
async def async_get_adapters(hass: HomeAssistant) -> list[Adapter]: ...
@bind_hass
async def async_get_source_ip(hass: HomeAssistant, target_ip: str | UndefinedType = ...) -> str: ...
@bind_hass
async def async_get_enabled_source_ips(hass: HomeAssistant) -> list[IPv4Address | IPv6Address]: ...
@callback
def async_only_default_interface_enabled(adapters: list[Adapter]) -> bool: ...
@bind_hass
async def async_get_ipv4_broadcast_addresses(hass: HomeAssistant) -> set[IPv4Address]: ...
async def async_get_announce_addresses(hass: HomeAssistant) -> list[str]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
