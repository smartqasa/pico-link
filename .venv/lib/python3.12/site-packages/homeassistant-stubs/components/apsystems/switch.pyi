from . import ApSystemsConfigEntry as ApSystemsConfigEntry, ApSystemsData as ApSystemsData
from .entity import ApSystemsEntity as ApSystemsEntity
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ApSystemsConfigEntry, add_entities: AddEntitiesCallback) -> None: ...

class ApSystemsInverterSwitch(ApSystemsEntity, SwitchEntity):
    _attr_device_class: Incomplete
    _attr_translation_key: str
    _api: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, data: ApSystemsData) -> None: ...
    _attr_available: bool
    _attr_is_on: Incomplete
    async def async_update(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
