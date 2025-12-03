from _typeshed import Incomplete
from collections.abc import Iterable
from enum import IntFlag
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_COMMAND as ATTR_COMMAND, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity, ToggleEntityDescription as ToggleEntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.hass_dict import HassKey as HassKey
from propcache import cached_property
from typing import Any, final

_LOGGER: Incomplete
DOMAIN: str
DATA_COMPONENT: HassKey[EntityComponent[RemoteEntity]]
ENTITY_ID_FORMAT: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete
ATTR_ACTIVITY: str
ATTR_ACTIVITY_LIST: str
ATTR_CURRENT_ACTIVITY: str
ATTR_COMMAND_TYPE: str
ATTR_DEVICE: str
ATTR_NUM_REPEATS: str
ATTR_DELAY_SECS: str
ATTR_HOLD_SECS: str
ATTR_ALTERNATIVE: str
ATTR_TIMEOUT: str
MIN_TIME_BETWEEN_SCANS: Incomplete
SERVICE_SEND_COMMAND: str
SERVICE_LEARN_COMMAND: str
SERVICE_DELETE_COMMAND: str
SERVICE_SYNC: str
DEFAULT_NUM_REPEATS: int
DEFAULT_DELAY_SECS: float
DEFAULT_HOLD_SECS: int

class RemoteEntityFeature(IntFlag):
    LEARN_COMMAND = 1
    DELETE_COMMAND = 2
    ACTIVITY = 4

REMOTE_SERVICE_ACTIVITY_SCHEMA: Incomplete

@bind_hass
def is_on(hass: HomeAssistant, entity_id: str) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class RemoteEntityDescription(ToggleEntityDescription, frozen_or_thawed=True): ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class RemoteEntity(ToggleEntity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: RemoteEntityDescription
    _attr_activity_list: list[str] | None
    _attr_current_activity: str | None
    _attr_supported_features: RemoteEntityFeature
    @cached_property
    def supported_features(self) -> RemoteEntityFeature: ...
    @cached_property
    def current_activity(self) -> str | None: ...
    @cached_property
    def activity_list(self) -> list[str] | None: ...
    @final
    @property
    def state_attributes(self) -> dict[str, Any] | None: ...
    def send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
    async def async_send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
    def learn_command(self, **kwargs: Any) -> None: ...
    async def async_learn_command(self, **kwargs: Any) -> None: ...
    def delete_command(self, **kwargs: Any) -> None: ...
    async def async_delete_command(self, **kwargs: Any) -> None: ...
