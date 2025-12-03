from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.light import ATTR_TRANSITION as ATTR_TRANSITION
from homeassistant.components.scene import STATES as STATES, Scene as Scene
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_STATE as ATTR_STATE, CONF_ENTITIES as CONF_ENTITIES, CONF_ICON as CONF_ICON, CONF_ID as CONF_ID, CONF_NAME as CONF_NAME, CONF_PLATFORM as CONF_PLATFORM, SERVICE_RELOAD as SERVICE_RELOAD, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, State as State, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback, EntityPlatform as EntityPlatform
from homeassistant.helpers.service import async_extract_entity_ids as async_extract_entity_ids, async_register_admin_service as async_register_admin_service
from homeassistant.helpers.state import async_reproduce_state as async_reproduce_state
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.loader import async_get_integration as async_get_integration
from typing import Any, NamedTuple

def _convert_states(states: dict[str, Any]) -> dict[str, State]: ...
def _ensure_no_intersection(value: dict[str, Any]) -> dict[str, Any]: ...

CONF_SCENE_ID: str
CONF_SNAPSHOT: str
DATA_PLATFORM: str
EVENT_SCENE_RELOADED: str
STATES_SCHEMA: Incomplete
PLATFORM_SCHEMA: Incomplete
CREATE_SCENE_SCHEMA: Incomplete
SERVICE_APPLY: str
SERVICE_CREATE: str
SERVICE_DELETE: str
_LOGGER: Incomplete

class SceneConfig(NamedTuple):
    id: str | None
    name: str
    icon: str | None
    states: dict[str, State]

@callback
def scenes_with_entity(hass: HomeAssistant, entity_id: str) -> list[str]: ...
@callback
def entities_in_scene(hass: HomeAssistant, entity_id: str) -> list[str]: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
def _process_scenes_config(hass: HomeAssistant, async_add_entities: AddEntitiesCallback, config: dict[str, Any]) -> None: ...

class HomeAssistantScene(Scene):
    hass: Incomplete
    scene_config: Incomplete
    from_service: Incomplete
    def __init__(self, hass: HomeAssistant, scene_config: SceneConfig, from_service: bool = False) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def icon(self) -> str | None: ...
    @property
    def unique_id(self) -> str | None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any]: ...
    async def async_activate(self, **kwargs: Any) -> None: ...
