from . import MyUplinkConfigEntry as MyUplinkConfigEntry, MyUplinkDataCoordinator as MyUplinkDataCoordinator
from .entity import MyUplinkEntity as MyUplinkEntity
from _typeshed import Incomplete
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

UPDATE_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: MyUplinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MyUplinkDeviceUpdate(MyUplinkEntity, UpdateEntity):
    entity_description: Incomplete
    def __init__(self, coordinator: MyUplinkDataCoordinator, device_id: str, entity_description: UpdateEntityDescription, unique_id_suffix: str) -> None: ...
    @property
    def installed_version(self) -> str | None: ...
    @property
    def latest_version(self) -> str | None: ...
