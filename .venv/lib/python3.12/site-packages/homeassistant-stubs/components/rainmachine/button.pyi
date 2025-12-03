from . import RainMachineConfigEntry as RainMachineConfigEntry
from .const import DATA_PROVISION_SETTINGS as DATA_PROVISION_SETTINGS
from .entity import RainMachineEntity as RainMachineEntity, RainMachineEntityDescription as RainMachineEntityDescription
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from regenmaschine.controller import Controller as Controller

@dataclass(frozen=True, kw_only=True)
class RainMachineButtonDescription(ButtonEntityDescription, RainMachineEntityDescription):
    push_action: Callable[[Controller], Awaitable]

BUTTON_KIND_REBOOT: str

async def _async_reboot(controller: Controller) -> None: ...

BUTTON_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: RainMachineConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RainMachineButton(RainMachineEntity, ButtonEntity):
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    entity_description: RainMachineButtonDescription
    async def async_press(self) -> None: ...
