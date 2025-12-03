from . import Camera as Camera
from .const import DATA_COMPONENT as DATA_COMPONENT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

def get_camera_from_entity_id(hass: HomeAssistant, entity_id: str) -> Camera: ...
