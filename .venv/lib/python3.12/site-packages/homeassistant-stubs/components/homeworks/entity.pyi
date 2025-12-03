from .util import calculate_unique_id as calculate_unique_id
from _typeshed import Incomplete
from homeassistant.helpers.entity import Entity as Entity
from pyhomeworks.pyhomeworks import Homeworks as Homeworks

class HomeworksEntity(Entity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _addr: Incomplete
    _idx: Incomplete
    _controller_id: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _controller: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, controller: Homeworks, controller_id: str, addr: str, idx: int, name: str | None) -> None: ...
