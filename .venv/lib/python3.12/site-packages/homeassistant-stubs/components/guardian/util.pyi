from .const import LOGGER as LOGGER
from .entity import GuardianEntity as GuardianEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine, Iterable
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate

DEFAULT_UPDATE_INTERVAL: Incomplete
SIGNAL_REBOOT_REQUESTED: str

@dataclass
class EntityDomainReplacementStrategy:
    old_domain: str
    old_unique_id: str

@callback
def async_finish_entity_domain_replacements(hass: HomeAssistant, entry: ConfigEntry, entity_replacement_strategies: Iterable[EntityDomainReplacementStrategy]) -> None: ...
@callback
def convert_exceptions_to_homeassistant_error[_GuardianEntityT: GuardianEntity, **_P](func: Callable[Concatenate[_GuardianEntityT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_GuardianEntityT, _P], Coroutine[Any, Any, None]]: ...
