from . import ADB_PYTHON_EXCEPTIONS as ADB_PYTHON_EXCEPTIONS, ADB_TCP_EXCEPTIONS as ADB_TCP_EXCEPTIONS, AndroidTVConfigEntry as AndroidTVConfigEntry, get_androidtv_mac as get_androidtv_mac
from .const import DEVICE_ANDROIDTV as DEVICE_ANDROIDTV, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable, Coroutine
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS, ATTR_IDENTIFIERS as ATTR_IDENTIFIERS, ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_MODEL as ATTR_MODEL, ATTR_SW_VERSION as ATTR_SW_VERSION, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from typing import Any, Concatenate

PREFIX_ANDROIDTV: str
PREFIX_FIRETV: str
_LOGGER: Incomplete
type _FuncType[_T, **_P, _R] = Callable[Concatenate[_T, _P], Awaitable[_R]]
type _ReturnFuncType[_T, **_P, _R] = Callable[Concatenate[_T, _P], Coroutine[Any, Any, _R | None]]

def adb_decorator[_ADBDeviceT: AndroidTVEntity, **_P, _R](override_available: bool = False) -> Callable[[_FuncType[_ADBDeviceT, _P, _R]], _ReturnFuncType[_ADBDeviceT, _P, _R]]: ...

class AndroidTVEntity(Entity):
    _attr_has_entity_name: bool
    aftv: Incomplete
    _attr_unique_id: Incomplete
    _entry_runtime_data: Incomplete
    _attr_device_info: Incomplete
    exceptions: Incomplete
    def __init__(self, entry: AndroidTVConfigEntry) -> None: ...
