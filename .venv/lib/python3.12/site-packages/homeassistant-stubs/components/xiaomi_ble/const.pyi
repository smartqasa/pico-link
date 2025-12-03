from typing import Final, TypedDict

DOMAIN: str
CONF_DISCOVERED_EVENT_CLASSES: Final[str]
CONF_EVENT_PROPERTIES: Final[str]
CONF_EVENT_CLASS: Final[str]
CONF_SLEEPY_DEVICE: Final[str]
CONF_SUBTYPE: Final[str]
EVENT_CLASS: Final[str]
EVENT_TYPE: Final[str]
EVENT_SUBTYPE: Final[str]
EVENT_PROPERTIES: Final[str]
XIAOMI_BLE_EVENT: Final[str]
EVENT_CLASS_BUTTON: Final[str]
EVENT_CLASS_CUBE: Final[str]
EVENT_CLASS_DIMMER: Final[str]
EVENT_CLASS_ERROR: Final[str]
EVENT_CLASS_FINGERPRINT: Final[str]
EVENT_CLASS_LOCK: Final[str]
EVENT_CLASS_MOTION: Final[str]
BUTTON: Final[str]
CUBE: Final[str]
DIMMER: Final[str]
ERROR: Final[str]
FINGERPRINT: Final[str]
LOCK: Final[str]
LOCK_FINGERPRINT: str
MOTION_DEVICE: Final[str]
DOUBLE_BUTTON: Final[str]
TRIPPLE_BUTTON: Final[str]
REMOTE: Final[str]
REMOTE_FAN: Final[str]
REMOTE_VENFAN: Final[str]
REMOTE_BATHROOM: Final[str]
MOTION: Final[str]
BUTTON_PRESS: Final[str]
BUTTON_PRESS_LONG: Final[str]
BUTTON_PRESS_DOUBLE_LONG: Final[str]
DOUBLE_BUTTON_PRESS_DOUBLE_LONG: Final[str]
TRIPPLE_BUTTON_PRESS_DOUBLE_LONG: Final[str]

class XiaomiBleEvent(TypedDict):
    device_id: str
    address: str
    event_class: str
    event_type: str
    event_properties: dict[str, str | int | float | None] | None
