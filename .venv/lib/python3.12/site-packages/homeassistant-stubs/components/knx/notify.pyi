from . import KNXModule as KNXModule
from .const import KNX_ADDRESS as KNX_ADDRESS, KNX_MODULE_KEY as KNX_MODULE_KEY
from .entity import KnxYamlEntity as KnxYamlEntity
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.notify import NotifyEntity as NotifyEntity
from homeassistant.const import CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType
from xknx import XKNX as XKNX
from xknx.devices import Notification as XknxNotification

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _create_notification_instance(xknx: XKNX, config: ConfigType) -> XknxNotification: ...

class KNXNotify(KnxYamlEntity, NotifyEntity):
    _device: XknxNotification
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...
    async def async_send_message(self, message: str, title: str | None = None) -> None: ...
