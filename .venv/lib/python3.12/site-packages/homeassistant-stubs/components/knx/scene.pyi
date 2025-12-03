from . import KNXModule as KNXModule
from .const import KNX_ADDRESS as KNX_ADDRESS, KNX_MODULE_KEY as KNX_MODULE_KEY
from .entity import KnxYamlEntity as KnxYamlEntity
from .schema import SceneSchema as SceneSchema
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.scene import Scene as Scene
from homeassistant.const import CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any
from xknx.devices import Scene as XknxScene

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class KNXScene(KnxYamlEntity, Scene):
    _device: XknxScene
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...
    async def async_activate(self, **kwargs: Any) -> None: ...
