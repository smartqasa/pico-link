from . import EcovacsConfigEntry as EcovacsConfigEntry
from .entity import EcovacsEntity as EcovacsEntity
from _typeshed import Incomplete
from deebot_client.capabilities import Capabilities
from deebot_client.device import Device as Device
from deebot_client.events import StateEvent as StateEvent
from deebot_client.models import CleanAction
from homeassistant.components.lawn_mower import LawnMowerActivity as LawnMowerActivity, LawnMowerEntity as LawnMowerEntity, LawnMowerEntityEntityDescription as LawnMowerEntityEntityDescription, LawnMowerEntityFeature as LawnMowerEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete
_STATE_TO_MOWER_STATE: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: EcovacsConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EcovacsMower(EcovacsEntity[Capabilities], LawnMowerEntity):
    _attr_supported_features: Incomplete
    entity_description: Incomplete
    def __init__(self, device: Device) -> None: ...
    _attr_activity: Incomplete
    async def async_added_to_hass(self) -> None: ...
    async def _clean_command(self, action: CleanAction) -> None: ...
    async def async_start_mowing(self) -> None: ...
    async def async_pause(self) -> None: ...
    async def async_dock(self) -> None: ...
