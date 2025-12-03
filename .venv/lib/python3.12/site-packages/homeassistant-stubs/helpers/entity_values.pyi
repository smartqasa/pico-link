from _typeshed import Incomplete
from homeassistant.const import MAX_EXPECTED_ENTITY_IDS as MAX_EXPECTED_ENTITY_IDS
from homeassistant.core import split_entity_id as split_entity_id

class EntityValues:
    _exact: Incomplete
    _domain: Incomplete
    _glob: Incomplete
    def __init__(self, exact: dict[str, dict[str, str]] | None = None, domain: dict[str, dict[str, str]] | None = None, glob: dict[str, dict[str, str]] | None = None) -> None: ...
    def get(self, entity_id: str) -> dict[str, str]: ...
