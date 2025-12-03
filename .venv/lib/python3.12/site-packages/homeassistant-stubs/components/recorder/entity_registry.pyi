from .core import Recorder as Recorder
from .util import filter_unique_constraint_integrity_error as filter_unique_constraint_integrity_error, get_instance as get_instance, session_scope as session_scope
from _typeshed import Incomplete
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.start import async_at_start as async_at_start

_LOGGER: Incomplete

@callback
def async_setup(hass: HomeAssistant) -> None: ...
def update_states_metadata(instance: Recorder, entity_id: str, new_entity_id: str) -> None: ...
