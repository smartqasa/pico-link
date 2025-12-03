from .const import ATTR_DURATION as ATTR_DURATION, ATTR_ROTATION as ATTR_ROTATION, CONF_ANGLE as CONF_ANGLE, CONF_GESTURE as CONF_GESTURE, LOGGER as LOGGER
from .entity import DeconzBase as DeconzBase
from .hub import DeconzHub as DeconzHub
from _typeshed import Incomplete
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_EVENT as CONF_EVENT, CONF_ID as CONF_ID, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_XY as CONF_XY
from homeassistant.core import callback as callback
from homeassistant.util import slugify as slugify
from pydeconz.models.event import EventType as EventType
from pydeconz.models.sensor.ancillary_control import AncillaryControl
from pydeconz.models.sensor.presence import Presence
from pydeconz.models.sensor.relative_rotary import RelativeRotary
from pydeconz.models.sensor.switch import Switch

CONF_DECONZ_EVENT: str
CONF_DECONZ_ALARM_EVENT: str
CONF_DECONZ_PRESENCE_EVENT: str
CONF_DECONZ_RELATIVE_ROTARY_EVENT: str
SUPPORTED_DECONZ_ALARM_EVENTS: Incomplete
SUPPORTED_DECONZ_PRESENCE_EVENTS: Incomplete
RELATIVE_ROTARY_DECONZ_TO_EVENT: Incomplete

async def async_setup_events(hub: DeconzHub) -> None: ...
@callback
def async_unload_events(hub: DeconzHub) -> None: ...

class DeconzEventBase(DeconzBase):
    _unsubscribe: Incomplete
    device: Incomplete
    device_id: str | None
    event_id: Incomplete
    def __init__(self, device: AncillaryControl | Presence | RelativeRotary | Switch, hub: DeconzHub) -> None: ...
    @callback
    def async_will_remove_from_hass(self) -> None: ...
    @callback
    def async_update_callback(self) -> None: ...
    async def async_update_device_registry(self) -> None: ...

class DeconzEvent(DeconzEventBase):
    _device: Switch
    @callback
    def async_update_callback(self) -> None: ...

class DeconzAlarmEvent(DeconzEventBase):
    _device: AncillaryControl
    @callback
    def async_update_callback(self) -> None: ...

class DeconzPresenceEvent(DeconzEventBase):
    _device: Presence
    @callback
    def async_update_callback(self) -> None: ...

class DeconzRelativeRotaryEvent(DeconzEventBase):
    _device: RelativeRotary
    @callback
    def async_update_callback(self) -> None: ...
