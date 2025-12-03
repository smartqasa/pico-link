from .const import DOMAIN as DOMAIN
from .coordinator import FluxLedUpdateCoordinator as FluxLedUpdateCoordinator
from .entity import FluxBaseEntity as FluxBaseEntity
from _typeshed import Incomplete
from flux_led.aio import AIOWifiLedBulb as AIOWifiLedBulb
from homeassistant import config_entries as config_entries
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_RESTART_KEY: str
_UNPAIR_REMOTES_KEY: str
RESTART_BUTTON_DESCRIPTION: Incomplete
UNPAIR_REMOTES_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FluxButton(FluxBaseEntity, ButtonEntity):
    _attr_entity_category: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device: AIOWifiLedBulb, entry: config_entries.ConfigEntry, description: ButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
