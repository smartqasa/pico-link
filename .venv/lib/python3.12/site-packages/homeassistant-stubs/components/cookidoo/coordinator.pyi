from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from cookidoo_api import Cookidoo as Cookidoo, CookidooAdditionalItem as CookidooAdditionalItem, CookidooIngredientItem as CookidooIngredientItem
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_EMAIL as CONF_EMAIL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
type CookidooConfigEntry = ConfigEntry[CookidooDataUpdateCoordinator]

@dataclass
class CookidooData:
    ingredient_items: list[CookidooIngredientItem]
    additional_items: list[CookidooAdditionalItem]

class CookidooDataUpdateCoordinator(DataUpdateCoordinator[CookidooData]):
    config_entry: CookidooConfigEntry
    cookidoo: Incomplete
    def __init__(self, hass: HomeAssistant, cookidoo: Cookidoo, entry: CookidooConfigEntry) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> CookidooData: ...
