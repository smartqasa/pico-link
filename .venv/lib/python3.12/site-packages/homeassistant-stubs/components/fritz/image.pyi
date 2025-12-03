from .const import DOMAIN as DOMAIN
from .coordinator import AvmWrapper as AvmWrapper
from .entity import FritzBoxBaseEntity as FritzBoxBaseEntity
from _typeshed import Incomplete
from homeassistant.components.image import ImageEntity as ImageEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import slugify as slugify

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzGuestWifiQRImage(FritzBoxBaseEntity, ImageEntity):
    _attr_content_type: str
    _attr_entity_category: Incomplete
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _current_qr_bytes: bytes | None
    def __init__(self, hass: HomeAssistant, avm_wrapper: AvmWrapper, device_friendly_name: str, ssid: str) -> None: ...
    async def _fetch_image(self) -> bytes: ...
    _attr_image_last_updated: Incomplete
    async def async_added_to_hass(self) -> None: ...
    async def async_update(self) -> None: ...
    async def async_image(self) -> bytes | None: ...
