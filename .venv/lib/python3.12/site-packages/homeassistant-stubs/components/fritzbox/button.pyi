from .const import DOMAIN as DOMAIN
from .coordinator import FritzboxConfigEntry as FritzboxConfigEntry
from .entity import FritzBoxEntity as FritzBoxEntity
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyfritzhome.devicetypes import FritzhomeTemplate as FritzhomeTemplate

async def async_setup_entry(hass: HomeAssistant, entry: FritzboxConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzBoxTemplate(FritzBoxEntity, ButtonEntity):
    @property
    def data(self) -> FritzhomeTemplate: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    async def async_press(self) -> None: ...
    def apply_template(self) -> None: ...
