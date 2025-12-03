from .const import ATTR_FAN_MODE as ATTR_FAN_MODE, ATTR_HUMIDITY as ATTR_HUMIDITY, ATTR_HVAC_MODE as ATTR_HVAC_MODE, ATTR_PRESET_MODE as ATTR_PRESET_MODE, ATTR_SWING_HORIZONTAL_MODE as ATTR_SWING_HORIZONTAL_MODE, ATTR_SWING_MODE as ATTR_SWING_MODE, ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, DOMAIN as DOMAIN, HVAC_MODES as HVAC_MODES, SERVICE_SET_FAN_MODE as SERVICE_SET_FAN_MODE, SERVICE_SET_HUMIDITY as SERVICE_SET_HUMIDITY, SERVICE_SET_HVAC_MODE as SERVICE_SET_HVAC_MODE, SERVICE_SET_PRESET_MODE as SERVICE_SET_PRESET_MODE, SERVICE_SET_SWING_HORIZONTAL_MODE as SERVICE_SET_SWING_HORIZONTAL_MODE, SERVICE_SET_SWING_MODE as SERVICE_SET_SWING_MODE, SERVICE_SET_TEMPERATURE as SERVICE_SET_TEMPERATURE
from collections.abc import Iterable
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State
from typing import Any

async def _async_reproduce_states(hass: HomeAssistant, state: State, *, context: Context | None = None, reproduce_options: dict[str, Any] | None = None) -> None: ...
async def async_reproduce_states(hass: HomeAssistant, states: Iterable[State], *, context: Context | None = None, reproduce_options: dict[str, Any] | None = None) -> None: ...
