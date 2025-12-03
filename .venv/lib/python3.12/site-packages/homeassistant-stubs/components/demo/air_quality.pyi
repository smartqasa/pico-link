from _typeshed import Incomplete
from homeassistant.components.air_quality import AirQualityEntity as AirQualityEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DemoAirQuality(AirQualityEntity):
    _attr_attribution: str
    _attr_should_poll: bool
    _attr_name: Incomplete
    _pm_2_5: Incomplete
    _pm_10: Incomplete
    _n2o: Incomplete
    def __init__(self, name: str, pm_2_5: int, pm_10: int, n2o: int | None) -> None: ...
    @property
    def particulate_matter_2_5(self) -> int: ...
    @property
    def particulate_matter_10(self) -> int: ...
    @property
    def nitrogen_oxide(self) -> int | None: ...
