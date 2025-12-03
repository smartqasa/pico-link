from .. import get_instance as get_instance
from ..const import SupportedDialect as SupportedDialect
from ..core import Recorder as Recorder
from ..util import session_scope as session_scope
from _typeshed import Incomplete
from homeassistant.components import system_health as system_health
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

DIALECT_TO_GET_SIZE: Incomplete

@callback
def async_register(hass: HomeAssistant, register: system_health.SystemHealthRegistration) -> None: ...
def _get_db_stats(instance: Recorder, database_name: str) -> dict[str, Any]: ...
@callback
def _async_get_db_engine_info(instance: Recorder) -> dict[str, Any]: ...
async def system_health_info(hass: HomeAssistant) -> dict[str, Any]: ...
