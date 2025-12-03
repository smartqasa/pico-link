import voluptuous as vol
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

class BlueprintException(HomeAssistantError):
    domain: Incomplete
    def __init__(self, domain: str | None, msg: str) -> None: ...

class BlueprintWithNameException(BlueprintException):
    blueprint_name: Incomplete
    def __init__(self, domain: str | None, blueprint_name: str | None, msg: str) -> None: ...

class FailedToLoad(BlueprintWithNameException):
    def __init__(self, domain: str, blueprint_name: str, exc: Exception) -> None: ...

class InvalidBlueprint(BlueprintWithNameException):
    blueprint_data: Incomplete
    def __init__(self, domain: str | None, blueprint_name: str | None, blueprint_data: Any, msg_or_exc: str | vol.Invalid) -> None: ...

class InvalidBlueprintInputs(BlueprintException):
    def __init__(self, domain: str, msg: str) -> None: ...

class MissingInput(BlueprintWithNameException):
    def __init__(self, domain: str, blueprint_name: str, input_names: Iterable[str]) -> None: ...

class FileAlreadyExists(BlueprintWithNameException):
    def __init__(self, domain: str, blueprint_name: str) -> None: ...

class BlueprintInUse(BlueprintWithNameException):
    def __init__(self, domain: str, blueprint_name: str) -> None: ...
