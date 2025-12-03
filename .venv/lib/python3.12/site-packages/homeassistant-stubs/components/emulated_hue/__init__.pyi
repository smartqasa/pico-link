from .config import CONF_ADVERTISE_IP as CONF_ADVERTISE_IP, CONF_ADVERTISE_PORT as CONF_ADVERTISE_PORT, CONF_ENTITY_HIDDEN as CONF_ENTITY_HIDDEN, CONF_ENTITY_NAME as CONF_ENTITY_NAME, CONF_EXPOSED_DOMAINS as CONF_EXPOSED_DOMAINS, CONF_EXPOSE_BY_DEFAULT as CONF_EXPOSE_BY_DEFAULT, CONF_HOST_IP as CONF_HOST_IP, CONF_LIGHTS_ALL_DIMMABLE as CONF_LIGHTS_ALL_DIMMABLE, CONF_LISTEN_PORT as CONF_LISTEN_PORT, CONF_OFF_MAPS_TO_ON_DOMAINS as CONF_OFF_MAPS_TO_ON_DOMAINS, CONF_UPNP_BIND_MULTICAST as CONF_UPNP_BIND_MULTICAST, Config as Config, DEFAULT_LIGHTS_ALL_DIMMABLE as DEFAULT_LIGHTS_ALL_DIMMABLE, DEFAULT_LISTEN_PORT as DEFAULT_LISTEN_PORT, DEFAULT_TYPE as DEFAULT_TYPE, TYPE_ALEXA as TYPE_ALEXA, TYPE_GOOGLE as TYPE_GOOGLE
from .const import DOMAIN as DOMAIN
from .hue_api import HueAllGroupsStateView as HueAllGroupsStateView, HueAllLightsStateView as HueAllLightsStateView, HueConfigView as HueConfigView, HueFullStateView as HueFullStateView, HueGroupView as HueGroupView, HueOneLightChangeView as HueOneLightChangeView, HueOneLightStateView as HueOneLightStateView, HueUnauthorizedUser as HueUnauthorizedUser, HueUsernameView as HueUsernameView
from .upnp import DescriptionXmlView as DescriptionXmlView, async_create_upnp_datagram_endpoint as async_create_upnp_datagram_endpoint
from _typeshed import Incomplete
from aiohttp import web
from homeassistant.components.http import KEY_HASS as KEY_HASS
from homeassistant.components.network import async_get_source_ip as async_get_source_ip
from homeassistant.const import CONF_ENTITIES as CONF_ENTITIES, CONF_TYPE as CONF_TYPE, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONFIG_ENTITY_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

async def start_emulated_hue_bridge(hass: HomeAssistant, config: Config, app: web.Application) -> None: ...
async def async_setup(hass: HomeAssistant, yaml_config: ConfigType) -> bool: ...
