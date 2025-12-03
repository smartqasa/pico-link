from .const import ATTR_DEVICE_TRACKER as ATTR_DEVICE_TRACKER
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.util import slugify as slugify
from typing import Any

class Device:
    _mac: Incomplete
    _params: Incomplete
    _last_seen: datetime | None
    _attrs: dict[str, Any]
    _wireless_params: dict[str, Any]
    def __init__(self, mac: str, params: dict[str, Any]) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def ip_address(self) -> str | None: ...
    @property
    def mac(self) -> str: ...
    @property
    def last_seen(self) -> datetime | None: ...
    @property
    def attrs(self) -> dict[str, Any]: ...
    def update(self, wireless_params: dict[str, Any] | None = None, params: dict[str, Any] | None = None, active: bool = False) -> None: ...
