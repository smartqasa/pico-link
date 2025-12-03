from .config_flow import CONF_SITE as CONF_SITE, create_omada_client as create_omada_client
from .const import DOMAIN as DOMAIN
from .controller import OmadaSiteController as OmadaSiteController
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from tplink_omada_client.devices import OmadaListDevice as OmadaListDevice

PLATFORMS: list[Platform]
type OmadaConfigEntry = ConfigEntry[OmadaSiteController]

async def async_setup_entry(hass: HomeAssistant, entry: OmadaConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: OmadaConfigEntry) -> bool: ...
def _remove_old_devices(hass: HomeAssistant, entry: OmadaConfigEntry, omada_devices: dict[str, OmadaListDevice]) -> None: ...
