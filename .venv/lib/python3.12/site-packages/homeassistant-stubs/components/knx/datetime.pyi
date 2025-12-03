from . import KNXModule as KNXModule
from .const import CONF_RESPOND_TO_READ as CONF_RESPOND_TO_READ, CONF_STATE_ADDRESS as CONF_STATE_ADDRESS, CONF_SYNC_STATE as CONF_SYNC_STATE, KNX_ADDRESS as KNX_ADDRESS, KNX_MODULE_KEY as KNX_MODULE_KEY
from .entity import KnxYamlEntity as KnxYamlEntity
from _typeshed import Incomplete
from datetime import datetime
from homeassistant import config_entries as config_entries
from homeassistant.components.datetime import DateTimeEntity as DateTimeEntity
from homeassistant.const import CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, Platform as Platform, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType
from xknx import XKNX as XKNX
from xknx.devices import DateTimeDevice as XknxDateTimeDevice

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _create_xknx_device(xknx: XKNX, config: ConfigType) -> XknxDateTimeDevice: ...

class KNXDateTimeEntity(KnxYamlEntity, DateTimeEntity, RestoreEntity):
    _device: XknxDateTimeDevice
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def native_value(self) -> datetime | None: ...
    async def async_set_value(self, value: datetime) -> None: ...
