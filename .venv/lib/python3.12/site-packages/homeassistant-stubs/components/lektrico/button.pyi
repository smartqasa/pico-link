from . import LektricoConfigEntry as LektricoConfigEntry, LektricoDeviceDataUpdateCoordinator as LektricoDeviceDataUpdateCoordinator
from .entity import LektricoEntity as LektricoEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import ATTR_SERIAL_NUMBER as ATTR_SERIAL_NUMBER, CONF_TYPE as CONF_TYPE, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from lektricowifi import Device
from typing import Any

@dataclass(frozen=True, kw_only=True)
class LektricoButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[Device], Coroutine[Any, Any, dict[Any, Any]]]

BUTTONS_FOR_CHARGERS: tuple[LektricoButtonEntityDescription, ...]
BUTTONS_FOR_LB_DEVICES: tuple[LektricoButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LektricoConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LektricoButton(LektricoEntity, ButtonEntity):
    entity_description: LektricoButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, description: LektricoButtonEntityDescription, coordinator: LektricoDeviceDataUpdateCoordinator, device_name: str) -> None: ...
    async def async_press(self) -> None: ...
