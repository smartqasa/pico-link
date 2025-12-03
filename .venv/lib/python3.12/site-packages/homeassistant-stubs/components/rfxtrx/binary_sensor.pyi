import RFXtrx as rfxtrxmod
from . import DeviceTuple as DeviceTuple, async_setup_platform_entry as async_setup_platform_entry, get_pt2262_cmd as get_pt2262_cmd
from .const import COMMAND_OFF_LIST as COMMAND_OFF_LIST, COMMAND_ON_LIST as COMMAND_ON_LIST, CONF_DATA_BITS as CONF_DATA_BITS, CONF_OFF_DELAY as CONF_OFF_DELAY, DEVICE_PACKET_TYPE_LIGHTING4 as DEVICE_PACKET_TYPE_LIGHTING4
from .entity import RfxtrxEntity as RfxtrxEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_COMMAND_OFF as CONF_COMMAND_OFF, CONF_COMMAND_ON as CONF_COMMAND_ON, STATE_ON as STATE_ON
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete
SENSOR_STATUS_ON: Incomplete
SENSOR_STATUS_OFF: Incomplete
SENSOR_TYPES: Incomplete
SENSOR_TYPES_DICT: Incomplete

def supported(event: rfxtrxmod.RFXtrxEvent) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RfxtrxBinarySensor(RfxtrxEntity, BinarySensorEntity):
    _attr_force_update: bool
    _attr_name: Incomplete
    entity_description: Incomplete
    _data_bits: Incomplete
    _off_delay: Incomplete
    _delay_listener: CALLBACK_TYPE | None
    _cmd_on: Incomplete
    _cmd_off: Incomplete
    def __init__(self, device: rfxtrxmod.RFXtrxDevice, device_id: DeviceTuple, entity_description: BinarySensorEntityDescription, off_delay: float | None = None, data_bits: int | None = None, cmd_on: int | None = None, cmd_off: int | None = None, event: rfxtrxmod.RFXtrxEvent | None = None) -> None: ...
    _attr_is_on: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def _apply_event_lighting4(self, event: rfxtrxmod.RFXtrxEvent) -> None: ...
    def _apply_event_standard(self, event: rfxtrxmod.RFXtrxEvent) -> None: ...
    def _apply_event(self, event: rfxtrxmod.RFXtrxEvent) -> None: ...
    @callback
    def _handle_event(self, event: rfxtrxmod.RFXtrxEvent, device_id: DeviceTuple) -> None: ...
