from .const import DOMAIN as DOMAIN, _LOGGER as _LOGGER
from .discovery import async_init_discovery_flow as async_init_discovery_flow
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

@callback
def async_migrate_legacy_entries(hass: HomeAssistant, discovered_hosts_by_serial: dict[str, str], existing_serials: set[str], legacy_entry: ConfigEntry) -> int: ...
@callback
def async_migrate_entities_devices(hass: HomeAssistant, legacy_entry_id: str, new_entry: ConfigEntry) -> None: ...
