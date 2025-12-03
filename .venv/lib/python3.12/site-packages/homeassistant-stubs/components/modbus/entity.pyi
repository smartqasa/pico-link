import abc
from .const import CALL_TYPE_COIL as CALL_TYPE_COIL, CALL_TYPE_DISCRETE as CALL_TYPE_DISCRETE, CALL_TYPE_REGISTER_HOLDING as CALL_TYPE_REGISTER_HOLDING, CALL_TYPE_REGISTER_INPUT as CALL_TYPE_REGISTER_INPUT, CALL_TYPE_WRITE_COIL as CALL_TYPE_WRITE_COIL, CALL_TYPE_WRITE_COILS as CALL_TYPE_WRITE_COILS, CALL_TYPE_WRITE_REGISTER as CALL_TYPE_WRITE_REGISTER, CALL_TYPE_WRITE_REGISTERS as CALL_TYPE_WRITE_REGISTERS, CALL_TYPE_X_COILS as CALL_TYPE_X_COILS, CALL_TYPE_X_REGISTER_HOLDINGS as CALL_TYPE_X_REGISTER_HOLDINGS, CONF_DATA_TYPE as CONF_DATA_TYPE, CONF_DEVICE_ADDRESS as CONF_DEVICE_ADDRESS, CONF_INPUT_TYPE as CONF_INPUT_TYPE, CONF_MAX_VALUE as CONF_MAX_VALUE, CONF_MIN_VALUE as CONF_MIN_VALUE, CONF_NAN_VALUE as CONF_NAN_VALUE, CONF_PRECISION as CONF_PRECISION, CONF_SCALE as CONF_SCALE, CONF_SLAVE_COUNT as CONF_SLAVE_COUNT, CONF_STATE_OFF as CONF_STATE_OFF, CONF_STATE_ON as CONF_STATE_ON, CONF_SWAP as CONF_SWAP, CONF_SWAP_BYTE as CONF_SWAP_BYTE, CONF_SWAP_WORD as CONF_SWAP_WORD, CONF_SWAP_WORD_BYTE as CONF_SWAP_WORD_BYTE, CONF_VERIFY as CONF_VERIFY, CONF_VIRTUAL_COUNT as CONF_VIRTUAL_COUNT, CONF_WRITE_TYPE as CONF_WRITE_TYPE, CONF_ZERO_SUPPRESS as CONF_ZERO_SUPPRESS, DataType as DataType, SIGNAL_START_ENTITY as SIGNAL_START_ENTITY, SIGNAL_STOP_ENTITY as SIGNAL_STOP_ENTITY
from .modbus import ModbusHub as ModbusHub
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_COMMAND_OFF as CONF_COMMAND_OFF, CONF_COMMAND_ON as CONF_COMMAND_ON, CONF_COUNT as CONF_COUNT, CONF_DELAY as CONF_DELAY, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_NAME as CONF_NAME, CONF_OFFSET as CONF_OFFSET, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_SLAVE as CONF_SLAVE, CONF_STRUCTURE as CONF_STRUCTURE, CONF_UNIQUE_ID as CONF_UNIQUE_ID, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import Entity as Entity, ToggleEntity as ToggleEntity
from homeassistant.helpers.event import async_call_later as async_call_later, async_track_time_interval as async_track_time_interval
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from typing import Any

_LOGGER: Incomplete

class BasePlatform(Entity, metaclass=abc.ABCMeta):
    _hub: Incomplete
    _slave: Incomplete
    _address: Incomplete
    _input_type: Incomplete
    _value: str | None
    _scan_interval: Incomplete
    _call_active: bool
    _cancel_timer: Callable[[], None] | None
    _cancel_call: Callable[[], None] | None
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_should_poll: bool
    _attr_device_class: Incomplete
    _attr_available: bool
    _attr_unit_of_measurement: Incomplete
    _min_value: Incomplete
    _max_value: Incomplete
    _nan_value: Incomplete
    _zero_suppress: Incomplete
    def __init__(self, hass: HomeAssistant, hub: ModbusHub, entry: dict[str, Any]) -> None: ...
    @abstractmethod
    async def async_update(self, now: datetime | None = None) -> None: ...
    @callback
    def async_run(self) -> None: ...
    @callback
    def async_hold(self, update: bool = True) -> None: ...
    async def async_base_added_to_hass(self) -> None: ...

class BaseStructPlatform(BasePlatform, RestoreEntity, metaclass=abc.ABCMeta):
    _swap: Incomplete
    _data_type: Incomplete
    _structure: str
    _scale: Incomplete
    _offset: Incomplete
    _slave_count: Incomplete
    _slave_size: Incomplete
    _value_is_int: bool
    _precision: Incomplete
    def __init__(self, hass: HomeAssistant, hub: ModbusHub, config: dict) -> None: ...
    def _swap_registers(self, registers: list[int], slave_count: int) -> list[int]: ...
    def __process_raw_value(self, entry: float | str | bytes) -> str | None: ...
    def unpack_structure_result(self, registers: list[int]) -> str | None: ...

class BaseSwitch(BasePlatform, ToggleEntity, RestoreEntity):
    _attr_is_on: bool
    _write_type: Incomplete
    command_on: Incomplete
    _command_off: Incomplete
    _verify_active: bool
    _verify_delay: Incomplete
    _verify_address: Incomplete
    _verify_type: Incomplete
    _state_on: Incomplete
    _state_off: Incomplete
    def __init__(self, hass: HomeAssistant, hub: ModbusHub, config: dict) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_available: bool
    async def async_turn(self, command: int) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _call_active: bool
    async def async_update(self, now: datetime | None = None) -> None: ...
