from . import AlarmControlPanelState as AlarmControlPanelState, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, SERVICE_ALARM_ARM_AWAY as SERVICE_ALARM_ARM_AWAY, SERVICE_ALARM_ARM_CUSTOM_BYPASS as SERVICE_ALARM_ARM_CUSTOM_BYPASS, SERVICE_ALARM_ARM_HOME as SERVICE_ALARM_ARM_HOME, SERVICE_ALARM_ARM_NIGHT as SERVICE_ALARM_ARM_NIGHT, SERVICE_ALARM_ARM_VACATION as SERVICE_ALARM_ARM_VACATION, SERVICE_ALARM_DISARM as SERVICE_ALARM_DISARM, SERVICE_ALARM_TRIGGER as SERVICE_ALARM_TRIGGER
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State
from typing import Any, Final

_LOGGER: Final[Incomplete]
VALID_STATES: Final[set[str]]

async def _async_reproduce_state(hass: HomeAssistant, state: State, *, context: Context | None = None, reproduce_options: dict[str, Any] | None = None) -> None: ...
async def async_reproduce_states(hass: HomeAssistant, states: Iterable[State], *, context: Context | None = None, reproduce_options: dict[str, Any] | None = None) -> None: ...
