from .core import EventStateChangedData as EventStateChangedData, EventStateReportedData as EventStateReportedData
from .helpers.deprecation import DeprecatedConstant as DeprecatedConstant, DeprecatedConstantEnum as DeprecatedConstantEnum, EnumWithDeprecatedMembers as EnumWithDeprecatedMembers, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from .helpers.typing import NoEventData as NoEventData
from .util.event_type import EventType as EventType
from .util.hass_dict import HassKey as HassKey
from .util.signal_type import SignalType as SignalType
from _typeshed import Incomplete
from enum import StrEnum
from typing import Final

APPLICATION_NAME: Final[str]
MAJOR_VERSION: Final[int]
MINOR_VERSION: Final[int]
PATCH_VERSION: Final[str]
__short_version__: Final[Incomplete]
__version__: Final[Incomplete]
REQUIRED_PYTHON_VER: Final[tuple[int, int, int]]
REQUIRED_NEXT_PYTHON_VER: Final[tuple[int, int, int]]
REQUIRED_NEXT_PYTHON_HA_RELEASE: Final[str]
PLATFORM_FORMAT: Final[str]

class Platform(StrEnum):
    AIR_QUALITY = 'air_quality'
    ALARM_CONTROL_PANEL = 'alarm_control_panel'
    ASSIST_SATELLITE = 'assist_satellite'
    BINARY_SENSOR = 'binary_sensor'
    BUTTON = 'button'
    CALENDAR = 'calendar'
    CAMERA = 'camera'
    CLIMATE = 'climate'
    CONVERSATION = 'conversation'
    COVER = 'cover'
    DATE = 'date'
    DATETIME = 'datetime'
    DEVICE_TRACKER = 'device_tracker'
    EVENT = 'event'
    FAN = 'fan'
    GEO_LOCATION = 'geo_location'
    HUMIDIFIER = 'humidifier'
    IMAGE = 'image'
    IMAGE_PROCESSING = 'image_processing'
    LAWN_MOWER = 'lawn_mower'
    LIGHT = 'light'
    LOCK = 'lock'
    MEDIA_PLAYER = 'media_player'
    NOTIFY = 'notify'
    NUMBER = 'number'
    REMOTE = 'remote'
    SCENE = 'scene'
    SELECT = 'select'
    SENSOR = 'sensor'
    SIREN = 'siren'
    STT = 'stt'
    SWITCH = 'switch'
    TEXT = 'text'
    TIME = 'time'
    TODO = 'todo'
    TTS = 'tts'
    UPDATE = 'update'
    VACUUM = 'vacuum'
    VALVE = 'valve'
    WAKE_WORD = 'wake_word'
    WATER_HEATER = 'water_heater'
    WEATHER = 'weather'

