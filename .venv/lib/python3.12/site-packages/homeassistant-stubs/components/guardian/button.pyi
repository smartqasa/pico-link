from . import GuardianData as GuardianData
from .const import API_SYSTEM_DIAGNOSTICS as API_SYSTEM_DIAGNOSTICS, DOMAIN as DOMAIN
from .entity import ValveControllerEntity as ValveControllerEntity, ValveControllerEntityDescription as ValveControllerEntityDescription
from .util import convert_exceptions_to_homeassistant_error as convert_exceptions_to_homeassistant_error
from _typeshed import Incomplete
from aioguardian import Client as Client
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class ValveControllerButtonDescription(ButtonEntityDescription, ValveControllerEntityDescription):
    push_action: Callable[[Client], Awaitable]

BUTTON_KIND_REBOOT: str
BUTTON_KIND_RESET_VALVE_DIAGNOSTICS: str

async def _async_reboot(client: Client) -> None: ...
async def _async_valve_reset(client: Client) -> None: ...

BUTTON_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class GuardianButton(ValveControllerEntity, ButtonEntity):
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    entity_description: ValveControllerButtonDescription
    _client: Incomplete
    def __init__(self, entry: ConfigEntry, data: GuardianData, description: ValveControllerButtonDescription) -> None: ...
    @convert_exceptions_to_homeassistant_error
    async def async_press(self) -> None: ...
