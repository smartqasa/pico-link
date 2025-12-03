from . import OmadaConfigEntry as OmadaConfigEntry
from .controller import OmadaGatewayCoordinator as OmadaGatewayCoordinator, OmadaSwitchPortCoordinator as OmadaSwitchPortCoordinator
from .coordinator import OmadaCoordinator as OmadaCoordinator
from .entity import OmadaDeviceEntity as OmadaDeviceEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tplink_omada_client import OmadaSiteClient as OmadaSiteClient
from tplink_omada_client.devices import OmadaDevice as OmadaDevice, OmadaGateway, OmadaGatewayPortConfig, OmadaGatewayPortStatus, OmadaSwitch, OmadaSwitchPortDetails
from typing import Any, Generic, TypeVar

TPort = TypeVar('TPort')
TDevice = TypeVar('TDevice', bound='OmadaDevice')
TCoordinator = TypeVar('TCoordinator', bound='OmadaCoordinator[Any]')

async def async_setup_entry(hass: HomeAssistant, config_entry: OmadaConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _get_switch_port_base_name(port: OmadaSwitchPortDetails) -> str: ...

@dataclass(frozen=True, kw_only=True)
class OmadaDevicePortSwitchEntityDescription(SwitchEntityDescription, Generic[TCoordinator, TDevice, TPort]):
    exists_func: Callable[[TDevice, TPort], bool] = ...
    coordinator_update_func: Callable[[TCoordinator, TDevice, TPort], TPort | None]
    set_func: Callable[[OmadaSiteClient, TDevice, TPort, bool], Awaitable[TPort | None]]
    update_func: Callable[[TPort], bool]

@dataclass(frozen=True, kw_only=True)
class OmadaSwitchPortSwitchEntityDescription(OmadaDevicePortSwitchEntityDescription[OmadaSwitchPortCoordinator, OmadaSwitch, OmadaSwitchPortDetails]):
    coordinator_update_func: Callable[[OmadaSwitchPortCoordinator, OmadaSwitch, OmadaSwitchPortDetails], OmadaSwitchPortDetails | None] = ...

@dataclass(frozen=True, kw_only=True)
class OmadaGatewayPortConfigSwitchEntityDescription(OmadaDevicePortSwitchEntityDescription[OmadaGatewayCoordinator, OmadaGateway, OmadaGatewayPortConfig]):
    coordinator_update_func: Callable[[OmadaGatewayCoordinator, OmadaGateway, OmadaGatewayPortConfig], OmadaGatewayPortConfig | None] = ...

@dataclass(frozen=True, kw_only=True)
class OmadaGatewayPortStatusSwitchEntityDescription(OmadaDevicePortSwitchEntityDescription[OmadaGatewayCoordinator, OmadaGateway, OmadaGatewayPortStatus]):
    coordinator_update_func: Callable[[OmadaGatewayCoordinator, OmadaGateway, OmadaGatewayPortStatus], OmadaGatewayPortStatus] = ...

async def _wan_connect_disconnect(client: OmadaSiteClient, device: OmadaDevice, port: OmadaGatewayPortStatus, enable: bool, ipv6: bool) -> None: ...

SWITCH_PORT_DETAILS_SWITCHES: list[OmadaSwitchPortSwitchEntityDescription]
GATEWAY_PORT_STATUS_SWITCHES: list[OmadaGatewayPortStatusSwitchEntityDescription]
GATEWAY_PORT_CONFIG_SWITCHES: list[OmadaGatewayPortConfigSwitchEntityDescription]

class OmadaDevicePortSwitchEntity(OmadaDeviceEntity[TCoordinator], SwitchEntity, Generic[TCoordinator, TDevice, TPort]):
    entity_description: OmadaDevicePortSwitchEntityDescription[TCoordinator, TDevice, TPort]
    _device: Incomplete
    _port_details: Incomplete
    _attr_unique_id: Incomplete
    _attr_translation_placeholders: Incomplete
    def __init__(self, coordinator: TCoordinator, device: TDevice, port_details: TPort, port_id: str, entity_description: OmadaDevicePortSwitchEntityDescription[TCoordinator, TDevice, TPort], port_name: str | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_is_on: Incomplete
    async def _async_turn_on_off(self, enable: bool) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def available(self) -> bool: ...
    def _do_update(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
