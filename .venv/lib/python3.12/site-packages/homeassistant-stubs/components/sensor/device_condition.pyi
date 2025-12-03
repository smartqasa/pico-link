import voluptuous as vol
from . import ATTR_STATE_CLASS as ATTR_STATE_CLASS, DOMAIN as DOMAIN, SensorDeviceClass as SensorDeviceClass
from _typeshed import Incomplete
from homeassistant.components.device_automation import InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig, async_get_entity_registry_entry_or_raise as async_get_entity_registry_entry_or_raise
from homeassistant.const import CONF_ABOVE as CONF_ABOVE, CONF_BELOW as CONF_BELOW, CONF_CONDITION as CONF_CONDITION, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import condition as condition
from homeassistant.helpers.entity import get_capability as get_capability, get_device_class as get_device_class, get_unit_of_measurement as get_unit_of_measurement
from homeassistant.helpers.typing import ConfigType as ConfigType

DEVICE_CLASS_NONE: str
CONF_IS_APPARENT_POWER: str
CONF_IS_AQI: str
CONF_IS_AREA: str
CONF_IS_ATMOSPHERIC_PRESSURE: str
CONF_IS_BATTERY_LEVEL: str
CONF_IS_BLOOD_GLUCOSE_CONCENTRATION: str
CONF_IS_CO: str
CONF_IS_CO2: str
CONF_IS_CONDUCTIVITY: str
CONF_IS_CURRENT: str
CONF_IS_DATA_RATE: str
CONF_IS_DATA_SIZE: str
CONF_IS_DISTANCE: str
CONF_IS_DURATION: str
CONF_IS_ENERGY: str
CONF_IS_FREQUENCY: str
CONF_IS_HUMIDITY: str
CONF_IS_GAS: str
CONF_IS_ILLUMINANCE: str
CONF_IS_IRRADIANCE: str
CONF_IS_MOISTURE: str
CONF_IS_MONETARY: str
CONF_IS_NITROGEN_DIOXIDE: str
CONF_IS_NITROGEN_MONOXIDE: str
CONF_IS_NITROUS_OXIDE: str
CONF_IS_OZONE: str
CONF_IS_PH: str
CONF_IS_PM1: str
CONF_IS_PM10: str
CONF_IS_PM25: str
CONF_IS_POWER: str
CONF_IS_POWER_FACTOR: str
CONF_IS_PRECIPITATION: str
CONF_IS_PRECIPITATION_INTENSITY: str
CONF_IS_PRESSURE: str
CONF_IS_SPEED: str
CONF_IS_REACTIVE_POWER: str
CONF_IS_SIGNAL_STRENGTH: str
CONF_IS_SOUND_PRESSURE: str
CONF_IS_SULPHUR_DIOXIDE: str
CONF_IS_TEMPERATURE: str
CONF_IS_VALUE: str
CONF_IS_VOLATILE_ORGANIC_COMPOUNDS: str
CONF_IS_VOLATILE_ORGANIC_COMPOUNDS_PARTS: str
CONF_IS_VOLTAGE: str
CONF_IS_VOLUME: str
CONF_IS_VOLUME_FLOW_RATE: str
CONF_IS_WATER: str
CONF_IS_WEIGHT: str
CONF_IS_WIND_SPEED: str
ENTITY_CONDITIONS: Incomplete
CONDITION_SCHEMA: Incomplete

async def async_get_conditions(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
@callback
def async_condition_from_config(hass: HomeAssistant, config: ConfigType) -> condition.ConditionCheckerType: ...
async def async_get_condition_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
