from .. import OverkizDataConfigEntry as OverkizDataConfigEntry
from .awning import Awning as Awning
from .generic_cover import OverkizGenericCover as OverkizGenericCover
from .vertical_cover import LowSpeedCover as LowSpeedCover, VerticalCover as VerticalCover
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: OverkizDataConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
