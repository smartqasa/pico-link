from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET
from typing import Final

DOMAIN: Final[str]
ATTR_ACCESS_TOKEN: Final[str]
ATTR_REFRESH_TOKEN: Final[str]
ATTR_LAST_SAVED_AT: Final[str]
ATTR_DURATION: Final[str]
ATTR_DISTANCE: Final[str]
ATTR_ELEVATION: Final[str]
ATTR_HEIGHT: Final[str]
ATTR_WEIGHT: Final[str]
ATTR_BODY: Final[str]
ATTR_LIQUIDS: Final[str]
ATTR_BLOOD_GLUCOSE: Final[str]
ATTR_BATTERY: Final[str]
CONF_MONITORED_RESOURCES: Final[str]
CONF_CLOCK_FORMAT: Final[str]
ATTRIBUTION: Final[str]
FITBIT_AUTH_CALLBACK_PATH: Final[str]
FITBIT_AUTH_START: Final[str]
FITBIT_CONFIG_FILE: Final[str]
FITBIT_DEFAULT_RESOURCES: Final[list[str]]
DEFAULT_CONFIG: Final[dict[str, str]]
DEFAULT_CLOCK_FORMAT: Final[str]
BATTERY_LEVELS: Final[dict[str, int]]

class FitbitUnitSystem(StrEnum):
    LEGACY_DEFAULT = 'default'
    METRIC = 'metric'
    EN_US = 'en_US'
    EN_GB = 'en_GB'

CONF_SCOPE: Final[str]

class FitbitScope(StrEnum):
    ACTIVITY = 'activity'
    HEART_RATE = 'heartrate'
    NUTRITION = 'nutrition'
    PROFILE = 'profile'
    DEVICE = 'settings'
    SLEEP = 'sleep'
    WEIGHT = 'weight'

OAUTH2_AUTHORIZE: str
OAUTH2_TOKEN: str
OAUTH_SCOPES: Incomplete
