from .const import NEATO_ROBOTS as NEATO_ROBOTS
from .entity import NeatoEntity as NeatoEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pybotvac import Robot as Robot

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NeatoDismissAlertButton(NeatoEntity, ButtonEntity):
    _attr_translation_key: str
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, robot: Robot) -> None: ...
    async def async_press(self) -> None: ...
