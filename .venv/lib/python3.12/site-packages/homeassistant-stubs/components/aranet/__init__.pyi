from _typeshed import Incomplete
from aranet4.client import Aranet4Advertisement
from homeassistant.components.bluetooth import BluetoothScanningMode as BluetoothScanningMode
from homeassistant.components.bluetooth.models import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothProcessorCoordinator as PassiveBluetoothProcessorCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]
_LOGGER: Incomplete
type AranetConfigEntry = ConfigEntry[PassiveBluetoothProcessorCoordinator[Aranet4Advertisement]]

def _service_info_to_adv(service_info: BluetoothServiceInfoBleak) -> Aranet4Advertisement: ...
async def async_setup_entry(hass: HomeAssistant, entry: AranetConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AranetConfigEntry) -> bool: ...