BASE_PLATFORMS: Final[Incomplete]
MATCH_ALL: Final[str]
ENTITY_MATCH_NONE: Final[str]
ENTITY_MATCH_ALL: Final[str]
ENTITY_MATCH_ANY: Final[str]
DEVICE_DEFAULT_NAME: Final[str]
MAX_LENGTH_EVENT_EVENT_TYPE: Final[int]
MAX_LENGTH_EVENT_ORIGIN: Final[int]
MAX_LENGTH_EVENT_CONTEXT_ID: Final[int]
MAX_LENGTH_STATE_DOMAIN: Final[int]
MAX_LENGTH_STATE_ENTITY_ID: Final[int]
MAX_LENGTH_STATE_STATE: Final[int]
SUN_EVENT_SUNSET: Final[str]
SUN_EVENT_SUNRISE: Final[str]
CONF_ABOVE: Final[str]
CONF_ACCESS_TOKEN: Final[str]
CONF_ACTION: Final[str]
CONF_ADDRESS: Final[str]
CONF_AFTER: Final[str]
CONF_ALIAS: Final[str]
CONF_LLM_HASS_API: str
CONF_ALLOWLIST_EXTERNAL_URLS: Final[str]
CONF_API_KEY: Final[str]
CONF_API_TOKEN: Final[str]
CONF_API_VERSION: Final[str]
CONF_ARMING_TIME: Final[str]
CONF_AT: Final[str]
CONF_ATTRIBUTE: Final[str]
CONF_AUTH_MFA_MODULES: Final[str]
CONF_AUTH_PROVIDERS: Final[str]
CONF_AUTHENTICATION: Final[str]
CONF_BASE: Final[str]
CONF_BEFORE: Final[str]
CONF_BELOW: Final[str]
CONF_BINARY_SENSORS: Final[str]
CONF_BRIGHTNESS: Final[str]
CONF_BROADCAST_ADDRESS: Final[str]
CONF_BROADCAST_PORT: Final[str]
CONF_CHOOSE: Final[str]
CONF_CLIENT_ID: Final[str]
CONF_CLIENT_SECRET: Final[str]
CONF_CODE: Final[str]
CONF_COLOR_TEMP: Final[str]
CONF_COMMAND: Final[str]
CONF_COMMAND_CLOSE: Final[str]
CONF_COMMAND_OFF: Final[str]
CONF_COMMAND_ON: Final[str]
CONF_COMMAND_OPEN: Final[str]
CONF_COMMAND_STATE: Final[str]
CONF_COMMAND_STOP: Final[str]
CONF_CONDITION: Final[str]
CONF_CONDITIONS: Final[str]
CONF_CONTINUE_ON_ERROR: Final[str]
CONF_CONTINUE_ON_TIMEOUT: Final[str]
CONF_COUNT: Final[str]
CONF_COUNTRY: Final[str]
CONF_COUNTRY_CODE: Final[str]
CONF_COVERS: Final[str]
CONF_CURRENCY: Final[str]
CONF_CUSTOMIZE: Final[str]
CONF_CUSTOMIZE_DOMAIN: Final[str]
CONF_CUSTOMIZE_GLOB: Final[str]
CONF_DEFAULT: Final[str]
CONF_DELAY: Final[str]
CONF_DELAY_TIME: Final[str]
CONF_DESCRIPTION: Final[str]
CONF_DEVICE: Final[str]
CONF_DEVICES: Final[str]
CONF_DEVICE_CLASS: Final[str]
CONF_DEVICE_ID: Final[str]
CONF_DISARM_AFTER_TRIGGER: Final[str]
CONF_DISCOVERY: Final[str]
CONF_DISKS: Final[str]
CONF_DISPLAY_CURRENCY: Final[str]
CONF_DISPLAY_OPTIONS: Final[str]
CONF_DOMAIN: Final[str]
CONF_DOMAINS: Final[str]
CONF_EFFECT: Final[str]
CONF_ELEVATION: Final[str]
CONF_ELSE: Final[str]
CONF_EMAIL: Final[str]
CONF_ENABLED: Final[str]
CONF_ENTITIES: Final[str]
CONF_ENTITY_CATEGORY: Final[str]
CONF_ENTITY_ID: Final[str]
CONF_ENTITY_NAMESPACE: Final[str]
CONF_ENTITY_PICTURE_TEMPLATE: Final[str]
CONF_ERROR: Final[str]
CONF_EVENT: Final[str]
CONF_EVENT_DATA: Final[str]
CONF_EVENT_DATA_TEMPLATE: Final[str]
CONF_EXCLUDE: Final[str]
CONF_EXTERNAL_URL: Final[str]
CONF_FILENAME: Final[str]
CONF_FILE_PATH: Final[str]
CONF_FOR: Final[str]
CONF_FOR_EACH: Final[str]
CONF_FORCE_UPDATE: Final[str]
CONF_FRIENDLY_NAME: Final[str]
CONF_FRIENDLY_NAME_TEMPLATE: Final[str]
CONF_HEADERS: Final[str]
CONF_HOST: Final[str]
CONF_HOSTS: Final[str]
CONF_HS: Final[str]
CONF_ICON: Final[str]
CONF_ICON_TEMPLATE: Final[str]
CONF_ID: Final[str]
CONF_IF: Final[str]
CONF_INCLUDE: Final[str]
CONF_INTERNAL_URL: Final[str]
CONF_IP_ADDRESS: Final[str]
CONF_LANGUAGE: Final[str]
CONF_LATITUDE: Final[str]
CONF_LEGACY_TEMPLATES: Final[str]
CONF_LIGHTS: Final[str]
CONF_LOCATION: Final[str]
CONF_LONGITUDE: Final[str]
CONF_MAC: Final[str]
CONF_MATCH: Final[str]
CONF_MAXIMUM: Final[str]
CONF_MEDIA_DIRS: Final[str]
CONF_METHOD: Final[str]
CONF_MINIMUM: Final[str]
CONF_MODE: Final[str]
CONF_MODEL: Final[str]
CONF_MODEL_ID: Final[str]
CONF_MONITORED_CONDITIONS: Final[str]
CONF_MONITORED_VARIABLES: Final[str]
CONF_NAME: Final[str]
CONF_OFFSET: Final[str]
CONF_OPTIMISTIC: Final[str]
CONF_PACKAGES: Final[str]
CONF_PARALLEL: Final[str]
CONF_PARAMS: Final[str]
CONF_PASSWORD: Final[str]
CONF_PATH: Final[str]
CONF_PAYLOAD: Final[str]
CONF_PAYLOAD_OFF: Final[str]
CONF_PAYLOAD_ON: Final[str]
CONF_PENDING_TIME: Final[str]
CONF_PIN: Final[str]
CONF_PLATFORM: Final[str]
CONF_PORT: Final[str]
CONF_PREFIX: Final[str]
CONF_PROFILE_NAME: Final[str]
CONF_PROTOCOL: Final[str]
CONF_PROXY_SSL: Final[str]
CONF_QUOTE: Final[str]
CONF_RADIUS: Final[str]
CONF_RECIPIENT: Final[str]
CONF_REGION: Final[str]
CONF_REPEAT: Final[str]
CONF_RESOURCE: Final[str]
CONF_RESOURCE_TEMPLATE: Final[str]
CONF_RESOURCES: Final[str]
CONF_RESPONSE_VARIABLE: Final[str]
CONF_RGB: Final[str]
CONF_ROOM: Final[str]
CONF_SCAN_INTERVAL: Final[str]
CONF_SCENE: Final[str]
CONF_SELECTOR: Final[str]
CONF_SENDER: Final[str]
CONF_SENSORS: Final[str]
CONF_SENSOR_TYPE: Final[str]
CONF_SEQUENCE: Final[str]
CONF_SERVICE: Final[str]
CONF_SERVICE_DATA: Final[str]
CONF_SERVICE_DATA_TEMPLATE: Final[str]
CONF_SERVICE_TEMPLATE: Final[str]
CONF_SET_CONVERSATION_RESPONSE: Final[str]
CONF_SHOW_ON_MAP: Final[str]
CONF_SLAVE: Final[str]
CONF_SOURCE: Final[str]
CONF_SSL: Final[str]
CONF_STATE: Final[str]
CONF_STATE_TEMPLATE: Final[str]
CONF_STOP: Final[str]
CONF_STRUCTURE: Final[str]
CONF_SWITCHES: Final[str]
CONF_TARGET: Final[str]
CONF_TEMPERATURE_UNIT: Final[str]
CONF_THEN: Final[str]
CONF_TIMEOUT: Final[str]
CONF_TIME_ZONE: Final[str]
CONF_TOKEN: Final[str]
CONF_TRIGGER: Final[str]
CONF_TRIGGERS: Final[str]
CONF_TRIGGER_TIME: Final[str]
CONF_TTL: Final[str]
CONF_TYPE: Final[str]
CONF_UNIQUE_ID: Final[str]
CONF_UNIT_OF_MEASUREMENT: Final[str]
CONF_UNIT_SYSTEM: Final[str]
CONF_UNTIL: Final[str]
CONF_URL: Final[str]
CONF_USERNAME: Final[str]
CONF_UUID: Final[str]
CONF_VALUE_TEMPLATE: Final[str]
CONF_VARIABLES: Final[str]
CONF_VERIFY_SSL: Final[str]
CONF_WAIT_FOR_TRIGGER: Final[str]
CONF_WAIT_TEMPLATE: Final[str]
CONF_WEBHOOK_ID: Final[str]
CONF_WEEKDAY: Final[str]
CONF_WHILE: Final[str]
CONF_WHITELIST: Final[str]
CONF_ALLOWLIST_EXTERNAL_DIRS: Final[str]
LEGACY_CONF_WHITELIST_EXTERNAL_DIRS: Final[str]
CONF_DEBUG: Final[str]
CONF_XY: Final[str]
CONF_ZONE: Final[str]
EVENT_CALL_SERVICE: Final[str]
EVENT_COMPONENT_LOADED: Final[str]
EVENT_CORE_CONFIG_UPDATE: Final[str]
EVENT_HOMEASSISTANT_CLOSE: EventType[NoEventData]
EVENT_HOMEASSISTANT_START: EventType[NoEventData]
EVENT_HOMEASSISTANT_STARTED: EventType[NoEventData]
EVENT_HOMEASSISTANT_STOP: EventType[NoEventData]
EVENT_HOMEASSISTANT_FINAL_WRITE: EventType[NoEventData]
EVENT_LOGBOOK_ENTRY: Final[str]
EVENT_LOGGING_CHANGED: Final[str]
EVENT_SERVICE_REGISTERED: Final[str]
EVENT_SERVICE_REMOVED: Final[str]
EVENT_STATE_CHANGED: EventType[EventStateChangedData]
EVENT_STATE_REPORTED: EventType[EventStateReportedData]
EVENT_THEMES_UPDATED: Final[str]
EVENT_PANELS_UPDATED: Final[str]
EVENT_LOVELACE_UPDATED: Final[str]
EVENT_RECORDER_5MIN_STATISTICS_GENERATED: Final[str]
EVENT_RECORDER_HOURLY_STATISTICS_GENERATED: Final[str]
EVENT_SHOPPING_LIST_UPDATED: Final[str]
STATE_ON: Final[str]
STATE_OFF: Final[str]
STATE_HOME: Final[str]
STATE_NOT_HOME: Final[str]
STATE_UNKNOWN: Final[str]
STATE_OPEN: Final[str]
STATE_OPENING: Final[str]
STATE_CLOSED: Final[str]
STATE_CLOSING: Final[str]
STATE_BUFFERING: Final[str]
STATE_PLAYING: Final[str]
STATE_PAUSED: Final[str]
STATE_IDLE: Final[str]
STATE_STANDBY: Final[str]
STATE_UNAVAILABLE: Final[str]
STATE_OK: Final[str]
STATE_PROBLEM: Final[str]
_DEPRECATED_STATE_LOCKED: Final[Incomplete]
_DEPRECATED_STATE_UNLOCKED: Final[Incomplete]
_DEPRECATED_STATE_LOCKING: Final[Incomplete]
_DEPRECATED_STATE_UNLOCKING: Final[Incomplete]
_DEPRECATED_STATE_JAMMED: Final[Incomplete]
_DEPRECATED_STATE_ALARM_DISARMED: Final[Incomplete]
_DEPRECATED_STATE_ALARM_ARMED_HOME: Final[Incomplete]
_DEPRECATED_STATE_ALARM_ARMED_AWAY: Final[Incomplete]
_DEPRECATED_STATE_ALARM_ARMED_NIGHT: Final[Incomplete]
_DEPRECATED_STATE_ALARM_ARMED_VACATION: Final[Incomplete]
_DEPRECATED_STATE_ALARM_ARMED_CUSTOM_BYPASS: Final[Incomplete]
_DEPRECATED_STATE_ALARM_PENDING: Final[Incomplete]
_DEPRECATED_STATE_ALARM_ARMING: Final[Incomplete]
_DEPRECATED_STATE_ALARM_DISARMING: Final[Incomplete]
_DEPRECATED_STATE_ALARM_TRIGGERED: Final[Incomplete]
ATTR_ATTRIBUTION: Final[str]
ATTR_CREDENTIALS: Final[str]
ATTR_NOW: Final[str]
ATTR_DATE: Final[str]
ATTR_TIME: Final[str]
ATTR_SECONDS: Final[str]
ATTR_DOMAIN: Final[str]
ATTR_SERVICE: Final[str]
ATTR_SERVICE_DATA: Final[str]
ATTR_ID: Final[str]
ATTR_NAME: Final[str]
ATTR_ENTITY_ID: Final[str]
ATTR_AREA_ID: Final[str]
ATTR_DEVICE_ID: Final[str]
ATTR_FLOOR_ID: Final[str]
ATTR_LABEL_ID: Final[str]
ATTR_FRIENDLY_NAME: Final[str]
ATTR_ENTITY_PICTURE: Final[str]
ATTR_IDENTIFIERS: Final[str]
ATTR_ICON: Final[str]
ATTR_UNIT_OF_MEASUREMENT: Final[str]
CONF_UNIT_SYSTEM_METRIC: Final[str]
CONF_UNIT_SYSTEM_IMPERIAL: Final[str]
ATTR_VOLTAGE: Final[str]
ATTR_LOCATION: Final[str]
ATTR_MODE: Final[str]
ATTR_CONFIGURATION_URL: Final[str]
ATTR_CONNECTIONS: Final[str]
ATTR_DEFAULT_NAME: Final[str]
ATTR_MANUFACTURER: Final[str]
ATTR_MODEL: Final[str]
ATTR_MODEL_ID: Final[str]
ATTR_SERIAL_NUMBER: Final[str]
ATTR_SUGGESTED_AREA: Final[str]
ATTR_SW_VERSION: Final[str]
ATTR_HW_VERSION: Final[str]
ATTR_VIA_DEVICE: Final[str]
ATTR_BATTERY_CHARGING: Final[str]
ATTR_BATTERY_LEVEL: Final[str]
ATTR_WAKEUP: Final[str]
ATTR_CODE: Final[str]
ATTR_CODE_FORMAT: Final[str]
ATTR_COMMAND: Final[str]
ATTR_ARMED: Final[str]
ATTR_LOCKED: Final[str]
ATTR_TRIPPED: Final[str]
ATTR_LAST_TRIP_TIME: Final[str]
ATTR_HIDDEN: Final[str]
ATTR_LATITUDE: Final[str]
ATTR_LONGITUDE: Final[str]
ATTR_ELEVATION: Final[str]
ATTR_GPS_ACCURACY: Final[str]
ATTR_ASSUMED_STATE: Final[str]
ATTR_STATE: Final[str]
ATTR_EDITABLE: Final[str]
ATTR_OPTION: Final[str]
ATTR_RESTORED: Final[str]
ATTR_SUPPORTED_FEATURES: Final[str]
ATTR_DEVICE_CLASS: Final[str]
ATTR_TEMPERATURE: Final[str]
ATTR_PERSONS: Final[str]

