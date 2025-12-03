import voluptuous as vol
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from enum import Enum
from typing import Any
from xknx.dpt import DPTBase

def dpt_subclass_validator(dpt_base_class: type[DPTBase]) -> Callable[[Any], str | int]: ...

dpt_base_type_validator: Incomplete
numeric_type_validator: Incomplete
string_type_validator: Incomplete
sensor_type_validator: Incomplete

def ga_validator(value: Any) -> str | int: ...
def maybe_ga_validator(value: Any) -> str | int | None: ...

ga_list_validator: Incomplete
ga_list_validator_optional: Incomplete
ia_validator: Incomplete

def ip_v4_validator(value: Any, multicast: bool | None = None) -> str: ...

sync_state_validator: Incomplete

def backwards_compatible_xknx_climate_enum_member(enumClass: type[Enum]) -> vol.All: ...
