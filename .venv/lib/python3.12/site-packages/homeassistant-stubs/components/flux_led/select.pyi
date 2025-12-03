from .const import CONF_WHITE_CHANNEL_TYPE as CONF_WHITE_CHANNEL_TYPE, DOMAIN as DOMAIN, FLUX_COLOR_MODE_RGBW as FLUX_COLOR_MODE_RGBW
from .coordinator import FluxLedUpdateCoordinator as FluxLedUpdateCoordinator
from .entity import FluxBaseEntity as FluxBaseEntity, FluxEntity as FluxEntity
from .util import _human_readable_option as _human_readable_option
from _typeshed import Incomplete
from flux_led.aio import AIOWifiLedBulb as AIOWifiLedBulb
from homeassistant import config_entries as config_entries
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.const import CONF_NAME as CONF_NAME, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

NAME_TO_POWER_RESTORE_STATE: Incomplete

async def _async_delayed_reload(hass: HomeAssistant, entry: config_entries.ConfigEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FluxConfigAtStartSelect(FluxBaseEntity, SelectEntity):
    _attr_entity_category: Incomplete

class FluxConfigSelect(FluxEntity, SelectEntity):
    _attr_entity_category: Incomplete

class FluxPowerStateSelect(FluxConfigAtStartSelect, SelectEntity):
    _attr_translation_key: str
    _attr_options: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device: AIOWifiLedBulb, entry: config_entries.ConfigEntry) -> None: ...
    _attr_current_option: Incomplete
    @callback
    def _async_set_current_option_from_device(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...

class FluxICTypeSelect(FluxConfigSelect):
    _attr_translation_key: str
    @property
    def options(self) -> list[str]: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...

class FluxWiringsSelect(FluxConfigSelect):
    _attr_translation_key: str
    @property
    def options(self) -> list[str]: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...

class FluxOperatingModesSelect(FluxConfigSelect):
    _attr_translation_key: str
    @property
    def options(self) -> list[str]: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...

class FluxRemoteConfigSelect(FluxConfigSelect):
    _attr_translation_key: str
    _name_to_state: Incomplete
    _attr_options: Incomplete
    def __init__(self, coordinator: FluxLedUpdateCoordinator, base_unique_id: str, key: str) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...

class FluxWhiteChannelSelect(FluxConfigAtStartSelect):
    _attr_translation_key: str
    _attr_options: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device: AIOWifiLedBulb, entry: config_entries.ConfigEntry) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
