from . import SensiboConfigEntry as SensiboConfigEntry
from .coordinator import SensiboDataUpdateCoordinator as SensiboDataUpdateCoordinator
from .entity import SensiboDeviceBaseEntity as SensiboDeviceBaseEntity, async_handle_api_call as async_handle_api_call
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class SensiboButtonEntityDescription(ButtonEntityDescription):
    data_key: str

DEVICE_BUTTON_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SensiboConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SensiboDeviceButton(SensiboDeviceBaseEntity, ButtonEntity):
    entity_description: SensiboButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SensiboDataUpdateCoordinator, device_id: str, entity_description: SensiboButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
    @async_handle_api_call
    async def async_send_api_call(self, key: str, value: Any) -> bool: ...
