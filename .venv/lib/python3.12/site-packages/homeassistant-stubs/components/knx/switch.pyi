from . import KNXModule as KNXModule
from .const import CONF_INVERT as CONF_INVERT, CONF_RESPOND_TO_READ as CONF_RESPOND_TO_READ, CONF_SYNC_STATE as CONF_SYNC_STATE, DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS, KNX_MODULE_KEY as KNX_MODULE_KEY
from .entity import KnxUiEntity as KnxUiEntity, KnxUiEntityPlatformController as KnxUiEntityPlatformController, KnxYamlEntity as KnxYamlEntity
from .schema import SwitchSchema as SwitchSchema
from .storage.const import CONF_ENTITY as CONF_ENTITY, CONF_GA_PASSIVE as CONF_GA_PASSIVE, CONF_GA_STATE as CONF_GA_STATE, CONF_GA_SWITCH as CONF_GA_SWITCH, CONF_GA_WRITE as CONF_GA_WRITE
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, Platform as Platform, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback, async_get_current_platform as async_get_current_platform
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any
from xknx.devices import Switch as XknxSwitch

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class _KnxSwitch(SwitchEntity, RestoreEntity):
    _device: XknxSwitch
    async def async_added_to_hass(self) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class KnxYamlSwitch(_KnxSwitch, KnxYamlEntity):
    _device: XknxSwitch
    _attr_entity_category: Incomplete
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...

class KnxUiSwitch(_KnxSwitch, KnxUiEntity):
    _device: XknxSwitch
    def __init__(self, knx_module: KNXModule, unique_id: str, config: dict[str, Any]) -> None: ...