class UnitOfApparentPower(StrEnum):
    VOLT_AMPERE = 'VA'

class UnitOfPower(StrEnum):
    MILLIWATT = 'mW'
    WATT = 'W'
    KILO_WATT = 'kW'
    MEGA_WATT = 'MW'
    GIGA_WATT = 'GW'
    TERA_WATT = 'TW'
    BTU_PER_HOUR = 'BTU/h'

class UnitOfReactivePower(StrEnum):
    VOLT_AMPERE_REACTIVE = 'var'

_DEPRECATED_POWER_VOLT_AMPERE_REACTIVE: Final[Incomplete]

class UnitOfEnergy(StrEnum):
    JOULE = 'J'
    KILO_JOULE = 'kJ'
    MEGA_JOULE = 'MJ'
    GIGA_JOULE = 'GJ'
    MILLIWATT_HOUR = 'mWh'
    WATT_HOUR = 'Wh'
    KILO_WATT_HOUR = 'kWh'
    MEGA_WATT_HOUR = 'MWh'
    GIGA_WATT_HOUR = 'GWh'
    TERA_WATT_HOUR = 'TWh'
    CALORIE = 'cal'
    KILO_CALORIE = 'kcal'
    MEGA_CALORIE = 'Mcal'
    GIGA_CALORIE = 'Gcal'

