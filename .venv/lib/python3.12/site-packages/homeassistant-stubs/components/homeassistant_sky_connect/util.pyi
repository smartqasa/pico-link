from .const import HardwareVariant as HardwareVariant
from _typeshed import Incomplete
from homeassistant.components import usb as usb
from homeassistant.config_entries import ConfigEntry as ConfigEntry

_LOGGER: Incomplete

def get_usb_service_info(config_entry: ConfigEntry) -> usb.UsbServiceInfo: ...
def get_hardware_variant(config_entry: ConfigEntry) -> HardwareVariant: ...
