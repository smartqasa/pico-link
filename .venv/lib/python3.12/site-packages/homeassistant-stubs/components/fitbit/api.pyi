import abc
from .const import FitbitUnitSystem as FitbitUnitSystem
from .exceptions import FitbitApiException as FitbitApiException, FitbitAuthException as FitbitAuthException
from .model import FitbitDevice as FitbitDevice, FitbitProfile as FitbitProfile
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Callable as Callable
from fitbit import Fitbit
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.util.unit_system import METRIC_SYSTEM as METRIC_SYSTEM
from typing import Any

_LOGGER: Incomplete
CONF_REFRESH_TOKEN: str
CONF_EXPIRES_AT: str

class FitbitApi(ABC, metaclass=abc.ABCMeta):
    _hass: Incomplete
    _profile: FitbitProfile | None
    _unit_system: Incomplete
    def __init__(self, hass: HomeAssistant, unit_system: FitbitUnitSystem | None = None) -> None: ...
    @abstractmethod
    async def async_get_access_token(self) -> dict[str, Any]: ...
    async def _async_get_client(self) -> Fitbit: ...
    async def async_get_user_profile(self) -> FitbitProfile: ...
    async def async_get_unit_system(self) -> FitbitUnitSystem: ...
    async def async_get_devices(self) -> list[FitbitDevice]: ...
    async def async_get_latest_time_series(self, resource_type: str) -> dict[str, Any]: ...
    async def _run[_T](self, func: Callable[[], _T]) -> _T: ...

class OAuthFitbitApi(FitbitApi):
    _oauth_session: Incomplete
    def __init__(self, hass: HomeAssistant, oauth_session: config_entry_oauth2_flow.OAuth2Session, unit_system: FitbitUnitSystem | None = None) -> None: ...
    async def async_get_access_token(self) -> dict[str, Any]: ...

class ConfigFlowFitbitApi(FitbitApi):
    _token: Incomplete
    def __init__(self, hass: HomeAssistant, token: dict[str, Any]) -> None: ...
    async def async_get_access_token(self) -> dict[str, Any]: ...