class UnitOfElectricCurrent(StrEnum):
    MILLIAMPERE = 'mA'
    AMPERE = 'A'

class UnitOfElectricPotential(StrEnum):
    MICROVOLT = 'µV'
    MILLIVOLT = 'mV'
    VOLT = 'V'

DEGREE: Final[str]
CURRENCY_EURO: Final[str]
CURRENCY_DOLLAR: Final[str]
CURRENCY_CENT: Final[str]

class UnitOfTemperature(StrEnum):
    CELSIUS = '°C'
    FAHRENHEIT = '°F'
    KELVIN = 'K'

class UnitOfTime(StrEnum):
    MICROSECONDS = 'μs'
    MILLISECONDS = 'ms'
    SECONDS = 's'
    MINUTES = 'min'
    HOURS = 'h'
    DAYS = 'd'
    WEEKS = 'w'
    MONTHS = 'm'
    YEARS = 'y'

class UnitOfLength(StrEnum):
    MILLIMETERS = 'mm'
    CENTIMETERS = 'cm'
    METERS = 'm'
    KILOMETERS = 'km'
    INCHES = 'in'
    FEET = 'ft'
    YARDS = 'yd'
    MILES = 'mi'
    NAUTICAL_MILES = 'nmi'

class UnitOfFrequency(StrEnum):
    HERTZ = 'Hz'
    KILOHERTZ = 'kHz'
    MEGAHERTZ = 'MHz'
    GIGAHERTZ = 'GHz'

