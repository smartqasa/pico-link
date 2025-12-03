from .const import DOMAIN as DOMAIN
from .coordinator import AndroidIPCamConfigEntry as AndroidIPCamConfigEntry, AndroidIPCamDataUpdateCoordinator as AndroidIPCamDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.mjpeg import MjpegCamera as MjpegCamera, filter_urllib3_logging as filter_urllib3_logging
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, HTTP_BASIC_AUTHENTICATION as HTTP_BASIC_AUTHENTICATION
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: AndroidIPCamConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IPWebcamCamera(MjpegCamera):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AndroidIPCamDataUpdateCoordinator) -> None: ...
