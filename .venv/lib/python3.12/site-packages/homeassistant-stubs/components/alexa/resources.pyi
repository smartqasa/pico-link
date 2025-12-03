from _typeshed import Incomplete
from typing import Any

class AlexaGlobalCatalog:
    DEVICE_NAME_AIR_PURIFIER: str
    DEVICE_NAME_FAN: str
    DEVICE_NAME_ROUTER: str
    DEVICE_NAME_SHADE: str
    DEVICE_NAME_SHOWER: str
    DEVICE_NAME_SPACE_HEATER: str
    DEVICE_NAME_WASHER: str
    SETTING_2G_GUEST_WIFI: str
    SETTING_5G_GUEST_WIFI: str
    SETTING_AUTO: str
    SETTING_DIRECTION: str
    SETTING_DRY_CYCLE: str
    SETTING_FAN_SPEED: str
    SETTING_GUEST_WIFI: str
    SETTING_HEAT: str
    SETTING_MODE: str
    SETTING_NIGHT: str
    SETTING_OPENING: str
    SETTING_OSCILLATE: str
    SETTING_PRESET: str
    SETTING_QUIET: str
    SETTING_TEMPERATURE: str
    SETTING_WASH_CYCLE: str
    SETTING_WATER_TEMPERATURE: str
    SHOWER_HAND_HELD: str
    SHOWER_RAIN_HEAD: str
    UNIT_ANGLE_DEGREES: str
    UNIT_ANGLE_RADIANS: str
    UNIT_DISTANCE_FEET: str
    UNIT_DISTANCE_INCHES: str
    UNIT_DISTANCE_KILOMETERS: str
    UNIT_DISTANCE_METERS: str
    UNIT_DISTANCE_MILES: str
    UNIT_DISTANCE_YARDS: str
    UNIT_MASS_GRAMS: str
    UNIT_MASS_KILOGRAMS: str
    UNIT_PERCENT: str
    UNIT_TEMPERATURE_CELSIUS: str
    UNIT_TEMPERATURE_DEGREES: str
    UNIT_TEMPERATURE_FAHRENHEIT: str
    UNIT_TEMPERATURE_KELVIN: str
    UNIT_VOLUME_CUBIC_FEET: str
    UNIT_VOLUME_CUBIC_METERS: str
    UNIT_VOLUME_GALLONS: str
    UNIT_VOLUME_LITERS: str
    UNIT_VOLUME_PINTS: str
    UNIT_VOLUME_QUARTS: str
    UNIT_WEIGHT_OUNCES: str
    UNIT_WEIGHT_POUNDS: str
    VALUE_CLOSE: str
    VALUE_DELICATE: str
    VALUE_HIGH: str
    VALUE_LOW: str
    VALUE_MAXIMUM: str
    VALUE_MEDIUM: str
    VALUE_MINIMUM: str
    VALUE_OPEN: str
    VALUE_QUICK_WASH: str

class AlexaCapabilityResource:
    _resource_labels: Incomplete
    def __init__(self, labels: list[str]) -> None: ...
    def serialize_capability_resources(self) -> dict[str, list[dict[str, Any]]]: ...
    def serialize_configuration(self) -> dict[str, Any]: ...
    def serialize_labels(self, resources: list[str]) -> dict[str, list[dict[str, Any]]]: ...

class AlexaModeResource(AlexaCapabilityResource):
    _supported_modes: list[dict[str, Any]]
    _mode_ordered: bool
    def __init__(self, labels: list[str], ordered: bool = False) -> None: ...
    def add_mode(self, value: str, labels: list[str]) -> None: ...
    def serialize_configuration(self) -> dict[str, Any]: ...

class AlexaPresetResource(AlexaCapabilityResource):
    _presets: list[dict[str, Any]]
    _minimum_value: Incomplete
    _maximum_value: Incomplete
    _precision: Incomplete
    _unit_of_measure: Incomplete
    def __init__(self, labels: list[str], min_value: float, max_value: float, precision: float, unit: str | None = None) -> None: ...
    def add_preset(self, value: float, labels: list[str]) -> None: ...
    def serialize_configuration(self) -> dict[str, Any]: ...

class AlexaSemantics:
    MAPPINGS_ACTION: str
    MAPPINGS_STATE: str
    ACTIONS_TO_DIRECTIVE: str
    STATES_TO_VALUE: str
    STATES_TO_RANGE: str
    ACTION_CLOSE: str
    ACTION_LOWER: str
    ACTION_OPEN: str
    ACTION_RAISE: str
    STATES_OPEN: str
    STATES_CLOSED: str
    DIRECTIVE_RANGE_SET_VALUE: str
    DIRECTIVE_RANGE_ADJUST_VALUE: str
    DIRECTIVE_TOGGLE_TURN_ON: str
    DIRECTIVE_TOGGLE_TURN_OFF: str
    DIRECTIVE_MODE_SET_MODE: str
    DIRECTIVE_MODE_ADJUST_MODE: str
    _action_mappings: list[dict[str, Any]]
    _state_mappings: list[dict[str, Any]]
    def __init__(self) -> None: ...
    def _add_action_mapping(self, semantics: dict[str, Any]) -> None: ...
    def _add_state_mapping(self, semantics: dict[str, Any]) -> None: ...
    def add_states_to_value(self, states: list[str], value: Any) -> None: ...
    def add_states_to_range(self, states: list[str], min_value: float, max_value: float) -> None: ...
    def add_action_to_directive(self, actions: list[str], directive: str, payload: dict[str, Any]) -> None: ...
    def serialize_semantics(self) -> dict[str, Any]: ...
