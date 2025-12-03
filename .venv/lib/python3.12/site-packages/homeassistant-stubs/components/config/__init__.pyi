from . import area_registry as area_registry, auth as auth, auth_provider_homeassistant as auth_provider_homeassistant, automation as automation, category_registry as category_registry, config_entries as config_entries, core as core, device_registry as device_registry, entity_registry as entity_registry, floor_registry as floor_registry, label_registry as label_registry, scene as scene, script as script
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components import frontend as frontend
from homeassistant.const import EVENT_COMPONENT_LOADED as EVENT_COMPONENT_LOADED
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.setup import EventComponentLoaded as EventComponentLoaded

SECTIONS: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
