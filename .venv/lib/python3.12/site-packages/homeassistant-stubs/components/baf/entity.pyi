from _typeshed import Incomplete
from aiobafi6 import Device as Device
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo, format_mac as format_mac
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription

class BAFEntity(Entity):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    _device: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, device: Device) -> None: ...
    _attr_available: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
    @callback
    def _async_update_from_device(self, device: Device) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...

class BAFDescriptionEntity(BAFEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device: Device, description: EntityDescription) -> None: ...
