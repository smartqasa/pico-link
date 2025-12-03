import asyncio
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Generator
from contextlib import contextmanager
from dataclasses import dataclass, field
from homeassistant.components.recorder import Recorder as Recorder
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.util.hass_dict import HassKey as HassKey
from sqlalchemy.orm.session import Session as Session
from typing import Any

_LOGGER: Incomplete
DOMAIN: HassKey[RecorderData]
DATA_INSTANCE: HassKey[Recorder]

@dataclass(slots=True)
class RecorderData:
    recorder_platforms: dict[str, Any] = field(default_factory=dict)
    db_connected: asyncio.Future[bool] = field(default_factory=asyncio.Future)

@callback
def async_migration_in_progress(hass: HomeAssistant) -> bool: ...
@callback
def async_migration_is_live(hass: HomeAssistant) -> bool: ...
@callback
def async_initialize_recorder(hass: HomeAssistant) -> None: ...
async def async_wait_recorder(hass: HomeAssistant) -> bool: ...
def get_instance(hass: HomeAssistant) -> Recorder: ...
@contextmanager
def session_scope(*, hass: HomeAssistant | None = None, session: Session | None = None, exception_filter: Callable[[Exception], bool] | None = None, read_only: bool = False) -> Generator[Session]: ...
