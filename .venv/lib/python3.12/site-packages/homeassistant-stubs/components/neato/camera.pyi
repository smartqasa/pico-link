from .const import NEATO_LOGIN as NEATO_LOGIN, NEATO_MAP_DATA as NEATO_MAP_DATA, NEATO_ROBOTS as NEATO_ROBOTS, SCAN_INTERVAL_MINUTES as SCAN_INTERVAL_MINUTES
from .entity import NeatoEntity as NeatoEntity
from .hub import NeatoHub as NeatoHub
from _typeshed import Incomplete
from homeassistant.components.camera import Camera as Camera
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pybotvac.robot import Robot as Robot
from typing import Any

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
ATTR_GENERATED_AT: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NeatoCleaningMap(NeatoEntity, Camera):
    _attr_translation_key: str
    neato: Incomplete
    _mapdata: Incomplete
    _available: Incomplete
    _robot_serial: str
    _attr_unique_id: Incomplete
    _generated_at: str | None
    _image_url: str | None
    _image: bytes | None
    def __init__(self, neato: NeatoHub, robot: Robot, mapdata: dict[str, Any] | None) -> None: ...
    def camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
    def update(self) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
