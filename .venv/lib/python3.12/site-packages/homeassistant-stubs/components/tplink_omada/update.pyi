from . import OmadaConfigEntry as OmadaConfigEntry
from .coordinator import OmadaCoordinator as OmadaCoordinator, OmadaDevicesCoordinator as OmadaDevicesCoordinator, POLL_DEVICES as POLL_DEVICES
from .entity import OmadaDeviceEntity as OmadaDeviceEntity
from _typeshed import Incomplete
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tplink_omada_client import OmadaSiteClient as OmadaSiteClient
from tplink_omada_client.devices import OmadaFirmwareUpdate as OmadaFirmwareUpdate, OmadaListDevice as OmadaListDevice
from typing import Any, NamedTuple

POLL_DELAY_UPGRADE: int

class FirmwareUpdateStatus(NamedTuple):
    device: OmadaListDevice
    firmware: OmadaFirmwareUpdate | None

class OmadaFirmwareUpdateCoordinator(OmadaCoordinator[FirmwareUpdateStatus]):
    _devices_coordinator: Incomplete
    _config_entry: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: OmadaConfigEntry, omada_client: OmadaSiteClient, devices_coordinator: OmadaDevicesCoordinator) -> None: ...
    async def _get_firmware_updates(self) -> list[FirmwareUpdateStatus]: ...
    async def poll_update(self) -> dict[str, FirmwareUpdateStatus]: ...
    @callback
    def _handle_devices_update(self) -> None: ...

async def async_setup_entry(hass: HomeAssistant, config_entry: OmadaConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OmadaDeviceUpdate(OmadaDeviceEntity[OmadaFirmwareUpdateCoordinator], UpdateEntity):
    _attr_supported_features: Incomplete
    _attr_device_class: Incomplete
    _mac: Incomplete
    _omada_client: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: OmadaFirmwareUpdateCoordinator, device: OmadaListDevice) -> None: ...
    def release_notes(self) -> str | None: ...
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
    _attr_installed_version: Incomplete
    _attr_latest_version: Incomplete
    _attr_in_progress: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
