from .models import USBDevice as USBDevice
from serial.tools.list_ports_common import ListPortInfo as ListPortInfo

def usb_device_from_port(port: ListPortInfo) -> USBDevice: ...
