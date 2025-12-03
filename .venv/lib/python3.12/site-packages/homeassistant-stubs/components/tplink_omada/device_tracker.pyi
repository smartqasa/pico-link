from . import OmadaConfigEntry as OmadaConfigEntry
from .config_flow import CONF_SITE as CONF_SITE
from .controller import OmadaClientsCoordinator as OmadaClientsCoordinator
from _typeshed import Incomplete
from homeassistant.components.device_tracker import ScannerEntity as ScannerEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from tplink_omada_client.clients import OmadaWirelessClient

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: OmadaConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OmadaClientScannerEntity(CoordinatorEntity[OmadaClientsCoordinator], ScannerEntity):
    _client_details: OmadaWirelessClient | None
    _site_id: Incomplete
    _client_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, site_id: str, client_id: str, display_name: str, coordinator: OmadaClientsCoordinator) -> None: ...
    def _do_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @property
    def ip_address(self) -> str | None: ...
    @property
    def mac_address(self) -> str | None: ...
    @property
    def hostname(self) -> str | None: ...
    @property
    def is_connected(self) -> bool: ...
    @property
    def unique_id(self) -> str | None: ...
