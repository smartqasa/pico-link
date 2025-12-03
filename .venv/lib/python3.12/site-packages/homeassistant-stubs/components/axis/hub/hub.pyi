import axis
from .. import AxisConfigEntry as AxisConfigEntry
from ..const import ATTR_MANUFACTURER as ATTR_MANUFACTURER
from .config import AxisConfig as AxisConfig
from .entity_loader import AxisEntityLoader as AxisEntityLoader
from .event_source import AxisEventSource as AxisEventSource
from _typeshed import Incomplete
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, format_mac as format_mac
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from typing import Any

class AxisHub:
    hass: Incomplete
    config: Incomplete
    entity_loader: Incomplete
    event_source: Incomplete
    api: Incomplete
    fw_version: Incomplete
    product_type: Incomplete
    unique_id: Incomplete
    additional_diagnostics: dict[str, Any]
    def __init__(self, hass: HomeAssistant, config_entry: AxisConfigEntry, api: axis.AxisDevice) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def signal_reachable(self) -> str: ...
    @property
    def signal_new_address(self) -> str: ...
    @staticmethod
    async def async_new_address_callback(hass: HomeAssistant, config_entry: AxisConfigEntry) -> None: ...
    async def async_update_device_registry(self) -> None: ...
    @callback
    def setup(self) -> None: ...
    async def shutdown(self, event: Event) -> None: ...
    @callback
    def teardown(self) -> None: ...
