from .entity import DeconzDevice as DeconzDevice
from .hub import DeconzHub as DeconzHub
from _typeshed import Incomplete
from homeassistant.components.select import DOMAIN as SELECT_DOMAIN, SelectEntity as SelectEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydeconz.models.event import EventType as EventType
from pydeconz.models.sensor.air_purifier import AirPurifier
from pydeconz.models.sensor.presence import Presence

SENSITIVITY_TO_DECONZ: Incomplete
DECONZ_TO_SENSITIVITY: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzAirPurifierFanMode(DeconzDevice[AirPurifier], SelectEntity):
    _name_suffix: str
    unique_id_suffix: str
    _update_key: str
    _attr_entity_category: Incomplete
    _attr_options: Incomplete
    TYPE = SELECT_DOMAIN
    @property
    def current_option(self) -> str: ...
    async def async_select_option(self, option: str) -> None: ...

class DeconzPresenceDeviceModeSelect(DeconzDevice[Presence], SelectEntity):
    _name_suffix: str
    unique_id_suffix: str
    _update_key: str
    _attr_entity_category: Incomplete
    _attr_options: Incomplete
    TYPE = SELECT_DOMAIN
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...

class DeconzPresenceSensitivitySelect(DeconzDevice[Presence], SelectEntity):
    _name_suffix: str
    unique_id_suffix: str
    _update_key: str
    _attr_entity_category: Incomplete
    _attr_options: Incomplete
    TYPE = SELECT_DOMAIN
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...

class DeconzPresenceTriggerDistanceSelect(DeconzDevice[Presence], SelectEntity):
    _name_suffix: str
    unique_id_suffix: str
    _update_key: str
    _attr_entity_category: Incomplete
    _attr_options: Incomplete
    TYPE = SELECT_DOMAIN
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
