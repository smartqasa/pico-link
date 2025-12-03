from _typeshed import Incomplete
from collections.abc import Callable, Coroutine
from homeassistant.core import HassJob as HassJob, HassJobType as HassJobType, HomeAssistant as HomeAssistant, callback as callback, get_hassjob_callable_job_type as get_hassjob_callable_job_type
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.async_ import run_callback_threadsafe as run_callback_threadsafe
from homeassistant.util.logging import catch_log_exception as catch_log_exception, log_exception as log_exception
from homeassistant.util.signal_type import SignalType as SignalType
from typing import Any, overload

_LOGGER: Incomplete
DATA_DISPATCHER: str
type _DispatcherDataType[*_Ts] = dict[SignalType[*_Ts] | str, dict[Callable[[*_Ts], Any] | Callable[..., Any], HassJob[..., None | Coroutine[Any, Any, None]] | None]]

@overload
@bind_hass
def dispatcher_connect[*_Ts](hass: HomeAssistant, signal: SignalType[*_Ts], target: Callable[[*_Ts], None]) -> Callable[[], None]: ...
@overload
@bind_hass
def dispatcher_connect(hass: HomeAssistant, signal: str, target: Callable[..., None]) -> Callable[[], None]: ...
@callback
def _async_remove_dispatcher[*_Ts](dispatchers: _DispatcherDataType[*_Ts], signal: SignalType[*_Ts] | str, target: Callable[[*_Ts], Any] | Callable[..., Any]) -> None: ...
@overload
@callback
@bind_hass
def async_dispatcher_connect[*_Ts](hass: HomeAssistant, signal: SignalType[*_Ts], target: Callable[[*_Ts], Any]) -> Callable[[], None]: ...
@overload
@callback
@bind_hass
def async_dispatcher_connect(hass: HomeAssistant, signal: str, target: Callable[..., Any]) -> Callable[[], None]: ...
@overload
@bind_hass
def dispatcher_send[*_Ts](hass: HomeAssistant, signal: SignalType[*_Ts], *args: *_Ts) -> None: ...
@overload
@bind_hass
def dispatcher_send(hass: HomeAssistant, signal: str, *args: Any) -> None: ...
def _format_err[*_Ts](signal: SignalType[*_Ts] | str, target: Callable[[*_Ts], Any] | Callable[..., Any], *args: Any) -> str: ...
def _generate_job[*_Ts](signal: SignalType[*_Ts] | str, target: Callable[[*_Ts], Any] | Callable[..., Any]) -> HassJob[..., Coroutine[Any, Any, None] | None]: ...
@overload
@callback
@bind_hass
def async_dispatcher_send[*_Ts](hass: HomeAssistant, signal: SignalType[*_Ts], *args: *_Ts) -> None: ...
@overload
@callback
@bind_hass
def async_dispatcher_send(hass: HomeAssistant, signal: str, *args: Any) -> None: ...
@callback
@bind_hass
def async_dispatcher_send_internal[*_Ts](hass: HomeAssistant, signal: SignalType[*_Ts] | str, *args: *_Ts) -> None: ...
