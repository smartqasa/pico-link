import voluptuous as vol
from .entity_store_schema import ENTITY_STORE_DATA_SCHEMA as ENTITY_STORE_DATA_SCHEMA
from _typeshed import Incomplete
from typing import Literal, TypedDict

class _ErrorDescription(TypedDict):
    path: list[str] | None
    error_message: str
    error_class: str

class EntityStoreValidationError(TypedDict):
    success: Literal[False]
    error_base: str
    errors: list[_ErrorDescription]

class EntityStoreValidationSuccess(TypedDict):
    success: Literal[True]
    entity_id: str | None

def parse_invalid(exc: vol.Invalid) -> _ErrorDescription: ...
def validate_entity_data(entity_data: dict) -> dict: ...

class EntityStoreValidationException(Exception):
    validation_error: Incomplete
    def __init__(self, validation_error: EntityStoreValidationError) -> None: ...
