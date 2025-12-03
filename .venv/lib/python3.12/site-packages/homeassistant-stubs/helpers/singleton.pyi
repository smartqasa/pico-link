from collections.abc import Callable
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import overload

type _FuncType[_T] = Callable[[HomeAssistant], _T]
@overload
def singleton[_T](data_key: HassKey[_T]) -> Callable[[_FuncType[_T]], _FuncType[_T]]: ...
@overload
def singleton[_T](data_key: str) -> Callable[[_FuncType[_T]], _FuncType[_T]]: ...
