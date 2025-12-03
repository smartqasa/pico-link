from . import AdGuardConfigEntry as AdGuardConfigEntry, AdGuardData as AdGuardData
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import SOURCE_HASSIO as SOURCE_HASSIO
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity

class AdGuardHomeEntity(Entity):
    _attr_has_entity_name: bool
    _attr_available: bool
    _entry: Incomplete
    data: Incomplete
    adguard: Incomplete
    def __init__(self, data: AdGuardData, entry: AdGuardConfigEntry) -> None: ...
    async def async_update(self) -> None: ...
    async def _adguard_update(self) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
