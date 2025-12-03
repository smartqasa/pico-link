from . import VelbusConfigEntry as VelbusConfigEntry
from .entity import VelbusEntity as VelbusEntity, api_call as api_call
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from velbusaio.channels import Button as VelbusaioButton, ButtonCounter as VelbusaioButtonCounter

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: VelbusConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class VelbusButton(VelbusEntity, ButtonEntity):
    _channel: VelbusaioButton | VelbusaioButtonCounter
    _attr_entity_registry_enabled_default: bool
    _attr_entity_category: Incomplete
    @api_call
    async def async_press(self) -> None: ...
