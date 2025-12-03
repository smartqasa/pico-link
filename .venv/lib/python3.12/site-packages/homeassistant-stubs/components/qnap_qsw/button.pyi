from .const import DOMAIN as DOMAIN, QSW_COORD_DATA as QSW_COORD_DATA, QSW_REBOOT as QSW_REBOOT
from .coordinator import QswDataCoordinator as QswDataCoordinator
from .entity import QswDataEntity as QswDataEntity
from _typeshed import Incomplete
from aioqsw.localapi import QnapQswApi as QnapQswApi
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Final

@dataclass(frozen=True, kw_only=True)
class QswButtonDescription(ButtonEntityDescription):
    press_action: Callable[[QnapQswApi], Awaitable[bool]]

BUTTON_TYPES: Final[tuple[QswButtonDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class QswButton(QswDataEntity, ButtonEntity):
    _attr_has_entity_name: bool
    entity_description: QswButtonDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: QswDataCoordinator, description: QswButtonDescription, entry: ConfigEntry) -> None: ...
    async def async_press(self) -> None: ...
