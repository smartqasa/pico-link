from .. import OverkizDataConfigEntry as OverkizDataConfigEntry
from ..entity import OverkizEntity as OverkizEntity
from .atlantic_domestic_hot_water_production_mlb_component import AtlanticDomesticHotWaterProductionMBLComponent as AtlanticDomesticHotWaterProductionMBLComponent
from .atlantic_pass_apc_dhw import AtlanticPassAPCDHW as AtlanticPassAPCDHW
from .domestic_hot_water_production import DomesticHotWaterProduction as DomesticHotWaterProduction
from .hitachi_dhw import HitachiDHW as HitachiDHW
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: OverkizDataConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

WIDGET_TO_WATER_HEATER_ENTITY: Incomplete
CONTROLLABLE_NAME_TO_WATER_HEATER_ENTITY: Incomplete
