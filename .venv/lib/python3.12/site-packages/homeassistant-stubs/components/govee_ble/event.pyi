from .const import DOMAIN as DOMAIN
from .coordinator import GoveeBLEConfigEntry as GoveeBLEConfigEntry, format_event_dispatcher_name as format_event_dispatcher_name
from _typeshed import Incomplete
from govee_ble import ModelInfo as ModelInfo
from homeassistant.components.bluetooth import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak, async_last_service_info as async_last_service_info
from homeassistant.components.event import EventDeviceClass as EventDeviceClass, EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

BUTTON_DESCRIPTIONS: Incomplete
MOTION_DESCRIPTION: Incomplete
VIBRATION_DESCRIPTION: Incomplete

class GoveeBluetoothEventEntity(EventEntity):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _address: Incomplete
    _signal: Incomplete
    def __init__(self, model_info: ModelInfo, service_info: BluetoothServiceInfoBleak | None, address: str, description: EventEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_handle_event(self) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: GoveeBLEConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
