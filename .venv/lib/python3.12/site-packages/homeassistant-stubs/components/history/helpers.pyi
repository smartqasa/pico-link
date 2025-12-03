from collections.abc import Iterable
from datetime import datetime as dt
from homeassistant.components.recorder import get_instance as get_instance
from homeassistant.core import HomeAssistant as HomeAssistant

def entities_may_have_state_changes_after(hass: HomeAssistant, entity_ids: Iterable, start_time: dt, no_attributes: bool) -> bool: ...
def has_states_before(hass: HomeAssistant, run_time: dt) -> bool: ...
