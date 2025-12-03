from .const import DOMAIN as DOMAIN, IDENTIFY as IDENTIFY, RESTART as RESTART
from .coordinator import LIFXUpdateCoordinator as LIFXUpdateCoordinator
from .entity import LIFXEntity as LIFXEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

RESTART_BUTTON_DESCRIPTION: Incomplete
IDENTIFY_BUTTON_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LIFXButton(LIFXEntity, ButtonEntity):
    _attr_should_poll: bool
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LIFXUpdateCoordinator) -> None: ...

class LIFXRestartButton(LIFXButton):
    entity_description = RESTART_BUTTON_DESCRIPTION
    async def async_press(self) -> None: ...

class LIFXIdentifyButton(LIFXButton):
    entity_description = IDENTIFY_BUTTON_DESCRIPTION
    async def async_press(self) -> None: ...
