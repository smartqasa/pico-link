from . import MastodonConfigEntry as MastodonConfigEntry
from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, INSTANCE_VERSION as INSTANCE_VERSION
from .coordinator import MastodonCoordinator as MastodonCoordinator
from .utils import construct_mastodon_username as construct_mastodon_username
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class MastodonEntity(CoordinatorEntity[MastodonCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: MastodonCoordinator, entity_description: EntityDescription, data: MastodonConfigEntry) -> None: ...
