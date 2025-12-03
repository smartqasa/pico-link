from .const import CONF_ARRIVAL_TIME as CONF_ARRIVAL_TIME, CONF_DEPARTURE_TIME as CONF_DEPARTURE_TIME, CONF_DESTINATION_ENTITY_ID as CONF_DESTINATION_ENTITY_ID, CONF_DESTINATION_LATITUDE as CONF_DESTINATION_LATITUDE, CONF_DESTINATION_LONGITUDE as CONF_DESTINATION_LONGITUDE, CONF_ORIGIN_ENTITY_ID as CONF_ORIGIN_ENTITY_ID, CONF_ORIGIN_LATITUDE as CONF_ORIGIN_LATITUDE, CONF_ORIGIN_LONGITUDE as CONF_ORIGIN_LONGITUDE, CONF_ROUTE_MODE as CONF_ROUTE_MODE, DOMAIN as DOMAIN, TRAVEL_MODE_PUBLIC as TRAVEL_MODE_PUBLIC
from .coordinator import HERERoutingDataUpdateCoordinator as HERERoutingDataUpdateCoordinator, HERETransitDataUpdateCoordinator as HERETransitDataUpdateCoordinator
from .model import HERETravelTimeConfig as HERETravelTimeConfig
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_MODE as CONF_MODE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.start import async_at_started as async_at_started

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
