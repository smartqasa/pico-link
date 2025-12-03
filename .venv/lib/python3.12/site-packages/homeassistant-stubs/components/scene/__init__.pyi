from _typeshed import Incomplete
from homeassistant.components.light import ATTR_TRANSITION as ATTR_TRANSITION
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PLATFORM as CONF_PLATFORM, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Any, Final, final

DOMAIN: Final[str]
DATA_COMPONENT: HassKey[EntityComponent[Scene]]
STATES: Final[str]

def _hass_domain_validator(config: dict[str, Any]) -> dict[str, Any]: ...
def _platform_validator(config: dict[str, Any]) -> dict[str, Any]: ...

PLATFORM_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class Scene(RestoreEntity):
    _attr_should_poll: bool
    __last_activated: str | None
    @property
    @final
    def state(self) -> str | None: ...
    @final
    async def _async_activate(self, **kwargs: Any) -> None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    def activate(self, **kwargs: Any) -> None: ...
    async def async_activate(self, **kwargs: Any) -> None: ...
