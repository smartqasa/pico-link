from . import get_device_tuple_from_identifiers as get_device_tuple_from_identifiers
from RFXtrx import RFXtrxDevice as RFXtrxDevice
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

@callback
def async_get_device_object(hass: HomeAssistant, device_id: str) -> RFXtrxDevice: ...
