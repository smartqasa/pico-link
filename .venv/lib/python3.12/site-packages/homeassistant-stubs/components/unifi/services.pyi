from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from typing import Any

SERVICE_RECONNECT_CLIENT: str
SERVICE_REMOVE_CLIENTS: str
SERVICE_RECONNECT_CLIENT_SCHEMA: Incomplete
SUPPORTED_SERVICES: Incomplete
SERVICE_TO_SCHEMA: Incomplete

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
async def async_reconnect_client(hass: HomeAssistant, data: Mapping[str, Any]) -> None: ...
async def async_remove_clients(hass: HomeAssistant, data: Mapping[str, Any]) -> None: ...
