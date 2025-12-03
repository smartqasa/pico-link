from typing import Final, TypedDict

DOMAIN: str
CONF_BINDKEY: Final[str]
CONF_DISCOVERED_EVENT_CLASSES: Final[str]
CONF_SLEEPY_DEVICE: Final[str]
CONF_SUBTYPE: Final[str]
EVENT_TYPE: Final[str]
EVENT_CLASS: Final[str]
EVENT_PROPERTIES: Final[str]
BTHOME_BLE_EVENT: Final[str]
EVENT_CLASS_BUTTON: Final[str]
EVENT_CLASS_DIMMER: Final[str]
CONF_EVENT_CLASS: Final[str]
CONF_EVENT_PROPERTIES: Final[str]

class BTHomeBleEvent(TypedDict):
    device_id: str
    address: str
    event_class: str
    event_type: str
    event_properties: dict[str, str | int | float | None] | None