class UnitOfPressure(StrEnum):
    PA = 'Pa'
    HPA = 'hPa'
    KPA = 'kPa'
    BAR = 'bar'
    CBAR = 'cbar'
    MBAR = 'mbar'
    MMHG = 'mmHg'
    INHG = 'inHg'
    PSI = 'psi'

class UnitOfSoundPressure(StrEnum):
    DECIBEL = 'dB'
    WEIGHTED_DECIBEL_A = 'dBA'

class UnitOfVolume(StrEnum):
    CUBIC_FEET = 'ft³'
    CENTUM_CUBIC_FEET = 'CCF'
    CUBIC_METERS = 'm³'
    LITERS = 'L'
    MILLILITERS = 'mL'
    GALLONS = 'gal'
    FLUID_OUNCES = 'fl. oz.'

class UnitOfVolumeFlowRate(StrEnum):
    CUBIC_METERS_PER_HOUR = 'm³/h'
    CUBIC_FEET_PER_MINUTE = 'ft³/min'
    LITERS_PER_MINUTE = 'L/min'
    GALLONS_PER_MINUTE = 'gal/min'
    MILLILITERS_PER_SECOND = 'mL/s'

class UnitOfArea(StrEnum):
    SQUARE_METERS = 'm²'
    SQUARE_CENTIMETERS = 'cm²'
    SQUARE_KILOMETERS = 'km²'
    SQUARE_MILLIMETERS = 'mm²'
    SQUARE_INCHES = 'in²'
    SQUARE_FEET = 'ft²'
    SQUARE_YARDS = 'yd²'
    SQUARE_MILES = 'mi²'
    ACRES = 'ac'
    HECTARES = 'ha'

