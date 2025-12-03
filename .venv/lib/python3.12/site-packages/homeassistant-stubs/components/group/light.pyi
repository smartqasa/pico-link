from .entity import GroupEntity as GroupEntity
from .util import find_state_attributes as find_state_attributes, mean_tuple as mean_tuple, reduce_attribute as reduce_attribute
from _typeshed import Incomplete
from homeassistant.components import light as light
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_MODE as ATTR_COLOR_MODE, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_EFFECT as ATTR_EFFECT, ATTR_EFFECT_LIST as ATTR_EFFECT_LIST, ATTR_FLASH as ATTR_FLASH, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_MAX_COLOR_TEMP_KELVIN as ATTR_MAX_COLOR_TEMP_KELVIN, ATTR_MIN_COLOR_TEMP_KELVIN as ATTR_MIN_COLOR_TEMP_KELVIN, ATTR_RGBWW_COLOR as ATTR_RGBWW_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_SUPPORTED_COLOR_MODES as ATTR_SUPPORTED_COLOR_MODES, ATTR_TRANSITION as ATTR_TRANSITION, ATTR_WHITE as ATTR_WHITE, ATTR_XY_COLOR as ATTR_XY_COLOR, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature, filter_supported_color_modes as filter_supported_color_modes
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

DEFAULT_NAME: str
CONF_ALL: str
PARALLEL_UPDATES: int
PLATFORM_SCHEMA: Incomplete
SUPPORT_GROUP_LIGHT: Incomplete
_LOGGER: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
@callback
def async_create_preview_light(hass: HomeAssistant, name: str, validated_config: dict[str, Any]) -> LightGroup: ...

FORWARDED_ATTRIBUTES: Incomplete

class LightGroup(GroupEntity, LightEntity):
    _attr_available: bool
    _attr_icon: str
    _attr_max_color_temp_kelvin: int
    _attr_min_color_temp_kelvin: int
    _attr_should_poll: bool
    _entity_ids: Incomplete
    _attr_name: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    mode: Incomplete
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    def __init__(self, unique_id: str | None, name: str, entity_ids: list[str], mode: bool | None) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    _attr_brightness: Incomplete
    _attr_hs_color: Incomplete
    _attr_rgb_color: Incomplete
    _attr_rgbw_color: Incomplete
    _attr_rgbww_color: Incomplete
    _attr_xy_color: Incomplete
    _attr_color_temp_kelvin: Incomplete
    _attr_effect_list: Incomplete
    _attr_effect: Incomplete
    _attr_supported_features: Incomplete
    @callback
    def async_update_group_state(self) -> None: ...
