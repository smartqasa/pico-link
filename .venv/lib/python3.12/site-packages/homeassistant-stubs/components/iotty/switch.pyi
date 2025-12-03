from . import IottyConfigEntry as IottyConfigEntry
from .api import IottyProxy as IottyProxy
from .coordinator import IottyDataUpdateCoordinator as IottyDataUpdateCoordinator
from .entity import IottyEntity as IottyEntity
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from iottycloud.lightswitch import LightSwitch
from iottycloud.outlet import Outlet
from typing import Any

_LOGGER: Incomplete
ENTITIES: dict[str, SwitchEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: IottyConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IottySwitch(IottyEntity, SwitchEntity):
    _attr_device_class: SwitchDeviceClass | None
    _iotty_device: LightSwitch | Outlet
    entity_description: Incomplete
    def __init__(self, coordinator: IottyDataUpdateCoordinator, iotty_cloud: IottyProxy, iotty_device: LightSwitch | Outlet, entity_description: SwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
