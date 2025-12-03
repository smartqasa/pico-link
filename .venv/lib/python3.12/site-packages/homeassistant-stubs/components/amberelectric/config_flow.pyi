from .const import CONF_SITE_ID as CONF_SITE_ID, CONF_SITE_NAME as CONF_SITE_NAME, DOMAIN as DOMAIN
from amberelectric.models.site import Site as Site
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_API_TOKEN as CONF_API_TOKEN
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode

API_URL: str

def generate_site_selector_name(site: Site) -> str: ...
def filter_sites(sites: list[Site]) -> list[Site]: ...

class AmberElectricConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _errors: dict[str, str]
    _sites: list[Site] | None
    _api_token: str | None
    def __init__(self) -> None: ...
    def _fetch_sites(self, token: str) -> list[Site] | None: ...
    async def async_step_user(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def async_step_site(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
