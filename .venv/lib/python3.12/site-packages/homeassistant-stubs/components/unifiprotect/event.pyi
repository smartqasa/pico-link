import dataclasses
from . import Bootstrap as Bootstrap
from .const import ATTR_EVENT_ID as ATTR_EVENT_ID, EVENT_TYPE_DOORBELL_RING as EVENT_TYPE_DOORBELL_RING, EVENT_TYPE_FINGERPRINT_IDENTIFIED as EVENT_TYPE_FINGERPRINT_IDENTIFIED, EVENT_TYPE_FINGERPRINT_NOT_IDENTIFIED as EVENT_TYPE_FINGERPRINT_NOT_IDENTIFIED, EVENT_TYPE_NFC_SCANNED as EVENT_TYPE_NFC_SCANNED, KEYRINGS_KEY_TYPE_ID_NFC as KEYRINGS_KEY_TYPE_ID_NFC, KEYRINGS_ULP_ID as KEYRINGS_ULP_ID, KEYRINGS_USER_FULL_NAME as KEYRINGS_USER_FULL_NAME, KEYRINGS_USER_STATUS as KEYRINGS_USER_STATUS
from .data import Camera as Camera, EventType as EventType, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel, ProtectData as ProtectData, ProtectDeviceType as ProtectDeviceType, UFPConfigEntry as UFPConfigEntry
from .entity import EventEntityMixin as EventEntityMixin, ProtectDeviceEntity as ProtectDeviceEntity, ProtectEventMixin as ProtectEventMixin
from _typeshed import Incomplete
from homeassistant.components.event import EventDeviceClass as EventDeviceClass, EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

def _add_ulp_user_infos(bootstrap: Bootstrap, event_data: dict[str, str], ulp_id: str) -> None: ...

@dataclasses.dataclass(frozen=True, kw_only=True)
class ProtectEventEntityDescription(ProtectEventMixin, EventEntityDescription):
    entity_class: type[ProtectDeviceEntity]

class ProtectDeviceRingEventEntity(EventEntityMixin, ProtectDeviceEntity, EventEntity):
    entity_description: ProtectEventEntityDescription
    _event: Incomplete
    _event_end: Incomplete
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...

class ProtectDeviceNFCEventEntity(EventEntityMixin, ProtectDeviceEntity, EventEntity):
    entity_description: ProtectEventEntityDescription
    _event: Incomplete
    _event_end: Incomplete
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...

class ProtectDeviceFingerprintEventEntity(EventEntityMixin, ProtectDeviceEntity, EventEntity):
    entity_description: ProtectEventEntityDescription
    _event: Incomplete
    _event_end: Incomplete
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...

EVENT_DESCRIPTIONS: tuple[ProtectEventEntityDescription, ...]

@callback
def _async_event_entities(data: ProtectData, ufp_device: ProtectAdoptableDeviceModel | None = None) -> list[ProtectDeviceEntity]: ...
async def async_setup_entry(hass: HomeAssistant, entry: UFPConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
