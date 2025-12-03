from . import RingConfigEntry as RingConfigEntry
from .coordinator import RingDataCoordinator as RingDataCoordinator
from .entity import RingEntity as RingEntity, exception_wrap as exception_wrap
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from ring_doorbell import RingOther

BUTTON_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: RingConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RingDoorButton(RingEntity[RingOther], ButtonEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device: RingOther, coordinator: RingDataCoordinator, description: ButtonEntityDescription) -> None: ...
    @exception_wrap
    async def async_press(self) -> None: ...
