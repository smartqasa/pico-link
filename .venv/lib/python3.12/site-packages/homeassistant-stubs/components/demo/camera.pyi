from _typeshed import Incomplete
from homeassistant.components.camera import Camera as Camera, CameraEntityFeature as CameraEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DemoCamera(Camera):
    _attr_is_streaming: bool
    _attr_motion_detection_enabled: bool
    _attr_supported_features: Incomplete
    _attr_name: Incomplete
    content_type: Incomplete
    _images_index: int
    def __init__(self, name: str, content_type: str) -> None: ...
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes: ...
    async def async_enable_motion_detection(self) -> None: ...
    async def async_disable_motion_detection(self) -> None: ...
    _attr_is_on: bool
    async def async_turn_off(self) -> None: ...
    async def async_turn_on(self) -> None: ...

class DemoCameraWithoutStream(DemoCamera):
    _attr_supported_features: Incomplete
