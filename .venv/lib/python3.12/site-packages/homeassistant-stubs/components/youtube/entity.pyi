from .const import ATTR_TITLE as ATTR_TITLE, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import YouTubeDataUpdateCoordinator as YouTubeDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class YouTubeChannelEntity(CoordinatorEntity[YouTubeDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _channel_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: YouTubeDataUpdateCoordinator, description: EntityDescription, channel_id: str) -> None: ...
