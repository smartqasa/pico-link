from . import KNXModule as KNXModule
from .const import CONF_RESPOND_TO_READ as CONF_RESPOND_TO_READ, CONF_STATE_ADDRESS as CONF_STATE_ADDRESS, KNX_ADDRESS as KNX_ADDRESS, KNX_MODULE_KEY as KNX_MODULE_KEY
from .entity import KnxYamlEntity as KnxYamlEntity
from .schema import NumberSchema as NumberSchema
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.number import RestoreNumber as RestoreNumber
from homeassistant.const import CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_MODE as CONF_MODE, CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE, Platform as Platform, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType
from xknx import XKNX as XKNX
from xknx.devices import NumericValue

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _create_numeric_value(xknx: XKNX, config: ConfigType) -> NumericValue: ...

class KNXNumber(KnxYamlEntity, RestoreNumber):
    _device: NumericValue
    _attr_native_max_value: Incomplete
    _attr_native_min_value: Incomplete
    _attr_mode: Incomplete
    _attr_native_step: Incomplete
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def native_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...
