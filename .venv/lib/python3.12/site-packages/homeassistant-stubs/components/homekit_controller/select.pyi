from . import KNOWN_DEVICES as KNOWN_DEVICES
from .connection import HKDevice as HKDevice
from .entity import CharacteristicEntity as CharacteristicEntity
from _typeshed import Incomplete
from aiohomekit.model.characteristics import Characteristic as Characteristic
from dataclasses import dataclass
from enum import IntEnum
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType

@dataclass(frozen=True, kw_only=True)
class HomeKitSelectEntityDescription(SelectEntityDescription):
    choices: dict[str, IntEnum]
    name: str | None = ...

SELECT_ENTITIES: dict[str, HomeKitSelectEntityDescription]
_ECOBEE_MODE_TO_TEXT: Incomplete
_ECOBEE_MODE_TO_NUMBERS: Incomplete

class BaseHomeKitSelect(CharacteristicEntity, SelectEntity): ...

class HomeKitSelect(BaseHomeKitSelect):
    entity_description: HomeKitSelectEntityDescription
    _choice_to_enum: Incomplete
    _enum_to_choice: Incomplete
    _attr_options: Incomplete
    def __init__(self, conn: HKDevice, info: ConfigType, char: Characteristic, description: HomeKitSelectEntityDescription) -> None: ...
    def get_characteristic_types(self) -> list[str]: ...
    @property
    def name(self) -> str | None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...

class EcobeeModeSelect(BaseHomeKitSelect):
    _attr_options: Incomplete
    _attr_translation_key: str
    @property
    def name(self) -> str: ...
    def get_characteristic_types(self) -> list[str]: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