_DEPRECATED_AREA_SQUARE_METERS: Final[Incomplete]

class UnitOfMass(StrEnum):
    GRAMS = 'g'
    KILOGRAMS = 'kg'
    MILLIGRAMS = 'mg'
    MICROGRAMS = 'µg'
    OUNCES = 'oz'
    POUNDS = 'lb'
    STONES = 'st'

class UnitOfConductivity(StrEnum, deprecated={'SIEMENS': ('UnitOfConductivity.SIEMENS_PER_CM', '2025.11.0'), 'MICROSIEMENS': ('UnitOfConductivity.MICROSIEMENS_PER_CM', '2025.11.0'), 'MILLISIEMENS': ('UnitOfConductivity.MILLISIEMENS_PER_CM', '2025.11.0')}, metaclass=EnumWithDeprecatedMembers):
    SIEMENS_PER_CM = 'S/cm'
    MICROSIEMENS_PER_CM = 'µS/cm'
    MILLISIEMENS_PER_CM = 'mS/cm'
    SIEMENS = 'S/cm'
    MICROSIEMENS = 'µS/cm'
    MILLISIEMENS = 'mS/cm'

_DEPRECATED_CONDUCTIVITY: Final[Incomplete]
LIGHT_LUX: Final[str]
UV_INDEX: Final[str]
PERCENTAGE: Final[str]
REVOLUTIONS_PER_MINUTE: Final[str]

class UnitOfIrradiance(StrEnum):
    WATTS_PER_SQUARE_METER = 'W/m²'
    BTUS_PER_HOUR_SQUARE_FOOT = 'BTU/(h⋅ft²)'

class UnitOfVolumetricFlux(StrEnum):
    INCHES_PER_DAY = 'in/d'
    INCHES_PER_HOUR = 'in/h'
    MILLIMETERS_PER_DAY = 'mm/d'
    MILLIMETERS_PER_HOUR = 'mm/h'

