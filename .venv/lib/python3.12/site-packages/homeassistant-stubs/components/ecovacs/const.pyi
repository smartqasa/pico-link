from _typeshed import Incomplete
from enum import StrEnum

DOMAIN: str
CONF_CONTINENT: str
CONF_OVERRIDE_REST_URL: str
CONF_OVERRIDE_MQTT_URL: str
CONF_VERIFY_MQTT_CERTIFICATE: str
SUPPORTED_LIFESPANS: Incomplete
SUPPORTED_STATION_ACTIONS: Incomplete
LEGACY_SUPPORTED_LIFESPANS: Incomplete

class InstanceMode(StrEnum):
    CLOUD = 'cloud'
    SELF_HOSTED = 'self_hosted'
