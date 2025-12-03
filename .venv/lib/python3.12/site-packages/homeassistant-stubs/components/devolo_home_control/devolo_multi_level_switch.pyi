from .entity import DevoloDeviceEntity as DevoloDeviceEntity
from _typeshed import Incomplete
from devolo_home_control_api.devices.zwave import Zwave as Zwave
from devolo_home_control_api.homecontrol import HomeControl as HomeControl

class DevoloMultiLevelSwitchDeviceEntity(DevoloDeviceEntity):
    _attr_name: Incomplete
    _multi_level_switch_property: Incomplete
    _value: Incomplete
    def __init__(self, homecontrol: HomeControl, device_instance: Zwave, element_uid: str) -> None: ...
