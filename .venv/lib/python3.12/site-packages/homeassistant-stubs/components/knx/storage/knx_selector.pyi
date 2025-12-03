import voluptuous as vol
from ..validation import ga_validator as ga_validator, maybe_ga_validator as maybe_ga_validator
from .const import CONF_DPT as CONF_DPT, CONF_GA_PASSIVE as CONF_GA_PASSIVE, CONF_GA_STATE as CONF_GA_STATE, CONF_GA_WRITE as CONF_GA_WRITE
from _typeshed import Incomplete
from enum import Enum
from typing import Any

class GASelector:
    schema: vol.Schema
    write: Incomplete
    state: Incomplete
    passive: Incomplete
    write_required: Incomplete
    state_required: Incomplete
    dpt: Incomplete
    def __init__(self, write: bool = True, state: bool = True, passive: bool = True, write_required: bool = False, state_required: bool = False, dpt: type[Enum] | None = None) -> None: ...
    def __call__(self, data: Any) -> Any: ...
    def build_schema(self) -> vol.Schema: ...
    def _add_group_addresses(self, schema: dict[vol.Marker, Any]) -> None: ...
    def _add_passive(self, schema: dict[vol.Marker, Any]) -> None: ...
    def _add_dpt(self, schema: dict[vol.Marker, Any]) -> None: ...
