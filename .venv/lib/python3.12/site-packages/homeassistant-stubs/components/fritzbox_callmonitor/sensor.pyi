import queue
from . import FritzBoxCallMonitorConfigEntry as FritzBoxCallMonitorConfigEntry
from .base import Contact as Contact, FritzBoxPhonebook as FritzBoxPhonebook
from .const import ATTR_PREFIXES as ATTR_PREFIXES, CONF_PHONEBOOK as CONF_PHONEBOOK, CONF_PREFIXES as CONF_PREFIXES, DOMAIN as DOMAIN, FritzState as FritzState, MANUFACTURER as MANUFACTURER, SERIAL_NUMBER as SERIAL_NUMBER
from _typeshed import Incomplete
from collections.abc import Mapping
from enum import StrEnum
from fritzconnection.core.fritzmonitor import FritzMonitor
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete

class CallState(StrEnum):
    RINGING = 'ringing'
    DIALING = 'dialing'
    TALKING = 'talking'
    IDLE = 'idle'

async def async_setup_entry(hass: HomeAssistant, config_entry: FritzBoxCallMonitorConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzBoxCallSensor(SensorEntity):
    _attr_has_entity_name: bool
    _attr_translation_key = DOMAIN
    _attr_device_class: Incomplete
    _attr_options: Incomplete
    _fritzbox_phonebook: Incomplete
    _prefixes: Incomplete
    _host: Incomplete
    _port: Incomplete
    _monitor: FritzBoxCallMonitor | None
    _attributes: dict[str, str | list[str] | bool]
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_value: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, phonebook_name: str, unique_id: str, fritzbox_phonebook: FritzBoxPhonebook, prefixes: list[str] | None, host: str, port: int) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def _start_call_monitor(self) -> None: ...
    def _stop_call_monitor(self, event: Event | None = None) -> None: ...
    def set_state(self, state: CallState) -> None: ...
    def set_attributes(self, attributes: Mapping[str, str | bool]) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str | list[str] | bool]: ...
    def number_to_contact(self, number: str) -> Contact: ...
    def update(self) -> None: ...

class FritzBoxCallMonitor:
    host: Incomplete
    port: Incomplete
    connection: FritzMonitor | None
    stopped: Incomplete
    _sensor: Incomplete
    def __init__(self, host: str, port: int, sensor: FritzBoxCallSensor) -> None: ...
    def connect(self) -> None: ...
    def _process_events(self, event_queue: queue.Queue[str]) -> None: ...
    def _parse(self, event: str) -> None: ...
