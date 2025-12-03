import contextlib
from .coordinator import DeviceCoordinator as DeviceCoordinator
from _typeshed import Incomplete
from collections.abc import Generator
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

_LOGGER: Incomplete

class WemoEntity(CoordinatorEntity[DeviceCoordinator]):
    _name_suffix: str | None
    _unique_id_suffix: str | None
    wemo: Incomplete
    _device_info: Incomplete
    def __init__(self, coordinator: DeviceCoordinator) -> None: ...
    @property
    def name_suffix(self) -> str | None: ...
    @property
    def name(self) -> str: ...
    @property
    def unique_id_suffix(self) -> str | None: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @contextlib.contextmanager
    def _wemo_call_wrapper(self, message: str) -> Generator[None]: ...

class WemoBinaryStateEntity(WemoEntity):
    @property
    def is_on(self) -> bool: ...
