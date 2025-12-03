from . import ApSystemsConfigEntry as ApSystemsConfigEntry, ApSystemsData as ApSystemsData
from .entity import ApSystemsEntity as ApSystemsEntity
from _typeshed import Incomplete
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberMode as NumberMode
from homeassistant.const import UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType

async def async_setup_entry(hass: HomeAssistant, config_entry: ApSystemsConfigEntry, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class ApSystemsMaxOutputNumber(ApSystemsEntity, NumberEntity):
    _attr_native_step: int
    _attr_device_class: Incomplete
    _attr_mode: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_translation_key: str
    _api: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_max_value: Incomplete
    _attr_native_min_value: Incomplete
    def __init__(self, data: ApSystemsData) -> None: ...
    _attr_available: bool
    _attr_native_value: Incomplete
    async def async_update(self) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
