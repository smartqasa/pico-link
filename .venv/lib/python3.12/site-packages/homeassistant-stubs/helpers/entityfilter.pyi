import re
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.const import CONF_DOMAINS as CONF_DOMAINS, CONF_ENTITIES as CONF_ENTITIES, CONF_EXCLUDE as CONF_EXCLUDE, CONF_INCLUDE as CONF_INCLUDE, MAX_EXPECTED_ENTITY_IDS as MAX_EXPECTED_ENTITY_IDS
from homeassistant.core import split_entity_id as split_entity_id

CONF_INCLUDE_DOMAINS: str
CONF_INCLUDE_ENTITY_GLOBS: str
CONF_INCLUDE_ENTITIES: str
CONF_EXCLUDE_DOMAINS: str
CONF_EXCLUDE_ENTITY_GLOBS: str
CONF_EXCLUDE_ENTITIES: str
CONF_ENTITY_GLOBS: str

class EntityFilter:
    empty_filter: bool
    config: Incomplete
    _include_e: Incomplete
    _exclude_e: Incomplete
    _include_d: Incomplete
    _exclude_d: Incomplete
    _include_eg: Incomplete
    _exclude_eg: Incomplete
    _filter: Incomplete
    def __init__(self, config: dict[str, list[str]]) -> None: ...
    def explicitly_included(self, entity_id: str) -> bool: ...
    def explicitly_excluded(self, entity_id: str) -> bool: ...
    def get_filter(self) -> Callable[[str], bool]: ...
    def __call__(self, entity_id: str) -> bool: ...

def convert_filter(config: dict[str, list[str]]) -> EntityFilter: ...

BASE_FILTER_SCHEMA: Incomplete
FILTER_SCHEMA: Incomplete

def convert_include_exclude_filter(config: dict[str, dict[str, list[str]]]) -> EntityFilter: ...

INCLUDE_EXCLUDE_FILTER_SCHEMA_INNER: Incomplete
INCLUDE_EXCLUDE_BASE_FILTER_SCHEMA: Incomplete
INCLUDE_EXCLUDE_FILTER_SCHEMA: Incomplete

def _convert_globs_to_pattern(globs: list[str] | None) -> re.Pattern[str] | None: ...
def generate_filter(include_domains: list[str], include_entities: list[str], exclude_domains: list[str], exclude_entities: list[str], include_entity_globs: list[str] | None = None, exclude_entity_globs: list[str] | None = None) -> Callable[[str], bool]: ...
def _generate_filter_from_sets_and_pattern_lists(include_d: set[str], include_e: set[str], exclude_d: set[str], exclude_e: set[str], include_eg: re.Pattern[str] | None, exclude_eg: re.Pattern[str] | None) -> Callable[[str], bool]: ...