class UnitOfPrecipitationDepth(StrEnum):
    INCHES = 'in'
    MILLIMETERS = 'mm'
    CENTIMETERS = 'cm'

CONCENTRATION_MICROGRAMS_PER_CUBIC_METER: Final[str]
CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER: Final[str]
CONCENTRATION_MICROGRAMS_PER_CUBIC_FOOT: Final[str]
CONCENTRATION_PARTS_PER_CUBIC_METER: Final[str]
CONCENTRATION_PARTS_PER_MILLION: Final[str]
CONCENTRATION_PARTS_PER_BILLION: Final[str]

class UnitOfBloodGlucoseConcentration(StrEnum):
    MILLIGRAMS_PER_DECILITER = 'mg/dL'
    MILLIMOLE_PER_LITER = 'mmol/L'

class UnitOfSpeed(StrEnum):
    BEAUFORT = 'Beaufort'
    FEET_PER_SECOND = 'ft/s'
    INCHES_PER_SECOND = 'in/s'
    METERS_PER_SECOND = 'm/s'
    KILOMETERS_PER_HOUR = 'km/h'
    KNOTS = 'kn'
    MILES_PER_HOUR = 'mph'
    MILLIMETERS_PER_SECOND = 'mm/s'

SIGNAL_STRENGTH_DECIBELS: Final[str]
SIGNAL_STRENGTH_DECIBELS_MILLIWATT: Final[str]

class UnitOfInformation(StrEnum):
    BITS = 'bit'
    KILOBITS = 'kbit'
    MEGABITS = 'Mbit'
    GIGABITS = 'Gbit'
    BYTES = 'B'
    KILOBYTES = 'kB'
    MEGABYTES = 'MB'
    GIGABYTES = 'GB'
    TERABYTES = 'TB'
    PETABYTES = 'PB'
    EXABYTES = 'EB'
    ZETTABYTES = 'ZB'
    YOTTABYTES = 'YB'
    KIBIBYTES = 'KiB'
    MEBIBYTES = 'MiB'
    GIBIBYTES = 'GiB'
    TEBIBYTES = 'TiB'
    PEBIBYTES = 'PiB'
    EXBIBYTES = 'EiB'
    ZEBIBYTES = 'ZiB'
    YOBIBYTES = 'YiB'

class UnitOfDataRate(StrEnum):
    BITS_PER_SECOND = 'bit/s'
    KILOBITS_PER_SECOND = 'kbit/s'
    MEGABITS_PER_SECOND = 'Mbit/s'
    GIGABITS_PER_SECOND = 'Gbit/s'
    BYTES_PER_SECOND = 'B/s'
    KILOBYTES_PER_SECOND = 'kB/s'
    MEGABYTES_PER_SECOND = 'MB/s'
    GIGABYTES_PER_SECOND = 'GB/s'
    KIBIBYTES_PER_SECOND = 'KiB/s'
    MEBIBYTES_PER_SECOND = 'MiB/s'
    GIBIBYTES_PER_SECOND = 'GiB/s'

