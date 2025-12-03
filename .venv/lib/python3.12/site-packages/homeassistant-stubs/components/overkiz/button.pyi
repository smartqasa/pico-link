from . import OverkizDataConfigEntry as OverkizDataConfigEntry
from .const import IGNORED_OVERKIZ_DEVICES as IGNORED_OVERKIZ_DEVICES
from .entity import OverkizDescriptiveEntity as OverkizDescriptiveEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyoverkiz.types import StateType as OverkizStateType

@dataclass(frozen=True)
class OverkizButtonDescription(ButtonEntityDescription):
    press_args: OverkizStateType | None = ...

BUTTON_DESCRIPTIONS: list[OverkizButtonDescription]
SUPPORTED_COMMANDS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: OverkizDataConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OverkizButton(OverkizDescriptiveEntity, ButtonEntity):
    entity_description: OverkizButtonDescription
    async def async_press(self) -> None: ...
