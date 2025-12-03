from .const import CONF_CANDLE_LIGHT_MINUTES as CONF_CANDLE_LIGHT_MINUTES, CONF_DIASPORA as CONF_DIASPORA, CONF_HAVDALAH_OFFSET_MINUTES as CONF_HAVDALAH_OFFSET_MINUTES, DEFAULT_CANDLE_LIGHT as DEFAULT_CANDLE_LIGHT, DEFAULT_DIASPORA as DEFAULT_DIASPORA, DEFAULT_HAVDALAH_OFFSET_MINUTES as DEFAULT_HAVDALAH_OFFSET_MINUTES, DEFAULT_LANGUAGE as DEFAULT_LANGUAGE
from .entity import JewishCalendarConfigEntry as JewishCalendarConfigEntry, JewishCalendarData as JewishCalendarData
from homeassistant.const import CONF_ELEVATION as CONF_ELEVATION, CONF_LANGUAGE as CONF_LANGUAGE, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_TIME_ZONE as CONF_TIME_ZONE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, config_entry: JewishCalendarConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: JewishCalendarConfigEntry) -> bool: ...
