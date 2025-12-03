import aiounifi
from .. import UnifiConfigEntry as UnifiConfigEntry
from ..const import ATTR_MANUFACTURER as ATTR_MANUFACTURER, CONF_SITE_ID as CONF_SITE_ID, PLATFORMS as PLATFORMS
from .config import UnifiConfig as UnifiConfig
from .entity_helper import UnifiEntityHelper as UnifiEntityHelper
from .entity_loader import UnifiEntityLoader as UnifiEntityLoader
from .websocket import UnifiWebsocket as UnifiWebsocket
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry, DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send

class UnifiHub:
    hass: Incomplete
    api: Incomplete
    config: Incomplete
    entity_loader: Incomplete
    _entity_helper: Incomplete
    websocket: Incomplete
    site: Incomplete
    is_admin: bool
    def __init__(self, hass: HomeAssistant, config_entry: UnifiConfigEntry, api: aiounifi.Controller) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def signal_heartbeat_missed(self) -> str: ...
    @callback
    def update_heartbeat(self, unique_id: str, heartbeat_expire_time: datetime) -> None: ...
    @callback
    def remove_heartbeat(self, unique_id: str) -> None: ...
    @callback
    def queue_poe_port_command(self, device_id: str, port_idx: int, poe_mode: str) -> None: ...
    @property
    def signal_reachable(self) -> str: ...
    @property
    def signal_options_update(self) -> str: ...
    async def initialize(self) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @callback
    def async_update_device_registry(self) -> DeviceEntry: ...
    @staticmethod
    async def async_config_entry_updated(hass: HomeAssistant, config_entry: UnifiConfigEntry) -> None: ...
    @callback
    def shutdown(self, event: Event) -> None: ...
    async def async_reset(self) -> bool: ...
