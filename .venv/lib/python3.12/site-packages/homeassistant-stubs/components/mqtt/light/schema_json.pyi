from .. import subscription as subscription
from ..config import DEFAULT_QOS as DEFAULT_QOS, DEFAULT_RETAIN as DEFAULT_RETAIN, MQTT_RW_SCHEMA as MQTT_RW_SCHEMA
from ..const import CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_QOS as CONF_QOS, CONF_RETAIN as CONF_RETAIN, CONF_STATE_TOPIC as CONF_STATE_TOPIC
from ..entity import MqttEntity as MqttEntity
from ..models import ReceiveMessage as ReceiveMessage
from ..schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from ..util import valid_subscribe_topic as valid_subscribe_topic
from .schema import MQTT_LIGHT_SCHEMA_SCHEMA as MQTT_LIGHT_SCHEMA_SCHEMA
from .schema_basic import CONF_BRIGHTNESS_SCALE as CONF_BRIGHTNESS_SCALE, CONF_WHITE_SCALE as CONF_WHITE_SCALE, MQTT_LIGHT_ATTRIBUTES_BLOCKED as MQTT_LIGHT_ATTRIBUTES_BLOCKED
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_MODE as ATTR_COLOR_MODE, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_EFFECT as ATTR_EFFECT, ATTR_FLASH as ATTR_FLASH, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_RGBWW_COLOR as ATTR_RGBWW_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ATTR_WHITE as ATTR_WHITE, ATTR_XY_COLOR as ATTR_XY_COLOR, ColorMode as ColorMode, DEFAULT_MAX_KELVIN as DEFAULT_MAX_KELVIN, DEFAULT_MIN_KELVIN as DEFAULT_MIN_KELVIN, ENTITY_ID_FORMAT as ENTITY_ID_FORMAT, FLASH_LONG as FLASH_LONG, FLASH_SHORT as FLASH_SHORT, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature, VALID_COLOR_MODES as VALID_COLOR_MODES, brightness_supported as brightness_supported, color_supported as color_supported, filter_supported_color_modes as filter_supported_color_modes, valid_supported_color_modes as valid_supported_color_modes
from homeassistant.const import CONF_BRIGHTNESS as CONF_BRIGHTNESS, CONF_COLOR_TEMP as CONF_COLOR_TEMP, CONF_EFFECT as CONF_EFFECT, CONF_HS as CONF_HS, CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_RGB as CONF_RGB, CONF_XY as CONF_XY, STATE_ON as STATE_ON
from homeassistant.core import async_get_hass as async_get_hass, callback as callback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.json import json_dumps as json_dumps
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, VolSchemaType as VolSchemaType
from homeassistant.util.json import json_loads_object as json_loads_object
from typing import Any

_LOGGER: Incomplete
DOMAIN: str
DEFAULT_BRIGHTNESS: bool
DEFAULT_COLOR_MODE: bool
DEFAULT_COLOR_TEMP: bool
DEFAULT_EFFECT: bool
DEFAULT_FLASH_TIME_LONG: int
DEFAULT_FLASH_TIME_SHORT: int
DEFAULT_NAME: str
DEFAULT_RGB: bool
DEFAULT_XY: bool
DEFAULT_HS: bool
DEFAULT_BRIGHTNESS_SCALE: int
DEFAULT_WHITE_SCALE: int
CONF_COLOR_MODE: str
CONF_SUPPORTED_COLOR_MODES: str
CONF_EFFECT_LIST: str
CONF_FLASH_TIME_LONG: str
CONF_FLASH_TIME_SHORT: str
CONF_MAX_MIREDS: str
CONF_MIN_MIREDS: str

def valid_color_configuration(setup_from_yaml: bool) -> Callable[[dict[str, Any]], dict[str, Any]]: ...

_PLATFORM_SCHEMA_BASE: Incomplete
DISCOVERY_SCHEMA_JSON: Incomplete
PLATFORM_SCHEMA_MODERN_JSON: Incomplete

class MqttLightJson(MqttEntity, LightEntity, RestoreEntity):
    _default_name = DEFAULT_NAME
    _entity_id_format = ENTITY_ID_FORMAT
    _attributes_extra_blocked = MQTT_LIGHT_ATTRIBUTES_BLOCKED
    _fixed_color_mode: ColorMode | str | None
    _flash_times: dict[str, int | None]
    _topic: dict[str, str | None]
    _optimistic: bool
    _deprecated_color_handling: bool
    @staticmethod
    def config_schema() -> VolSchemaType: ...
    _attr_min_color_temp_kelvin: Incomplete
    _attr_max_color_temp_kelvin: Incomplete
    _attr_effect_list: Incomplete
    _attr_assumed_state: Incomplete
    _attr_supported_features: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _attr_hs_color: Incomplete
    _attr_color_temp_kelvin: Incomplete
    _attr_rgb_color: Incomplete
    _attr_rgbw_color: Incomplete
    _attr_rgbww_color: Incomplete
    _attr_xy_color: Incomplete
    def _update_color(self, values: dict[str, Any]) -> None: ...
    _attr_is_on: bool
    _attr_brightness: Incomplete
    _attr_effect: Incomplete
    @callback
    def _state_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    @property
    def color_mode(self) -> ColorMode | str | None: ...
    def _set_flash_and_transition(self, message: dict[str, Any], **kwargs: Any) -> None: ...
    def _scale_rgbxx(self, rgbxx: tuple[int, ...], kwargs: Any) -> tuple[int, ...]: ...
    def _supports_color_mode(self, color_mode: ColorMode | str) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
