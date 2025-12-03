import pybotvac
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries, core as core
from homeassistant.components.application_credentials import AuthImplementation as AuthImplementation
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from typing import Any

class ConfigEntryAuth(pybotvac.OAuthSession):
    hass: Incomplete
    session: Incomplete
    def __init__(self, hass: core.HomeAssistant, config_entry: config_entries.ConfigEntry, implementation: config_entry_oauth2_flow.AbstractOAuth2Implementation) -> None: ...
    def refresh_tokens(self) -> str: ...

class NeatoImplementation(AuthImplementation):
    @property
    def extra_authorize_data(self) -> dict[str, Any]: ...
    async def async_generate_authorize_url(self, flow_id: str) -> str: ...
