from collections.abc import Iterable
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ENTITY_MATCH_ALL as ENTITY_MATCH_ALL, ENTITY_MATCH_NONE as ENTITY_MATCH_NONE
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

ENTITY_PREFIX: str

def expand_entity_ids(hass: HomeAssistant, entity_ids: Iterable[Any]) -> list[str]: ...
def get_entity_ids(hass: HomeAssistant, entity_id: str, domain_filter: str | None = None) -> list[str]: ...
