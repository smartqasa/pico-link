from .coordinator import EnphaseUpdateCoordinator as EnphaseUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pyenphase import EnvoyData as EnvoyData

class EnvoyBaseEntity(CoordinatorEntity[EnphaseUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    envoy_serial_num: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: EntityDescription) -> None: ...
    @property
    def data(self) -> EnvoyData: ...
