import voluptuous as vol
from .const import DOMAIN as DOMAIN, FRITZ_SERVICES as FRITZ_SERVICES, SERVICE_SET_GUEST_WIFI_PW as SERVICE_SET_GUEST_WIFI_PW
from .coordinator import AvmWrapper as AvmWrapper
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.service import async_extract_config_entry_ids as async_extract_config_entry_ids

_LOGGER: Incomplete
SERVICE_SCHEMA_SET_GUEST_WIFI_PW: Incomplete
SERVICE_LIST: list[tuple[str, vol.Schema | None]]

async def async_setup_services(hass: HomeAssistant) -> None: ...
async def _async_get_configured_avm_device(hass: HomeAssistant, service_call: ServiceCall) -> list: ...
async def async_unload_services(hass: HomeAssistant) -> None: ...
