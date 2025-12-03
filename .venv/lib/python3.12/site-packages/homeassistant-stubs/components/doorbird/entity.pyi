from .const import DOORBIRD_INFO_KEY_BUILD_NUMBER as DOORBIRD_INFO_KEY_BUILD_NUMBER, DOORBIRD_INFO_KEY_DEVICE_TYPE as DOORBIRD_INFO_KEY_DEVICE_TYPE, DOORBIRD_INFO_KEY_FIRMWARE as DOORBIRD_INFO_KEY_FIRMWARE, MANUFACTURER as MANUFACTURER
from .models import DoorBirdData as DoorBirdData
from .util import get_mac_address_from_door_station_info as get_mac_address_from_door_station_info
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity

class DoorBirdEntity(Entity):
    _attr_has_entity_name: bool
    _door_bird_data: Incomplete
    _door_station: Incomplete
    _mac_addr: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, door_bird_data: DoorBirdData) -> None: ...
