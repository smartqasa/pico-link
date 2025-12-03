from . import ElkM1ConfigEntry as ElkM1ConfigEntry
from .entity import ElkAttachedEntity as ElkAttachedEntity, ElkEntity as ElkEntity, create_elk_entities as create_elk_entities
from .models import ELKM1Data as ELKM1Data
from _typeshed import Incomplete
from elkm1_lib.const import ThermostatMode
from elkm1_lib.elements import Element as Element
from elkm1_lib.elk import Elk as Elk
from elkm1_lib.outputs import Output as Output
from elkm1_lib.thermostats import Thermostat as Thermostat
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ElkM1ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElkOutput(ElkAttachedEntity, SwitchEntity):
    _element: Output
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class ElkThermostatEMHeat(ElkEntity, SwitchEntity):
    _element: Thermostat
    _unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, element: Element, elk: Elk, elk_data: ELKM1Data) -> None: ...
    @property
    def is_on(self) -> bool: ...
    def _elk_set(self, mode: ThermostatMode) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
