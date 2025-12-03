from . import KNXModule as KNXModule
from .const import CONF_PAYLOAD_LENGTH as CONF_PAYLOAD_LENGTH, CONF_RESPOND_TO_READ as CONF_RESPOND_TO_READ, CONF_STATE_ADDRESS as CONF_STATE_ADDRESS, CONF_SYNC_STATE as CONF_SYNC_STATE, KNX_ADDRESS as KNX_ADDRESS, KNX_MODULE_KEY as KNX_MODULE_KEY
from .entity import KnxYamlEntity as KnxYamlEntity
from .schema import SelectSchema as SelectSchema
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.const import CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, CONF_PAYLOAD as CONF_PAYLOAD, Platform as Platform, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType
from xknx import XKNX as XKNX
from xknx.devices import Device as XknxDevice, RawValue

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _create_raw_value(xknx: XKNX, config: ConfigType) -> RawValue: ...

class KNXSelect(KnxYamlEntity, SelectEntity, RestoreEntity):
    _device: RawValue
    _option_payloads: dict[str, int]
    _attr_options: Incomplete
    _attr_current_option: Incomplete
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def after_update_callback(self, device: XknxDevice) -> None: ...
    def option_from_payload(self, payload: int | None) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
