from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyfritzhome import Fritzhome, FritzhomeDevice as FritzhomeDevice
from pyfritzhome.devicetypes import FritzhomeTemplate as FritzhomeTemplate

type FritzboxConfigEntry = ConfigEntry[FritzboxDataUpdateCoordinator]
@dataclass
class FritzboxCoordinatorData:
    devices: dict[str, FritzhomeDevice]
    templates: dict[str, FritzhomeTemplate]
    supported_color_properties: dict[str, tuple[dict, list]]

class FritzboxDataUpdateCoordinator(DataUpdateCoordinator[FritzboxCoordinatorData]):
    config_entry: FritzboxConfigEntry
    configuration_url: str
    fritz: Fritzhome
    has_templates: bool
    new_devices: set[str]
    new_templates: set[str]
    data: Incomplete
    def __init__(self, hass: HomeAssistant, name: str) -> None: ...
    async def async_setup(self) -> None: ...
    def cleanup_removed_devices(self, available_ains: list[str]) -> None: ...
    def _update_fritz_devices(self) -> FritzboxCoordinatorData: ...
    async def _async_update_data(self) -> FritzboxCoordinatorData: ...
