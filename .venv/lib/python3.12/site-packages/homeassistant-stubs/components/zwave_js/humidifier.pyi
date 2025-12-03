from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.humidifier import DEFAULT_MAX_HUMIDITY as DEFAULT_MAX_HUMIDITY, DEFAULT_MIN_HUMIDITY as DEFAULT_MIN_HUMIDITY, HumidifierDeviceClass as HumidifierDeviceClass, HumidifierEntity as HumidifierEntity, HumidifierEntityDescription as HumidifierEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from zwave_js_server.const.command_class.humidity_control import HumidityControlMode, HumidityControlSetpointType
from zwave_js_server.model.driver import Driver as Driver
from zwave_js_server.model.value import Value as ZwaveValue

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ZwaveHumidifierEntityDescription(HumidifierEntityDescription):
    on_mode: HumidityControlMode
    inverse_mode: HumidityControlMode
    setpoint_type: HumidityControlSetpointType

HUMIDIFIER_ENTITY_DESCRIPTION: Incomplete
DEHUMIDIFIER_ENTITY_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ZWaveHumidifier(ZWaveBaseEntity, HumidifierEntity):
    entity_description: ZwaveHumidifierEntityDescription
    _current_mode: ZwaveValue
    _setpoint: ZwaveValue | None
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, config_entry: ConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo, description: ZwaveHumidifierEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    def _supports_inverse_mode(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def target_humidity(self) -> int | None: ...
    async def async_set_humidity(self, humidity: int) -> None: ...
    @property
    def min_humidity(self) -> int: ...
    @property
    def max_humidity(self) -> int: ...
