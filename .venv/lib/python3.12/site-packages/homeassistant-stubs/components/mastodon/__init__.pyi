from .const import CONF_BASE_URL as CONF_BASE_URL, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import MastodonCoordinator as MastodonCoordinator
from .utils import construct_mastodon_username as construct_mastodon_username, create_mastodon_client as create_mastodon_client
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import discovery as discovery
from homeassistant.util import slugify as slugify
from mastodon.Mastodon import Mastodon as Mastodon

PLATFORMS: list[Platform]

@dataclass
class MastodonData:
    client: Mastodon
    instance: dict
    account: dict
    coordinator: MastodonCoordinator
type MastodonConfigEntry = ConfigEntry[MastodonData]

async def async_setup_entry(hass: HomeAssistant, entry: MastodonConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: MastodonConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: MastodonConfigEntry) -> bool: ...
def setup_mastodon(entry: MastodonConfigEntry) -> tuple[Mastodon, dict, dict]: ...
