from .entity import Group as Group
from .registry import GroupIntegrationRegistry as GroupIntegrationRegistry
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey

CONF_HIDE_MEMBERS: str
CONF_IGNORE_NON_NUMERIC: str
DOMAIN: str
DATA_COMPONENT: HassKey[EntityComponent[Group]]
REG_KEY: HassKey[GroupIntegrationRegistry]
GROUP_ORDER: HassKey[int]
ATTR_ADD_ENTITIES: str
ATTR_REMOVE_ENTITIES: str
ATTR_AUTO: str
ATTR_ENTITIES: str
ATTR_OBJECT_ID: str
ATTR_ORDER: str
ATTR_ALL: str
