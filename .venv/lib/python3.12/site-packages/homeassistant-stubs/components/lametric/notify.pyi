from .const import CONF_CYCLES as CONF_CYCLES, CONF_ICON_TYPE as CONF_ICON_TYPE, CONF_PRIORITY as CONF_PRIORITY, CONF_SOUND as CONF_SOUND, DOMAIN as DOMAIN
from .coordinator import LaMetricDataUpdateCoordinator as LaMetricDataUpdateCoordinator
from _typeshed import Incomplete
from demetriek import LaMetricDevice as LaMetricDevice
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, BaseNotificationService as BaseNotificationService
from homeassistant.const import CONF_ICON as CONF_ICON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.enum import try_parse_enum as try_parse_enum
from typing import Any

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> LaMetricNotificationService | None: ...

class LaMetricNotificationService(BaseNotificationService):
    lametric: Incomplete
    def __init__(self, lametric: LaMetricDevice) -> None: ...
    async def async_send_message(self, message: str = '', **kwargs: Any) -> None: ...
