from .const import DOMAIN as DOMAIN
from Tami4EdgeAPI import Tami4EdgeAPI as Tami4EdgeAPI
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription

class Tami4EdgeBaseEntity(Entity):
    _attr_has_entity_name: bool
    _state: Incomplete
    _api: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, api: Tami4EdgeAPI, entity_description: EntityDescription) -> None: ...
