from .const import DOMAIN as DOMAIN, SERVICE_RANDOMIZE_DEVICE_TRACKER_DATA as SERVICE_RANDOMIZE_DEVICE_TRACKER_DATA
from homeassistant.components.device_tracker import SeeCallback as SeeCallback
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

def setup_scanner(hass: HomeAssistant, config: ConfigType, see: SeeCallback, discovery_info: DiscoveryInfoType | None = None) -> bool: ...
