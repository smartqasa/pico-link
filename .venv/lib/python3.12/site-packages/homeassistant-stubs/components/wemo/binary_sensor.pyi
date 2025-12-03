from . import async_wemo_dispatcher_connect as async_wemo_dispatcher_connect
from .coordinator import DeviceCoordinator as DeviceCoordinator
from .entity import WemoBinaryStateEntity as WemoBinaryStateEntity, WemoEntity as WemoEntity
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pywemo import Insight, Maker

async def async_setup_entry(hass: HomeAssistant, _config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WemoBinarySensor(WemoBinaryStateEntity, BinarySensorEntity): ...

class MakerBinarySensor(WemoEntity, BinarySensorEntity):
    _name_suffix: str
    wemo: Maker
    @property
    def is_on(self) -> bool: ...

class InsightBinarySensor(WemoBinarySensor):
    _name_suffix: str
    wemo: Insight
    @property
    def is_on(self) -> bool: ...
