import abc
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from abc import abstractmethod
from aiomealie import MealieClient as MealieClient, Mealplan, MealplanEntryType, ShoppingItem as ShoppingItem, ShoppingList as ShoppingList, Statistics
from dataclasses import dataclass
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

WEEK: Incomplete

@dataclass
class MealieData:
    client: MealieClient
    mealplan_coordinator: MealieMealplanCoordinator
    shoppinglist_coordinator: MealieShoppingListCoordinator
    statistics_coordinator: MealieStatisticsCoordinator
type MealieConfigEntry = ConfigEntry[MealieData]

class MealieDataUpdateCoordinator[_DataT](DataUpdateCoordinator[_DataT], metaclass=abc.ABCMeta):
    config_entry: MealieConfigEntry
    _name: str
    _update_interval: timedelta
    client: Incomplete
    def __init__(self, hass: HomeAssistant, client: MealieClient) -> None: ...
    async def _async_update_data(self) -> _DataT: ...
    @abstractmethod
    async def _async_update_internal(self) -> _DataT: ...

class MealieMealplanCoordinator(MealieDataUpdateCoordinator[dict[MealplanEntryType, list[Mealplan]]]):
    _name: str
    _update_interval: Incomplete
    async def _async_update_internal(self) -> dict[MealplanEntryType, list[Mealplan]]: ...

@dataclass
class ShoppingListData:
    shopping_list: ShoppingList
    items: list[ShoppingItem]

class MealieShoppingListCoordinator(MealieDataUpdateCoordinator[dict[str, ShoppingListData]]):
    _name: str
    _update_interval: Incomplete
    async def _async_update_internal(self) -> dict[str, ShoppingListData]: ...

class MealieStatisticsCoordinator(MealieDataUpdateCoordinator[Statistics]):
    _name: str
    _update_interval: Incomplete
    async def _async_update_internal(self) -> Statistics: ...
