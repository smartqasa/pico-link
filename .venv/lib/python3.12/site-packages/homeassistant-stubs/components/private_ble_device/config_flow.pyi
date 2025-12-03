from .const import DOMAIN as DOMAIN
from .coordinator import async_last_service_info as async_last_service_info
from _typeshed import Incomplete
from homeassistant.components import bluetooth as bluetooth
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult

_LOGGER: Incomplete
CONF_IRK: str

def _parse_irk(irk: str) -> bytes | None: ...

class BLEDeviceTrackerConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
