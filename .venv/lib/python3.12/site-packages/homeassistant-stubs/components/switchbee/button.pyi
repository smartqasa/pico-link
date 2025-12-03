from .const import DOMAIN as DOMAIN
from .coordinator import SwitchBeeCoordinator as SwitchBeeCoordinator
from .entity import SwitchBeeEntity as SwitchBeeEntity
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SwitchBeeButton(SwitchBeeEntity, ButtonEntity):
    async def async_press(self) -> None: ...
