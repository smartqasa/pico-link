from .entity import MatterEntity as MatterEntity
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from chip.clusters import Objects as clusters
from homeassistant.components.valve import ValveDeviceClass as ValveDeviceClass, ValveEntity as ValveEntity, ValveEntityDescription as ValveEntityDescription, ValveEntityFeature as ValveEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

ValveConfigurationAndControl: Incomplete
ValveStateEnum: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MatterValve(MatterEntity, ValveEntity):
    _feature_map: int | None
    entity_description: ValveEntityDescription
    _platform_translation_key: str
    async def send_device_command(self, command: clusters.ClusterCommand) -> None: ...
    async def async_open_valve(self) -> None: ...
    async def async_close_valve(self) -> None: ...
    async def async_set_valve_position(self, position: int) -> None: ...
    _attr_is_opening: bool
    _attr_is_closing: bool
    _attr_is_closed: bool
    _attr_current_valve_position: Incomplete
    @callback
    def _update_from_device(self) -> None: ...
    _attr_supported_features: Incomplete
    _attr_reports_position: bool
    @callback
    def _calculate_features(self) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
