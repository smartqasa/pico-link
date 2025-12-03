from .entity import BaseToggleEntity as BaseToggleEntity
from _typeshed import Incomplete
from homeassistant.components.siren import SirenEntity as SirenEntity, SirenEntityFeature as SirenEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SirenSwitch(BaseToggleEntity, SirenEntity):
    _attr_supported_features: Incomplete
