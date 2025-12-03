from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Iterable
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

class RunStates(StrEnum):
    NOT_RUNNING = 'Not Running'
    QUEUED = 'Queued'
    RUNNING = 'Running'

RUN_STATE_MAP: Incomplete

@dataclass
class EntityDomainReplacementStrategy:
    old_domain: str
    old_unique_id: str
    replacement_entity_id: str
    breaks_in_ha_version: str
    remove_old_entity: bool = ...

@callback
def async_finish_entity_domain_replacements(hass: HomeAssistant, entry: ConfigEntry, entity_replacement_strategies: Iterable[EntityDomainReplacementStrategy]) -> None: ...
def key_exists(data: dict[str, Any], search_key: str) -> bool: ...
