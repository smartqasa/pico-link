from . import ElkM1ConfigEntry as ElkM1ConfigEntry
from .const import ATTR_VALUE as ATTR_VALUE, ELK_USER_CODE_SERVICE_SCHEMA as ELK_USER_CODE_SERVICE_SCHEMA
from .entity import ElkAttachedEntity as ElkAttachedEntity, ElkEntity as ElkEntity, create_elk_entities as create_elk_entities
from _typeshed import Incomplete
from elkm1_lib.counters import Counter as Counter
from elkm1_lib.elements import Element as Element
from elkm1_lib.keypads import Keypad as Keypad
from elkm1_lib.panel import Panel as Panel
from elkm1_lib.settings import Setting as Setting
from elkm1_lib.zones import Zone as Zone
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.const import EntityCategory as EntityCategory, UnitOfElectricPotential as UnitOfElectricPotential
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import VolDictType as VolDictType
from typing import Any

SERVICE_SENSOR_COUNTER_REFRESH: str
SERVICE_SENSOR_COUNTER_SET: str
SERVICE_SENSOR_ZONE_BYPASS: str
SERVICE_SENSOR_ZONE_TRIGGER: str
UNDEFINED_TEMPERATURE: int
ELK_SET_COUNTER_SERVICE_SCHEMA: VolDictType

async def async_setup_entry(hass: HomeAssistant, config_entry: ElkM1ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def temperature_to_state(temperature: int, undefined_temperature: int) -> str | None: ...

class ElkSensor(ElkAttachedEntity, SensorEntity):
    _attr_native_value: str | None
    async def async_counter_refresh(self) -> None: ...
    async def async_counter_set(self, value: int | None = None) -> None: ...
    async def async_zone_bypass(self, code: int | None = None) -> None: ...
    async def async_zone_trigger(self) -> None: ...

class ElkCounter(ElkSensor):
    _attr_icon: str
    _element: Counter
    _attr_native_value: Incomplete
    def _element_changed(self, _: Element, changeset: Any) -> None: ...

class ElkKeypad(ElkSensor):
    _attr_icon: str
    _element: Keypad
    @property
    def temperature_unit(self) -> str: ...
    @property
    def native_unit_of_measurement(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    _attr_native_value: Incomplete
    def _element_changed(self, _: Element, changeset: Any) -> None: ...

class ElkPanel(ElkSensor):
    _attr_translation_key: str
    _attr_entity_category: Incomplete
    _element: Panel
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    _attr_native_value: Incomplete
    def _element_changed(self, _: Element, changeset: Any) -> None: ...

class ElkSetting(ElkSensor):
    _attr_translation_key: str
    _element: Setting
    _attr_native_value: Incomplete
    def _element_changed(self, _: Element, changeset: Any) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...

class ElkZone(ElkSensor):
    _element: Zone
    @property
    def icon(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def temperature_unit(self) -> str | None: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    _attr_native_value: Incomplete
    def _element_changed(self, _: Element, changeset: Any) -> None: ...
