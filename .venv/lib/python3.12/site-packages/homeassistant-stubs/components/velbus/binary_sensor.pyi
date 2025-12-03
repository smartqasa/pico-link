from . import VelbusConfigEntry as VelbusConfigEntry
from .entity import VelbusEntity as VelbusEntity
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from velbusaio.channels import Button as VelbusButton

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: VelbusConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class VelbusBinarySensor(VelbusEntity, BinarySensorEntity):
    _channel: VelbusButton
    @property
    def is_on(self) -> bool: ...
