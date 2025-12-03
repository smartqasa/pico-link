from .accessories import HomeAccessory as HomeAccessory, TYPES as TYPES
from .const import CHAR_ACTIVE as CHAR_ACTIVE, CHAR_CURRENT_HUMIDIFIER_DEHUMIDIFIER as CHAR_CURRENT_HUMIDIFIER_DEHUMIDIFIER, CHAR_CURRENT_HUMIDITY as CHAR_CURRENT_HUMIDITY, CHAR_DEHUMIDIFIER_THRESHOLD_HUMIDITY as CHAR_DEHUMIDIFIER_THRESHOLD_HUMIDITY, CHAR_HUMIDIFIER_THRESHOLD_HUMIDITY as CHAR_HUMIDIFIER_THRESHOLD_HUMIDITY, CHAR_TARGET_HUMIDIFIER_DEHUMIDIFIER as CHAR_TARGET_HUMIDIFIER_DEHUMIDIFIER, CONF_LINKED_HUMIDITY_SENSOR as CONF_LINKED_HUMIDITY_SENSOR, PROP_MAX_VALUE as PROP_MAX_VALUE, PROP_MIN_STEP as PROP_MIN_STEP, PROP_MIN_VALUE as PROP_MIN_VALUE, SERV_HUMIDIFIER_DEHUMIDIFIER as SERV_HUMIDIFIER_DEHUMIDIFIER
from _typeshed import Incomplete
from homeassistant.components.humidifier import ATTR_CURRENT_HUMIDITY as ATTR_CURRENT_HUMIDITY, ATTR_HUMIDITY as ATTR_HUMIDITY, ATTR_MAX_HUMIDITY as ATTR_MAX_HUMIDITY, ATTR_MIN_HUMIDITY as ATTR_MIN_HUMIDITY, DEFAULT_MAX_HUMIDITY as DEFAULT_MAX_HUMIDITY, DEFAULT_MIN_HUMIDITY as DEFAULT_MIN_HUMIDITY, HumidifierDeviceClass as HumidifierDeviceClass, SERVICE_SET_HUMIDITY as SERVICE_SET_HUMIDITY
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_ENTITY_ID as ATTR_ENTITY_ID, PERCENTAGE as PERCENTAGE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HassJobType as HassJobType, State as State, callback as callback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from pyhap.util import callback as pyhap_callback
from typing import Any

_LOGGER: Incomplete
HC_HUMIDIFIER: int
HC_DEHUMIDIFIER: int
HC_HASS_TO_HOMEKIT_DEVICE_CLASS: Incomplete
HC_HASS_TO_HOMEKIT_DEVICE_CLASS_NAME: Incomplete
HC_DEVICE_CLASS_TO_TARGET_CHAR: Incomplete
HC_STATE_INACTIVE: int
HC_STATE_IDLE: int
HC_STATE_HUMIDIFYING: int
HC_STATE_DEHUMIDIFYING: int
BASE_VALID_VALUES: Incomplete
VALID_VALUES_BY_DEVICE_CLASS: Incomplete

class HumidifierDehumidifier(HomeAccessory):
    chars: list[str]
    _hk_device_class: Incomplete
    _target_humidity_char_name: Incomplete
    char_current_humidifier_dehumidifier: Incomplete
    char_target_humidifier_dehumidifier: Incomplete
    char_current_humidity: Incomplete
    char_target_humidity: Incomplete
    char_active: Incomplete
    linked_humidity_sensor: Incomplete
    def __init__(self, *args: Any) -> None: ...
    @callback
    @pyhap_callback
    def run(self) -> None: ...
    @callback
    def async_update_current_humidity_event(self, event: Event[EventStateChangedData]) -> None: ...
    @callback
    def _async_update_current_humidity(self, new_state: State | None) -> None: ...
    @callback
    def _async_update_current_humidity_value(self, current_humidity: float) -> None: ...
    def _set_chars(self, char_values: dict[str, Any]) -> None: ...
    def get_humidity_range(self, state: State) -> tuple[int, int]: ...
    @callback
    def async_update_state(self, new_state: State) -> None: ...
