from .const import DOMAIN as DOMAIN
from .entity import EsphomeAssistEntity as EsphomeAssistEntity, EsphomeEntity as EsphomeEntity, platform_async_setup_entry as platform_async_setup_entry
from .entry_data import ESPHomeConfigEntry as ESPHomeConfigEntry
from _typeshed import Incomplete
from aioesphomeapi import BinarySensorInfo, BinarySensorState, EntityInfo as EntityInfo
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.enum import try_parse_enum as try_parse_enum

async def async_setup_entry(hass: HomeAssistant, entry: ESPHomeConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EsphomeBinarySensor(EsphomeEntity[BinarySensorInfo, BinarySensorState], BinarySensorEntity):
    @property
    def is_on(self) -> bool | None: ...
    _attr_device_class: Incomplete
    @callback
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @property
    def available(self) -> bool: ...

class EsphomeAssistInProgressBinarySensor(EsphomeAssistEntity, BinarySensorEntity):
    entity_description: Incomplete
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