COMPRESSED_STATE_STATE: Final[str]
COMPRESSED_STATE_ATTRIBUTES: Final[str]
COMPRESSED_STATE_CONTEXT: Final[str]
COMPRESSED_STATE_LAST_CHANGED: Final[str]
COMPRESSED_STATE_LAST_UPDATED: Final[str]
SERVICE_TURN_ON: Final[str]
SERVICE_TURN_OFF: Final[str]
SERVICE_TOGGLE: Final[str]
SERVICE_RELOAD: Final[str]
SERVICE_VOLUME_UP: Final[str]
SERVICE_VOLUME_DOWN: Final[str]
SERVICE_VOLUME_MUTE: Final[str]
SERVICE_VOLUME_SET: Final[str]
SERVICE_MEDIA_PLAY_PAUSE: Final[str]
SERVICE_MEDIA_PLAY: Final[str]
SERVICE_MEDIA_PAUSE: Final[str]
SERVICE_MEDIA_STOP: Final[str]
SERVICE_MEDIA_NEXT_TRACK: Final[str]
SERVICE_MEDIA_PREVIOUS_TRACK: Final[str]
SERVICE_MEDIA_SEEK: Final[str]
SERVICE_REPEAT_SET: Final[str]
SERVICE_SHUFFLE_SET: Final[str]
SERVICE_ALARM_DISARM: Final[str]
SERVICE_ALARM_ARM_HOME: Final[str]
SERVICE_ALARM_ARM_AWAY: Final[str]
SERVICE_ALARM_ARM_NIGHT: Final[str]
SERVICE_ALARM_ARM_VACATION: Final[str]
SERVICE_ALARM_ARM_CUSTOM_BYPASS: Final[str]
SERVICE_ALARM_TRIGGER: Final[str]
SERVICE_LOCK: Final[str]
SERVICE_UNLOCK: Final[str]
SERVICE_OPEN: Final[str]
SERVICE_CLOSE: Final[str]
SERVICE_CLOSE_COVER: Final[str]
SERVICE_CLOSE_COVER_TILT: Final[str]
SERVICE_OPEN_COVER: Final[str]
SERVICE_OPEN_COVER_TILT: Final[str]
SERVICE_SAVE_PERSISTENT_STATES: Final[str]
SERVICE_SET_COVER_POSITION: Final[str]
SERVICE_SET_COVER_TILT_POSITION: Final[str]
SERVICE_STOP_COVER: Final[str]
SERVICE_STOP_COVER_TILT: Final[str]
SERVICE_TOGGLE_COVER_TILT: Final[str]
SERVICE_CLOSE_VALVE: Final[str]
SERVICE_OPEN_VALVE: Final[str]
SERVICE_SET_VALVE_POSITION: Final[str]
SERVICE_STOP_VALVE: Final[str]
SERVICE_SELECT_OPTION: Final[str]
SERVER_PORT: Final[int]
URL_ROOT: Final[str]
URL_API: Final[str]
URL_API_STREAM: Final[str]
URL_API_CORE_STATE: Final[str]
URL_API_CONFIG: Final[str]
URL_API_STATES: Final[str]
URL_API_STATES_ENTITY: Final[str]
URL_API_EVENTS: Final[str]
URL_API_EVENTS_EVENT: Final[str]
URL_API_SERVICES: Final[str]
URL_API_SERVICES_SERVICE: Final[str]
URL_API_COMPONENTS: Final[str]
URL_API_ERROR_LOG: Final[str]
URL_API_LOG_OUT: Final[str]
URL_API_TEMPLATE: Final[str]
HTTP_BASIC_AUTHENTICATION: Final[str]
HTTP_BEARER_AUTHENTICATION: Final[str]
HTTP_DIGEST_AUTHENTICATION: Final[str]
HTTP_HEADER_X_REQUESTED_WITH: Final[str]
CONTENT_TYPE_JSON: Final[str]
CONTENT_TYPE_MULTIPART: Final[str]
CONTENT_TYPE_TEXT_PLAIN: Final[str]
RESTART_EXIT_CODE: Final[int]
UNIT_NOT_RECOGNIZED_TEMPLATE: Final[str]
LENGTH: Final[str]
AREA: Final[str]
MASS: Final[str]
PRESSURE: Final[str]
VOLUME: Final[str]
TEMPERATURE: Final[str]
SPEED: Final[str]
WIND_SPEED: Final[str]
ILLUMINANCE: Final[str]
ACCUMULATED_PRECIPITATION: Final[str]
WEEKDAYS: Final[list[str]]
PRECISION_WHOLE: Final[int]
PRECISION_HALVES: Final[float]
PRECISION_TENTHS: Final[float]
CLOUD_NEVER_EXPOSED_ENTITIES: Final[list[str]]

class EntityCategory(StrEnum):
    CONFIG = 'config'
    DIAGNOSTIC = 'diagnostic'

ENTITY_CATEGORIES: Final[list[str]]
CAST_APP_ID_HOMEASSISTANT_MEDIA: Final[str]
CAST_APP_ID_HOMEASSISTANT_LOVELACE: Final[str]
HASSIO_USER_NAME: str
SIGNAL_BOOTSTRAP_INTEGRATIONS: SignalType[dict[str, float]]
KEY_DATA_LOGGING: HassKey[str]
FORMAT_DATE: Final[str]
FORMAT_TIME: Final[str]
FORMAT_DATETIME: Final[Incomplete]
MAX_EXPECTED_ENTITY_IDS: Final[int]
__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
