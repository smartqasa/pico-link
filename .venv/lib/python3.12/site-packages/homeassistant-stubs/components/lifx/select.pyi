from .const import ATTR_THEME as ATTR_THEME, DOMAIN as DOMAIN, INFRARED_BRIGHTNESS as INFRARED_BRIGHTNESS, INFRARED_BRIGHTNESS_VALUES_MAP as INFRARED_BRIGHTNESS_VALUES_MAP
from .coordinator import LIFXUpdateCoordinator as LIFXUpdateCoordinator
from .entity import LIFXEntity as LIFXEntity
from .util import lifx_features as lifx_features
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

THEME_NAMES: Incomplete
INFRARED_BRIGHTNESS_ENTITY: Incomplete
THEME_ENTITY: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LIFXInfraredBrightnessSelectEntity(LIFXEntity, SelectEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_current_option: Incomplete
    def __init__(self, coordinator: LIFXUpdateCoordinator, description: SelectEntityDescription) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @callback
    def _async_update_attrs(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...

class LIFXThemeSelectEntity(LIFXEntity, SelectEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_current_option: Incomplete
    def __init__(self, coordinator: LIFXUpdateCoordinator, description: SelectEntityDescription) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @callback
    def _async_update_attrs(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
