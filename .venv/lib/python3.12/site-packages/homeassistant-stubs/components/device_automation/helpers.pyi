import voluptuous as vol
from . import DeviceAutomationType as DeviceAutomationType, async_get_device_automation_platform as async_get_device_automation_platform
from .exceptions import InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from _typeshed import Incomplete
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType

DYNAMIC_VALIDATOR: Incomplete
STATIC_VALIDATOR: Incomplete
ENTITY_PLATFORMS: Incomplete

async def async_validate_device_automation_config(hass: HomeAssistant, config: ConfigType, automation_schema: vol.Schema, automation_type: DeviceAutomationType) -> ConfigType: ...
