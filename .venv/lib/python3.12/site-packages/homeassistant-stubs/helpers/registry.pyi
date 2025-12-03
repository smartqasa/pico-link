import abc
from .storage import Store as Store
from abc import ABC, abstractmethod
from collections import UserDict, defaultdict
from collections.abc import Mapping as Mapping, Sequence as Sequence, ValuesView
from homeassistant.core import CoreState as CoreState, HomeAssistant as HomeAssistant, callback as callback
from typing import Any, Literal

SAVE_DELAY: int
SAVE_DELAY_LONG: int
type RegistryIndexType = defaultdict[str, dict[str, Literal[True]]]

class BaseRegistryItems[_DataT](UserDict[str, _DataT], ABC, metaclass=abc.ABCMeta):
    data: dict[str, _DataT]
    def values(self) -> ValuesView[_DataT]: ...
    @abstractmethod
    def _index_entry(self, key: str, entry: _DataT) -> None: ...
    @abstractmethod
    def _unindex_entry(self, key: str, replacement_entry: _DataT | None = None) -> None: ...
    def __setitem__(self, key: str, entry: _DataT) -> None: ...
    def _unindex_entry_value(self, key: str, value: str, index: RegistryIndexType) -> None: ...
    def __delitem__(self, key: str) -> None: ...

class BaseRegistry[_StoreDataT: Mapping[str, Any] | Sequence[Any]](ABC, metaclass=abc.ABCMeta):
    hass: HomeAssistant
    _store: Store[_StoreDataT]
    @callback
    def async_schedule_save(self) -> None: ...
    @callback
    @abstractmethod
    def _data_to_save(self) -> _StoreDataT: ...
