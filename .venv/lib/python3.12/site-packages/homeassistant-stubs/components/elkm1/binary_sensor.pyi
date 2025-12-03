from . import ElkM1ConfigEntry as ElkM1ConfigEntry
from .entity import ElkAttachedEntity as ElkAttachedEntity, ElkEntity as ElkEntity
from _typeshed import Incomplete
from elkm1_lib.elements import Element as Element
from elkm1_lib.zones import Zone as Zone
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ElkM1ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElkBinarySensor(ElkAttachedEntity, BinarySensorEntity):
    _element: Zone
    _attr_entity_registry_enabled_default: bool
    _attr_is_on: Incomplete
    def _element_changed(self, _: Element, changeset: Any) -> None: ...
