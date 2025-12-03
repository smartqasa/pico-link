from .const import DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .helpers import get_unique_id as get_unique_id, get_valueless_base_unique_id as get_valueless_base_unique_id
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.const import Platform as Platform, STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import device_registry as dr, entity_registry as er
from zwave_js_server.model.driver import Driver as Driver
from zwave_js_server.model.node import Node as Node
from zwave_js_server.model.value import Value as ZwaveValue

_LOGGER: Incomplete

@dataclass
class ValueID:
    command_class: str
    endpoint: str
    property_: str
    property_key: str | None = ...
    @staticmethod
    def from_unique_id(unique_id: str) -> ValueID: ...
    @staticmethod
    def from_string_id(value_id_str: str) -> ValueID: ...
    def is_same_value_different_endpoints(self, other: ValueID) -> bool: ...

@callback
def async_migrate_old_entity(hass: HomeAssistant, ent_reg: er.EntityRegistry, registered_unique_ids: set[str], platform: Platform, device: dr.DeviceEntry, unique_id: str) -> None: ...
@callback
def async_migrate_unique_id(ent_reg: er.EntityRegistry, platform: Platform, old_unique_id: str, new_unique_id: str) -> None: ...
@callback
def async_migrate_discovered_value(hass: HomeAssistant, ent_reg: er.EntityRegistry, registered_unique_ids: set[str], device: dr.DeviceEntry, driver: Driver, disc_info: ZwaveDiscoveryInfo) -> None: ...
@callback
def async_migrate_statistics_sensors(hass: HomeAssistant, driver: Driver, node: Node, key_map: dict[str, str]) -> None: ...
@callback
def get_old_value_ids(value: ZwaveValue) -> list[str]: ...
