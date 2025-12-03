from .const import CONF_CLIENT_DEVICE_ID as CONF_CLIENT_DEVICE_ID, DOMAIN as DOMAIN, LOGGER as LOGGER, USER_APP_NAME as USER_APP_NAME
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from jellyfin_apiclient_python import JellyfinClient as JellyfinClient
from typing import Any

class JellyfinDataUpdateCoordinator(DataUpdateCoordinator[dict[str, dict[str, Any]]]):
    config_entry: ConfigEntry
    api_client: Incomplete
    server_id: str
    server_name: str
    server_version: str | None
    client_device_id: str
    user_id: str
    session_ids: set[str]
    remote_session_ids: set[str]
    device_ids: set[str]
    def __init__(self, hass: HomeAssistant, api_client: JellyfinClient, system_info: dict[str, Any], user_id: str) -> None: ...
    async def _async_update_data(self) -> dict[str, dict[str, Any]]: ...
