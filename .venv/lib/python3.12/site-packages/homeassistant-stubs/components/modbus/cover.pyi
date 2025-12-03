from . import get_hub as get_hub
from .const import CALL_TYPE_COIL as CALL_TYPE_COIL, CALL_TYPE_WRITE_COIL as CALL_TYPE_WRITE_COIL, CALL_TYPE_WRITE_REGISTER as CALL_TYPE_WRITE_REGISTER, CONF_STATE_CLOSED as CONF_STATE_CLOSED, CONF_STATE_CLOSING as CONF_STATE_CLOSING, CONF_STATE_OPEN as CONF_STATE_OPEN, CONF_STATE_OPENING as CONF_STATE_OPENING, CONF_STATUS_REGISTER as CONF_STATUS_REGISTER, CONF_STATUS_REGISTER_TYPE as CONF_STATUS_REGISTER_TYPE
from .entity import BasePlatform as BasePlatform
from .modbus import ModbusHub as ModbusHub
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.cover import CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature, CoverState as CoverState
from homeassistant.const import CONF_COVERS as CONF_COVERS, CONF_NAME as CONF_NAME, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class ModbusCover(BasePlatform, CoverEntity, RestoreEntity):
    _attr_supported_features: Incomplete
    _state_closed: Incomplete
    _state_closing: Incomplete
    _state_open: Incomplete
    _state_opening: Incomplete
    _status_register: Incomplete
    _status_register_type: Incomplete
    _attr_is_closed: bool
    _write_type: Incomplete
    _write_address: Incomplete
    _address: Incomplete
    _input_type: Incomplete
    def __init__(self, hass: HomeAssistant, hub: ModbusHub, config: dict[str, Any]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_is_opening: Incomplete
    _attr_is_closing: Incomplete
    def _set_attr_state(self, value: str | bool | int) -> None: ...
    _attr_available: Incomplete
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_update(self, now: datetime | None = None) -> None: ...
