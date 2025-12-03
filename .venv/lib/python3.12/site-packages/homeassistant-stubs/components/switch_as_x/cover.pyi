from .const import CONF_INVERT as CONF_INVERT
from .entity import BaseInvertableEntity as BaseInvertableEntity
from _typeshed import Incomplete
from homeassistant.components.cover import CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_ENTITY_ID as CONF_ENTITY_ID, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CoverSwitch(BaseInvertableEntity, CoverEntity):
    _attr_supported_features: Incomplete
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    _attr_is_closed: Incomplete
    @callback
    def async_state_changed_listener(self, event: Event[EventStateChangedData] | None = None) -> None: ...
