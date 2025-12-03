from .const import API_TEMP_UNITS as API_TEMP_UNITS
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Literal

class UnsupportedProperty(HomeAssistantError): ...
class NoTokenAvailable(HomeAssistantError): ...
class RequireRelink(Exception): ...

class AlexaError(Exception):
    namespace: str | None
    error_type: str | None
    error_message: Incomplete
    payload: Incomplete
    def __init__(self, error_message: str, payload: dict[str, Any] | None = None) -> None: ...

class AlexaInvalidEndpointError(AlexaError):
    namespace: str
    error_type: str
    endpoint_id: Incomplete
    def __init__(self, endpoint_id: str) -> None: ...

class AlexaInvalidValueError(AlexaError):
    namespace: str
    error_type: str

class AlexaInteralError(AlexaError):
    namespace: str
    error_type: str

class AlexaNotSupportedInCurrentMode(AlexaError):
    namespace: str
    error_type: str
    endpoint_id: Incomplete
    def __init__(self, endpoint_id: str, current_mode: Literal['COLOR', 'ASLEEP', 'NOT_PROVISIONED', 'OTHER']) -> None: ...

class AlexaUnsupportedThermostatModeError(AlexaError):
    namespace: str
    error_type: str

class AlexaUnsupportedThermostatTargetStateError(AlexaError):
    namespace: str
    error_type: str

class AlexaTempRangeError(AlexaError):
    namespace: str
    error_type: str
    def __init__(self, hass: HomeAssistant, temp: float, min_temp: float, max_temp: float) -> None: ...

class AlexaBridgeUnreachableError(AlexaError):
    namespace: str
    error_type: str

class AlexaSecurityPanelUnauthorizedError(AlexaError):
    namespace: str
    error_type: str

class AlexaSecurityPanelAuthorizationRequired(AlexaError):
    namespace: str
    error_type: str

class AlexaAlreadyInOperationError(AlexaError):
    namespace: str
    error_type: str

class AlexaInvalidDirectiveError(AlexaError):
    namespace: str
    error_type: str

class AlexaVideoActionNotPermittedForContentError(AlexaError):
    namespace: str
    error_type: str
