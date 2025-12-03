from .const import CONF_SERIAL as CONF_SERIAL, DOMAIN as DOMAIN, SERVICES as SERVICES, SERVICE_REBOOT as SERVICE_REBOOT, SERVICE_SHUTDOWN as SERVICE_SHUTDOWN
from .models import SynologyDSMData as SynologyDSMData
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall

LOGGER: Incomplete

async def async_setup_services(hass: HomeAssistant) -> None: ...
