from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping, Sequence
from enum import StrEnum
from functools import cache
from homeassistant.const import CONF_MODE as CONF_MODE, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT
from homeassistant.core import split_entity_id as split_entity_id, valid_entity_id as valid_entity_id
from homeassistant.generated.countries import COUNTRIES as COUNTRIES
from homeassistant.util import decorator as decorator
from homeassistant.util.yaml import dumper as dumper
from typing import Any, Literal, Required, TypedDict

SELECTORS: decorator.Registry[str, type[Selector]]

def _get_selector_class(config: Any) -> type[Selector]: ...
def selector(config: Any) -> Selector: ...
def validate_selector(config: Any) -> dict: ...

class Selector[_T: Mapping[str, Any]]:
    CONFIG_SCHEMA: Callable
    config: _T
    selector_type: str
    def __init__(self, config: Mapping[str, Any] | None = None) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def serialize(self) -> dict[str, dict[str, _T]]: ...

@cache
def _entity_feature_flag(domain: str, enum_name: str, feature_name: str) -> int: ...
def _validate_supported_feature(supported_feature: str) -> int: ...
def _validate_supported_features(supported_features: int | list[str]) -> int: ...

ENTITY_FILTER_SELECTOR_CONFIG_SCHEMA: Incomplete

class EntityFilterSelectorConfig(TypedDict, total=False):
    integration: str
    domain: str | list[str]
    device_class: str | list[str]
    supported_features: list[str]

DEVICE_FILTER_SELECTOR_CONFIG_SCHEMA: Incomplete

class DeviceFilterSelectorConfig(TypedDict, total=False):
    integration: str
    manufacturer: str
    model: str

class ActionSelectorConfig(TypedDict): ...

