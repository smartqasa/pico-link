from .const import CONF_CYCLES as CONF_CYCLES, CONF_DATA as CONF_DATA, CONF_ICON_TYPE as CONF_ICON_TYPE, CONF_MESSAGE as CONF_MESSAGE, CONF_PRIORITY as CONF_PRIORITY, CONF_SOUND as CONF_SOUND, DOMAIN as DOMAIN, SERVICE_CHART as SERVICE_CHART, SERVICE_MESSAGE as SERVICE_MESSAGE
from .coordinator import LaMetricDataUpdateCoordinator as LaMetricDataUpdateCoordinator
from .helpers import async_get_coordinator_by_device_id as async_get_coordinator_by_device_id
from _typeshed import Incomplete
from demetriek import Chart, Goal as Goal, Simple
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_ICON as CONF_ICON
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.util.enum import try_parse_enum as try_parse_enum

SERVICE_BASE_SCHEMA: Incomplete
SERVICE_MESSAGE_SCHEMA: Incomplete
SERVICE_CHART_SCHEMA: Incomplete

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
async def async_send_notification(coordinator: LaMetricDataUpdateCoordinator, call: ServiceCall, frames: list[Chart | Goal | Simple]) -> None: ...
