from .const import BLOCK_MAX_TRANSITION_TIME_MS as BLOCK_MAX_TRANSITION_TIME_MS, DUAL_MODE_LIGHT_MODELS as DUAL_MODE_LIGHT_MODELS, KELVIN_MAX_VALUE as KELVIN_MAX_VALUE, KELVIN_MIN_VALUE_COLOR as KELVIN_MIN_VALUE_COLOR, KELVIN_MIN_VALUE_WHITE as KELVIN_MIN_VALUE_WHITE, LOGGER as LOGGER, MODELS_SUPPORTING_LIGHT_TRANSITION as MODELS_SUPPORTING_LIGHT_TRANSITION, RGBW_MODELS as RGBW_MODELS, RPC_MIN_TRANSITION_TIME_SEC as RPC_MIN_TRANSITION_TIME_SEC, SHBLB_1_RGB_EFFECTS as SHBLB_1_RGB_EFFECTS, STANDARD_RGB_EFFECTS as STANDARD_RGB_EFFECTS
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyConfigEntry as ShellyConfigEntry, ShellyRpcCoordinator as ShellyRpcCoordinator
from .entity import ShellyBlockEntity as ShellyBlockEntity, ShellyRpcEntity as ShellyRpcEntity
from .utils import async_remove_orphaned_entities as async_remove_orphaned_entities, async_remove_shelly_entity as async_remove_shelly_entity, brightness_to_percentage as brightness_to_percentage, get_device_entry_gen as get_device_entry_gen, get_rpc_key_ids as get_rpc_key_ids, is_block_channel_type_light as is_block_channel_type_light, is_rpc_channel_type_light as is_rpc_channel_type_light, percentage_to_brightness as percentage_to_brightness
from _typeshed import Incomplete
from aioshelly.block_device import Block as Block
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_EFFECT as ATTR_EFFECT, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature, brightness_supported as brightness_supported
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
@callback
def async_setup_block_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
@callback
def async_setup_rpc_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BlockShellyLight(ShellyBlockEntity, LightEntity):
    _attr_supported_color_modes: set[str]
    control_result: dict[str, Any] | None
    _attr_min_color_temp_kelvin: Incomplete
    _attr_max_color_temp_kelvin: Incomplete
    def __init__(self, coordinator: ShellyBlockCoordinator, block: Block) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def mode(self) -> str: ...
    @property
    def brightness(self) -> int: ...
    @property
    def color_mode(self) -> ColorMode: ...
    @property
    def rgb_color(self) -> tuple[int, int, int]: ...
    @property
    def rgbw_color(self) -> tuple[int, int, int, int]: ...
    @property
    def color_temp_kelvin(self) -> int: ...
    @property
    def effect_list(self) -> list[str] | None: ...
    @property
    def effect(self) -> str | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @callback
    def _update_callback(self) -> None: ...

class RpcShellyLightBase(ShellyRpcEntity, LightEntity):
    _component: str
    _id: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, id_: int) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def brightness(self) -> int: ...
    @property
    def rgb_color(self) -> tuple[int, int, int]: ...
    @property
    def rgbw_color(self) -> tuple[int, int, int, int]: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class RpcShellySwitchAsLight(RpcShellyLightBase):
    _component: str
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete

class RpcShellyLight(RpcShellyLightBase):
    _component: str
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_supported_features: Incomplete

class RpcShellyCctLight(RpcShellyLightBase):
    _component: str
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_min_color_temp_kelvin: Incomplete
    _attr_max_color_temp_kelvin: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, id_: int) -> None: ...
    @property
    def color_temp_kelvin(self) -> int: ...

class RpcShellyRgbLight(RpcShellyLightBase):
    _component: str
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_supported_features: Incomplete

class RpcShellyRgbwLight(RpcShellyLightBase):
    _component: str
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_supported_features: Incomplete
