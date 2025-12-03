from . import ElkM1ConfigEntry as ElkM1ConfigEntry
from .entity import ElkAttachedEntity as ElkAttachedEntity, ElkEntity as ElkEntity, create_elk_entities as create_elk_entities
from elkm1_lib.tasks import Task as Task
from homeassistant.components.scene import Scene as Scene
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ElkM1ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElkTask(ElkAttachedEntity, Scene):
    _element: Task
    async def async_activate(self, **kwargs: Any) -> None: ...
