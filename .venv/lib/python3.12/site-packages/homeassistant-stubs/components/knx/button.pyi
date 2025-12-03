from . import KNXModule as KNXModule
from .const import CONF_PAYLOAD_LENGTH as CONF_PAYLOAD_LENGTH, KNX_ADDRESS as KNX_ADDRESS, KNX_MODULE_KEY as KNX_MODULE_KEY
from .entity import KnxYamlEntity as KnxYamlEntity
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.const import CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, CONF_PAYLOAD as CONF_PAYLOAD, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType
from xknx.devices import RawValue as XknxRawValue

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class KNXButton(KnxYamlEntity, ButtonEntity):
    _device: XknxRawValue
    _payload: Incomplete
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...
    async def async_press(self) -> None: ...
