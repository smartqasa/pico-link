from . import YaleConfigEntry as YaleConfigEntry
from .const import DOMAIN as DOMAIN, YALE_ALL_ERRORS as YALE_ALL_ERRORS
from .coordinator import YaleDataUpdateCoordinator as YaleDataUpdateCoordinator
from .entity import YaleAlarmEntity as YaleAlarmEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

BUTTON_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: YaleConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class YalePanicButton(YaleAlarmEntity, ButtonEntity):
    entity_description: ButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: YaleDataUpdateCoordinator, description: ButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
