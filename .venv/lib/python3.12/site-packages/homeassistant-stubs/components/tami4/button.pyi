from .const import API as API, DOMAIN as DOMAIN
from .entity import Tami4EdgeBaseEntity as Tami4EdgeBaseEntity
from Tami4EdgeAPI import Tami4EdgeAPI as Tami4EdgeAPI
from Tami4EdgeAPI.drink import Drink as Drink
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class Tami4EdgeButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[Tami4EdgeAPI], None]

@dataclass(frozen=True, kw_only=True)
class Tami4EdgeDrinkButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[Tami4EdgeAPI, Drink], None]

BOIL_WATER_BUTTON: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class Tami4EdgeButton(Tami4EdgeBaseEntity, ButtonEntity):
    entity_description: Tami4EdgeButtonEntityDescription
    def press(self) -> None: ...

class Tami4EdgeDrinkButton(Tami4EdgeBaseEntity, ButtonEntity):
    entity_description: Tami4EdgeDrinkButtonEntityDescription
    drink: Incomplete
    def __init__(self, api: Tami4EdgeAPI, entity_description: EntityDescription, drink: Drink) -> None: ...
    def press(self) -> None: ...
