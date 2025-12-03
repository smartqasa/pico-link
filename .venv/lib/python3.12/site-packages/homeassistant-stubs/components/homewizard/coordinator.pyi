from .const import DOMAIN as DOMAIN, DeviceResponseEntry as DeviceResponseEntry, UPDATE_INTERVAL as UPDATE_INTERVAL
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homewizard_energy import HomeWizardEnergyV1
from homewizard_energy.v1.models import Device as Device

_LOGGER: Incomplete

class HWEnergyDeviceUpdateCoordinator(DataUpdateCoordinator[DeviceResponseEntry]):
    api: HomeWizardEnergyV1
    api_disabled: bool
    _unsupported_error: bool
    config_entry: ConfigEntry
    def __init__(self, hass: HomeAssistant) -> None: ...
    data: Incomplete
    async def _async_update_data(self) -> DeviceResponseEntry: ...
    def supports_state(self, device: Device | None = None) -> bool: ...
    def supports_identify(self, device: Device | None = None) -> bool: ...