class ActionSelector(Selector[ActionSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: ActionSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> Any: ...

class AddonSelectorConfig(TypedDict, total=False):
    name: str
    slug: str

class AddonSelector(Selector[AddonSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: AddonSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> str: ...

class AreaSelectorConfig(TypedDict, total=False):
    entity: EntityFilterSelectorConfig | list[EntityFilterSelectorConfig]
    device: DeviceFilterSelectorConfig | list[DeviceFilterSelectorConfig]
    multiple: bool

class AreaSelector(Selector[AreaSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: AreaSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> str | list[str]: ...

class AssistPipelineSelectorConfig(TypedDict, total=False): ...

class AssistPipelineSelector(Selector[AssistPipelineSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: AssistPipelineSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> str: ...

class AttributeSelectorConfig(TypedDict, total=False):
    entity_id: Required[str]
    hide_attributes: list[str]

class AttributeSelector(Selector[AttributeSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: AttributeSelectorConfig) -> None: ...
    def __call__(self, data: Any) -> str: ...

class BackupLocationSelectorConfig(TypedDict, total=False): ...

class BackupLocationSelector(Selector[BackupLocationSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: BackupLocationSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> str: ...

class BooleanSelectorConfig(TypedDict): ...

class BooleanSelector(Selector[BooleanSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: BooleanSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> bool: ...

class ColorRGBSelectorConfig(TypedDict): ...

class ColorRGBSelector(Selector[ColorRGBSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: ColorRGBSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> list[int]: ...

class ColorTempSelectorConfig(TypedDict, total=False):
    unit: ColorTempSelectorUnit
    min: int
    max: int
    max_mireds: int
    min_mireds: int

class ColorTempSelectorUnit(StrEnum):
    KELVIN = 'kelvin'
    MIRED = 'mired'

class ColorTempSelector(Selector[ColorTempSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: ColorTempSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> int: ...

class ConditionSelectorConfig(TypedDict): ...

class ConditionSelector(Selector[ConditionSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: ConditionSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> Any: ...

class ConfigEntrySelectorConfig(TypedDict, total=False):
    integration: str

class ConfigEntrySelector(Selector[ConfigEntrySelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: ConfigEntrySelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> str: ...

class ConstantSelectorConfig(TypedDict, total=False):
    label: str
    translation_key: str
    value: str | int | bool

class ConstantSelector(Selector[ConstantSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: ConstantSelectorConfig) -> None: ...
    def __call__(self, data: Any) -> Any: ...

class QrErrorCorrectionLevel(StrEnum):
    LOW = 'low'
    MEDIUM = 'medium'
    QUARTILE = 'quartile'
    HIGH = 'high'

class QrCodeSelectorConfig(TypedDict, total=False):
    data: str
    scale: int
    error_correction_level: QrErrorCorrectionLevel

class QrCodeSelector(Selector[QrCodeSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: QrCodeSelectorConfig) -> None: ...
    def __call__(self, data: Any) -> Any: ...

class ConversationAgentSelectorConfig(TypedDict, total=False):
    language: str

class ConversationAgentSelector(Selector[ConversationAgentSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: ConversationAgentSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> str: ...

class CountrySelectorConfig(TypedDict, total=False):
    countries: list[str]
    no_sort: bool

class CountrySelector(Selector[CountrySelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: CountrySelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> Any: ...

class DateSelectorConfig(TypedDict): ...

class DateSelector(Selector[DateSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: DateSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> Any: ...

class DateTimeSelectorConfig(TypedDict): ...

class DateTimeSelector(Selector[DateTimeSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: DateTimeSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> Any: ...

class DeviceSelectorConfig(DeviceFilterSelectorConfig, total=False):
    entity: EntityFilterSelectorConfig | list[EntityFilterSelectorConfig]
    multiple: bool
    filter: DeviceFilterSelectorConfig | list[DeviceFilterSelectorConfig]

class DeviceSelector(Selector[DeviceSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: DeviceSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> str | list[str]: ...

class DurationSelectorConfig(TypedDict, total=False):
    enable_day: bool
    enable_millisecond: bool
    allow_negative: bool

class DurationSelector(Selector[DurationSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: DurationSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> dict[str, float]: ...

class EntitySelectorConfig(EntityFilterSelectorConfig, total=False):
    exclude_entities: list[str]
    include_entities: list[str]
    multiple: bool
    filter: EntityFilterSelectorConfig | list[EntityFilterSelectorConfig]

class EntitySelector(Selector[EntitySelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: EntitySelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> str | list[str]: ...

class FloorSelectorConfig(TypedDict, total=False):
    entity: EntityFilterSelectorConfig | list[EntityFilterSelectorConfig]
    device: DeviceFilterSelectorConfig | list[DeviceFilterSelectorConfig]
    multiple: bool

class FloorSelector(Selector[FloorSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: FloorSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> str | list[str]: ...

class IconSelectorConfig(TypedDict, total=False):
    placeholder: str

class IconSelector(Selector[IconSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: IconSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> str: ...

class LabelSelectorConfig(TypedDict, total=False):
    multiple: bool

class LabelSelector(Selector[LabelSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: LabelSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> str | list[str]: ...

class LanguageSelectorConfig(TypedDict, total=False):
    languages: list[str]
    native_name: bool
    no_sort: bool

class LanguageSelector(Selector[LanguageSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: LanguageSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> str: ...

class LocationSelectorConfig(TypedDict, total=False):
    radius: bool
    icon: str

class LocationSelector(Selector[LocationSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    DATA_SCHEMA: Incomplete
    def __init__(self, config: LocationSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> dict[str, float]: ...

class MediaSelectorConfig(TypedDict): ...

class MediaSelector(Selector[MediaSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    DATA_SCHEMA: Incomplete
    def __init__(self, config: MediaSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> dict[str, float]: ...

class NumberSelectorConfig(TypedDict, total=False):
    min: float
    max: float
    step: float | Literal['any']
    unit_of_measurement: str
    mode: NumberSelectorMode

class NumberSelectorMode(StrEnum):
    BOX = 'box'
    SLIDER = 'slider'

def validate_slider(data: Any) -> Any: ...

class NumberSelector(Selector[NumberSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: NumberSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> float: ...

class ObjectSelectorConfig(TypedDict): ...

class ObjectSelector(Selector[ObjectSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: ObjectSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> Any: ...

select_option: Incomplete

class SelectOptionDict(TypedDict):
    value: str
    label: str

class SelectSelectorMode(StrEnum):
    LIST = 'list'
    DROPDOWN = 'dropdown'

class SelectSelectorConfig(TypedDict, total=False):
    options: Required[Sequence[SelectOptionDict] | Sequence[str]]
    multiple: bool
    custom_value: bool
    mode: SelectSelectorMode
    translation_key: str
    sort: bool

class SelectSelector(Selector[SelectSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: SelectSelectorConfig) -> None: ...
    def __call__(self, data: Any) -> Any: ...

class TargetSelectorConfig(TypedDict, total=False):
    entity: EntityFilterSelectorConfig | list[EntityFilterSelectorConfig]
    device: DeviceFilterSelectorConfig | list[DeviceFilterSelectorConfig]

class StateSelectorConfig(TypedDict, total=False):
    entity_id: Required[str]

class StateSelector(Selector[StateSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: StateSelectorConfig) -> None: ...
    def __call__(self, data: Any) -> str: ...

class TargetSelector(Selector[TargetSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    TARGET_SELECTION_SCHEMA: Incomplete
    def __init__(self, config: TargetSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> dict[str, list[str]]: ...

class TemplateSelectorConfig(TypedDict): ...

class TemplateSelector(Selector[TemplateSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: TemplateSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> str: ...

class TextSelectorConfig(TypedDict, total=False):
    multiline: bool
    prefix: str
    suffix: str
    type: TextSelectorType
    autocomplete: str
    multiple: bool

class TextSelectorType(StrEnum):
    COLOR = 'color'
    DATE = 'date'
    DATETIME_LOCAL = 'datetime-local'
    EMAIL = 'email'
    MONTH = 'month'
    NUMBER = 'number'
    PASSWORD = 'password'
    SEARCH = 'search'
    TEL = 'tel'
    TEXT = 'text'
    TIME = 'time'
    URL = 'url'
    WEEK = 'week'

class TextSelector(Selector[TextSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: TextSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> str | list[str]: ...

class ThemeSelectorConfig(TypedDict): ...

class ThemeSelector(Selector[ThemeSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: ThemeSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> str: ...

class TimeSelectorConfig(TypedDict): ...

class TimeSelector(Selector[TimeSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: TimeSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> str: ...

class TriggerSelectorConfig(TypedDict): ...

class TriggerSelector(Selector[TriggerSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: TriggerSelectorConfig | None = None) -> None: ...
    def __call__(self, data: Any) -> Any: ...

class FileSelectorConfig(TypedDict):
    accept: str

class FileSelector(Selector[FileSelectorConfig]):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: FileSelectorConfig) -> None: ...
    def __call__(self, data: Any) -> str: ...
