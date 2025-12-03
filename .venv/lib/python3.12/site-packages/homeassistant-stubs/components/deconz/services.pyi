from .config_flow import get_master_hub as get_master_hub
from .const import CONF_BRIDGE_ID as CONF_BRIDGE_ID, DOMAIN as DOMAIN, LOGGER as LOGGER
from .hub import DeconzHub as DeconzHub
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.util.read_only_dict import ReadOnlyDict as ReadOnlyDict

DECONZ_SERVICES: str
SERVICE_FIELD: str
SERVICE_ENTITY: str
SERVICE_DATA: str
SERVICE_CONFIGURE_DEVICE: str
SERVICE_CONFIGURE_DEVICE_SCHEMA: Incomplete
SERVICE_DEVICE_REFRESH: str
SERVICE_REMOVE_ORPHANED_ENTRIES: str
SELECT_GATEWAY_SCHEMA: Incomplete
SUPPORTED_SERVICES: Incomplete
SERVICE_TO_SCHEMA: Incomplete

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
async def async_configure_service(hub: DeconzHub, data: ReadOnlyDict) -> None: ...
async def async_refresh_devices_service(hub: DeconzHub) -> None: ...
async def async_remove_orphaned_entries_service(hub: DeconzHub) -> None: ...
