from .const import DOMAIN as DOMAIN
from .models import ELKM1Data as ELKM1Data
from _typeshed import Incomplete
from collections.abc import Iterable
from elkm1_lib.elements import Element as Element
from elkm1_lib.elk import Elk as Elk
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from typing import Any

_LOGGER: Incomplete

def create_elk_entities(elk_data: ELKM1Data, elk_elements: Iterable[Element], element_type: str, class_: Any, entities: list[ElkEntity]) -> list[ElkEntity] | None: ...

class ElkEntity(Entity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _elk: Incomplete
    _element: Incomplete
    _mac: Incomplete
    _prefix: Incomplete
    _temperature_unit: str
    _unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, element: Element, elk: Elk, elk_data: ELKM1Data) -> None: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def available(self) -> bool: ...
    def initial_attrs(self) -> dict[str, Any]: ...
    def _element_changed(self, element: Element, changeset: dict[str, Any]) -> None: ...
    @callback
    def _element_callback(self, element: Element, changeset: dict[str, Any]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...

class ElkAttachedEntity(ElkEntity):
    @property
    def device_info(self) -> DeviceInfo: ...
