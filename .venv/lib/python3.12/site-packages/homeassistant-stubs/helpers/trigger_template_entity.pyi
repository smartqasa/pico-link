import voluptuous as vol
from .entity import Entity as Entity
from .template import TemplateStateFromEntityId as TemplateStateFromEntityId, render_complex as render_complex
from .typing import ConfigType as ConfigType
from _typeshed import Incomplete
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA, STATE_CLASSES_SCHEMA as STATE_CLASSES_SCHEMA, SensorEntity as SensorEntity
from homeassistant.const import ATTR_ENTITY_PICTURE as ATTR_ENTITY_PICTURE, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, ATTR_ICON as ATTR_ICON, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ICON as CONF_ICON, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.util.json import JSON_DECODE_EXCEPTIONS as JSON_DECODE_EXCEPTIONS, json_loads as json_loads
from typing import Any

CONF_AVAILABILITY: str
CONF_ATTRIBUTES: str
CONF_PICTURE: str
CONF_TO_ATTRIBUTE: Incomplete
TEMPLATE_ENTITY_BASE_SCHEMA: Incomplete

def make_template_entity_base_schema(default_name: str) -> vol.Schema: ...

TEMPLATE_SENSOR_BASE_SCHEMA: Incomplete

class TriggerBaseEntity(Entity):
    domain: str
    extra_template_keys: tuple[str, ...] | None
    extra_template_keys_complex: tuple[str, ...] | None
    _unique_id: str | None
    hass: Incomplete
    _config: Incomplete
    _static_rendered: Incomplete
    _to_render_simple: list[str]
    _to_render_complex: list[str]
    _rendered: Incomplete
    _parse_result: Incomplete
    _attr_device_class: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConfigType) -> None: ...
    @property
    def name(self) -> str | None: ...
    @property
    def unique_id(self) -> str | None: ...
    @property
    def icon(self) -> str | None: ...
    @property
    def entity_picture(self) -> str | None: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    def _set_unique_id(self, unique_id: str | None) -> None: ...
    def restore_attributes(self, last_state: State) -> None: ...
    def _render_templates(self, variables: dict[str, Any]) -> None: ...

class ManualTriggerEntity(TriggerBaseEntity):
    def __init__(self, hass: HomeAssistant, config: ConfigType) -> None: ...
    @callback
    def _process_manual_data(self, value: Any | None = None) -> None: ...

class ManualTriggerSensorEntity(ManualTriggerEntity, SensorEntity):
    _attr_native_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConfigType) -> None: ...
