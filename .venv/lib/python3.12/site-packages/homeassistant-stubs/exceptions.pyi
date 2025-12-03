from .core import Context as Context
from .util.event_type import EventType as EventType
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Generator, Sequence
from dataclasses import dataclass
from typing import Any

_function_cache: dict[str, Callable[[str, str, dict[str, str] | None], str]]

def import_async_get_exception_message() -> Callable[[str, str, dict[str, str] | None], str]: ...

class HomeAssistantError(Exception):
    _message: str | None
    generate_message: bool
    translation_domain: Incomplete
    translation_key: Incomplete
    translation_placeholders: Incomplete
    def __init__(self, *args: object, translation_domain: str | None = None, translation_key: str | None = None, translation_placeholders: dict[str, str] | None = None) -> None: ...
    def __str__(self) -> str: ...

class ConfigValidationError(HomeAssistantError, ExceptionGroup[Exception]):
    generate_message: bool
    def __init__(self, message_translation_key: str, exceptions: list[Exception], translation_domain: str | None = None, translation_placeholders: dict[str, str] | None = None) -> None: ...

class ServiceValidationError(HomeAssistantError): ...
class InvalidEntityFormatError(HomeAssistantError): ...
class NoEntitySpecifiedError(HomeAssistantError): ...

class TemplateError(HomeAssistantError):
    def __init__(self, exception: Exception | str) -> None: ...

@dataclass(slots=True)
class ConditionError(HomeAssistantError):
    type: str
    @staticmethod
    def _indent(indent: int, message: str) -> str: ...
    def output(self, indent: int) -> Generator[str]: ...
    def __str__(self) -> str: ...

@dataclass(slots=True)
class ConditionErrorMessage(ConditionError):
    message: str
    def output(self, indent: int) -> Generator[str]: ...

@dataclass(slots=True)
class ConditionErrorIndex(ConditionError):
    index: int
    total: int
    error: ConditionError
    def output(self, indent: int) -> Generator[str]: ...

@dataclass(slots=True)
class ConditionErrorContainer(ConditionError):
    errors: Sequence[ConditionError]
    def output(self, indent: int) -> Generator[str]: ...

class IntegrationError(HomeAssistantError):
    def __str__(self) -> str: ...

class PlatformNotReady(IntegrationError): ...
class ConfigEntryError(IntegrationError): ...
class ConfigEntryNotReady(IntegrationError): ...
class ConfigEntryAuthFailed(IntegrationError): ...
class InvalidStateError(HomeAssistantError): ...

class Unauthorized(HomeAssistantError):
    context: Incomplete
    user_id: Incomplete
    entity_id: Incomplete
    config_entry_id: Incomplete
    perm_category: Incomplete
    permission: Incomplete
    def __init__(self, context: Context | None = None, user_id: str | None = None, entity_id: str | None = None, config_entry_id: str | None = None, perm_category: str | None = None, permission: str | None = None) -> None: ...

class UnknownUser(Unauthorized): ...

class ServiceNotFound(ServiceValidationError):
    domain: Incomplete
    service: Incomplete
    generate_message: bool
    def __init__(self, domain: str, service: str) -> None: ...

class ServiceNotSupported(ServiceValidationError):
    domain: Incomplete
    service: Incomplete
    generate_message: bool
    def __init__(self, domain: str, service: str, entity_id: str) -> None: ...

class MaxLengthExceeded(HomeAssistantError):
    value: Incomplete
    property_name: Incomplete
    max_length: Incomplete
    generate_message: bool
    def __init__(self, value: EventType[Any] | str, property_name: str, max_length: int) -> None: ...

class DependencyError(HomeAssistantError):
    failed_dependencies: Incomplete
    def __init__(self, failed_dependencies: list[str]) -> None: ...
