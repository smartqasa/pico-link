from . import BondConfigEntry as BondConfigEntry
from .entity import BondEntity as BondEntity
from .models import BondData as BondData
from .utils import BondDevice as BondDevice
from _typeshed import Incomplete
from bond_async import Action
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

STEP_SIZE: int

@dataclass(frozen=True, kw_only=True)
class BondButtonEntityDescription(ButtonEntityDescription):
    name: str | None = ...
    mutually_exclusive: Action | None
    argument: int | None

STOP_BUTTON: Incomplete
BUTTONS: tuple[BondButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: BondConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BondButtonEntity(BondEntity, ButtonEntity):
    entity_description: BondButtonEntityDescription
    def __init__(self, data: BondData, device: BondDevice, description: BondButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
    def _apply_state(self) -> None: ...
