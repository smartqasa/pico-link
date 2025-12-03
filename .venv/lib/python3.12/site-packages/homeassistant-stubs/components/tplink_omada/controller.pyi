from .coordinator import OmadaClientsCoordinator as OmadaClientsCoordinator, OmadaDevicesCoordinator as OmadaDevicesCoordinator, OmadaGatewayCoordinator as OmadaGatewayCoordinator, OmadaSwitchPortCoordinator as OmadaSwitchPortCoordinator
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from tplink_omada_client import OmadaSiteClient as OmadaSiteClient
from tplink_omada_client.devices import OmadaSwitch as OmadaSwitch

class OmadaSiteController:
    _gateway_coordinator: OmadaGatewayCoordinator | None
    _hass: Incomplete
    _omada_client: Incomplete
    _switch_port_coordinators: dict[str, OmadaSwitchPortCoordinator]
    _devices_coordinator: Incomplete
    _clients_coordinator: Incomplete
    def __init__(self, hass: HomeAssistant, omada_client: OmadaSiteClient) -> None: ...
    async def initialize_first_refresh(self) -> None: ...
    @property
    def omada_client(self) -> OmadaSiteClient: ...
    def get_switch_port_coordinator(self, switch: OmadaSwitch) -> OmadaSwitchPortCoordinator: ...
    @property
    def gateway_coordinator(self) -> OmadaGatewayCoordinator | None: ...
    @property
    def devices_coordinator(self) -> OmadaDevicesCoordinator: ...
    @property
    def clients_coordinator(self) -> OmadaClientsCoordinator: ...
