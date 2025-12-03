from ..const import CONF_MASTER_GATEWAY as CONF_MASTER_GATEWAY, HASSIO_CONFIGURATION_URL as HASSIO_CONFIGURATION_URL, PLATFORMS as PLATFORMS
from ..deconz_event import DeconzAlarmEvent as DeconzAlarmEvent, DeconzEvent as DeconzEvent, DeconzPresenceEvent as DeconzPresenceEvent, DeconzRelativeRotaryEvent as DeconzRelativeRotaryEvent
from .config import DeconzConfig as DeconzConfig
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_HASSIO as SOURCE_HASSIO
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from pydeconz import DeconzSession as DeconzSession
from pydeconz.interfaces.api_handlers import APIHandler as APIHandler, GroupedAPIHandler as GroupedAPIHandler
from pydeconz.models.event import EventType

SENSORS: Incomplete

class DeconzHub:
    hass: Incomplete
    config: Incomplete
    config_entry: Incomplete
    api: Incomplete
    available: bool
    ignore_state_updates: bool
    signal_reachable: Incomplete
    deconz_ids: dict[str, str]
    entities: dict[str, set[str]]
    events: list[DeconzAlarmEvent | DeconzEvent | DeconzPresenceEvent | DeconzRelativeRotaryEvent]
    clip_sensors: set[tuple[Callable[[EventType, str], None], str]]
    deconz_groups: set[tuple[Callable[[EventType, str], None], str]]
    ignored_devices: set[tuple[Callable[[EventType, str], None], str]]
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, api: DeconzSession) -> None: ...
    @callback
    @staticmethod
    def get_hub(hass: HomeAssistant, config_entry: ConfigEntry) -> DeconzHub: ...
    @property
    def bridgeid(self) -> str: ...
    @property
    def master(self) -> bool: ...
    @callback
    def register_platform_add_device_callback(self, add_device_callback: Callable[[EventType, str], None], deconz_device_interface: APIHandler | GroupedAPIHandler, always_ignore_clip_sensors: bool = False) -> None: ...
    @callback
    def load_ignored_devices(self) -> None: ...
    @callback
    def async_connection_status_callback(self, available: bool) -> None: ...
    async def async_update_device_registry(self) -> None: ...
    @staticmethod
    async def async_config_entry_updated(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
    async def options_updated(self, previous_config: DeconzConfig) -> None: ...
    @callback
    def shutdown(self, event: Event) -> None: ...
    async def async_reset(self) -> bool: ...
