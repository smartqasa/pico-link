from . import KNOWN_DEVICES as KNOWN_DEVICES
from .connection import HKDevice as HKDevice
from .entity import CharacteristicEntity as CharacteristicEntity
from _typeshed import Incomplete
from aiohomekit.model.characteristics import Characteristic as Characteristic
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete

@dataclass(frozen=True)
class HomeKitButtonEntityDescription(ButtonEntityDescription):
    probe: Callable[[Characteristic], bool] | None = ...
    write_value: int | str | None = ...

BUTTON_ENTITIES: dict[str, HomeKitButtonEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BaseHomeKitButton(CharacteristicEntity, ButtonEntity): ...

class HomeKitButton(BaseHomeKitButton):
    entity_description: HomeKitButtonEntityDescription
    def __init__(self, conn: HKDevice, info: ConfigType, char: Characteristic, description: HomeKitButtonEntityDescription) -> None: ...
    def get_characteristic_types(self) -> list[str]: ...
    @property
    def name(self) -> str: ...
    async def async_press(self) -> None: ...

class HomeKitEcobeeClearHoldButton(BaseHomeKitButton):
    def get_characteristic_types(self) -> list[str]: ...
    @property
    def name(self) -> str: ...
    async def async_press(self) -> None: ...

class HomeKitProvisionPreferredThreadCredentials(BaseHomeKitButton):
    _attr_entity_category: Incomplete
    def get_characteristic_types(self) -> list[str]: ...
    @property
    def name(self) -> str: ...
    async def async_press(self) -> None: ...

BUTTON_ENTITY_CLASSES: dict[str, type]
