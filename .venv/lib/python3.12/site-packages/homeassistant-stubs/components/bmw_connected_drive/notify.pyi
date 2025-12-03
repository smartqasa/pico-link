from . import BMWConfigEntry as BMWConfigEntry
from _typeshed import Incomplete
from bimmer_connected.vehicle import MyBMWVehicle
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_TARGET as ATTR_TARGET, BaseNotificationService as BaseNotificationService
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONF_ENTITY_ID as CONF_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

PARALLEL_UPDATES: int
ATTR_LOCATION_ATTRIBUTES: Incomplete
POI_SCHEMA: Incomplete
_LOGGER: Incomplete

def get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> BMWNotificationService: ...

class BMWNotificationService(BaseNotificationService):
    vehicle_targets: dict[str, MyBMWVehicle]
    def __init__(self, targets: dict[str, MyBMWVehicle]) -> None: ...
    @property
    def targets(self) -> dict[str, Any] | None: ...
    async def async_send_message(self, message: str = '', **kwargs: Any) -> None: ...
