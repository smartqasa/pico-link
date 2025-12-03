from . import UnifiConfigEntry as UnifiConfigEntry
from .entity import HandlerT as HandlerT, UnifiEntity as UnifiEntity, UnifiEntityDescription as UnifiEntityDescription, async_wlan_available_fn as async_wlan_available_fn, async_wlan_device_info_fn as async_wlan_device_info_fn
from .hub import UnifiHub as UnifiHub
from _typeshed import Incomplete
from aiounifi.interfaces.api_handlers import ItemEvent as ItemEvent
from aiounifi.models.api import ApiItemT
from aiounifi.models.wlan import Wlan
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.image import ImageEntity as ImageEntity, ImageEntityDescription as ImageEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@callback
def async_wlan_qr_code_image_fn(hub: UnifiHub, wlan: Wlan) -> bytes: ...

@dataclass(frozen=True, kw_only=True)
class UnifiImageEntityDescription(ImageEntityDescription, UnifiEntityDescription[HandlerT, ApiItemT]):
    image_fn: Callable[[UnifiHub, ApiItemT], bytes]
    value_fn: Callable[[ApiItemT], str | None]

ENTITY_DESCRIPTIONS: tuple[UnifiImageEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: UnifiConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class UnifiImageEntity(UnifiEntity[HandlerT, ApiItemT], ImageEntity):
    entity_description: UnifiImageEntityDescription[HandlerT, ApiItemT]
    _attr_content_type: str
    current_image: bytes | None
    previous_value: str | None
    def __init__(self, obj_id: str, hub: UnifiHub, description: UnifiEntityDescription[HandlerT, ApiItemT]) -> None: ...
    def image(self) -> bytes | None: ...
    _attr_image_last_updated: Incomplete
    @callback
    def async_update_state(self, event: ItemEvent, obj_id: str) -> None: ...
