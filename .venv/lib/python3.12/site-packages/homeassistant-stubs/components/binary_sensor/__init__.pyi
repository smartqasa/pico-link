from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey
from propcache import cached_property
from typing import Literal, final

_LOGGER: Incomplete
DOMAIN: str
DATA_COMPONENT: HassKey[EntityComponent[BinarySensorEntity]]
ENTITY_ID_FORMAT: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete

class BinarySensorDeviceClass(StrEnum):
    BATTERY = 'battery'
    BATTERY_CHARGING = 'battery_charging'
    CO = 'carbon_monoxide'
    COLD = 'cold'
    CONNECTIVITY = 'connectivity'
    DOOR = 'door'
    GARAGE_DOOR = 'garage_door'
    GAS = 'gas'
    HEAT = 'heat'
    LIGHT = 'light'
    LOCK = 'lock'
    MOISTURE = 'moisture'
    MOTION = 'motion'
    MOVING = 'moving'
    OCCUPANCY = 'occupancy'
    OPENING = 'opening'
    PLUG = 'plug'
    POWER = 'power'
    PRESENCE = 'presence'
    PROBLEM = 'problem'
    RUNNING = 'running'
    SAFETY = 'safety'
    SMOKE = 'smoke'
    SOUND = 'sound'
    TAMPER = 'tamper'
    UPDATE = 'update'
    VIBRATION = 'vibration'
    WINDOW = 'window'

DEVICE_CLASSES_SCHEMA: Incomplete
DEVICE_CLASSES: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class BinarySensorEntityDescription(EntityDescription, frozen_or_thawed=True):
    device_class: BinarySensorDeviceClass | None = ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class BinarySensorEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: BinarySensorEntityDescription
    _attr_device_class: BinarySensorDeviceClass | None
    _attr_is_on: bool | None
    _attr_state: None
    async def async_internal_added_to_hass(self) -> None: ...
    def _default_to_device_class_name(self) -> bool: ...
    @cached_property
    def device_class(self) -> BinarySensorDeviceClass | None: ...
    @cached_property
    def is_on(self) -> bool | None: ...
    @final
    @property
    def state(self) -> Literal['on', 'off'] | None: ...
