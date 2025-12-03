from .const import ATTR_DISPLAY_NAME as ATTR_DISPLAY_NAME, ATTR_INTEGRATION as ATTR_INTEGRATION, ATTR_VALUE as ATTR_VALUE, BRIDGE_MODEL as BRIDGE_MODEL, BRIDGE_SERIAL_NUMBER as BRIDGE_SERIAL_NUMBER, CHAR_BATTERY_LEVEL as CHAR_BATTERY_LEVEL, CHAR_CHARGING_STATE as CHAR_CHARGING_STATE, CHAR_HARDWARE_REVISION as CHAR_HARDWARE_REVISION, CHAR_STATUS_LOW_BATTERY as CHAR_STATUS_LOW_BATTERY, CONF_FEATURE_LIST as CONF_FEATURE_LIST, CONF_LINKED_BATTERY_CHARGING_SENSOR as CONF_LINKED_BATTERY_CHARGING_SENSOR, CONF_LINKED_BATTERY_SENSOR as CONF_LINKED_BATTERY_SENSOR, CONF_LOW_BATTERY_THRESHOLD as CONF_LOW_BATTERY_THRESHOLD, DEFAULT_LOW_BATTERY_THRESHOLD as DEFAULT_LOW_BATTERY_THRESHOLD, EMPTY_MAC as EMPTY_MAC, EVENT_HOMEKIT_CHANGED as EVENT_HOMEKIT_CHANGED, HK_CHARGING as HK_CHARGING, HK_NOT_CHARGABLE as HK_NOT_CHARGABLE, HK_NOT_CHARGING as HK_NOT_CHARGING, MANUFACTURER as MANUFACTURER, MAX_MANUFACTURER_LENGTH as MAX_MANUFACTURER_LENGTH, MAX_MODEL_LENGTH as MAX_MODEL_LENGTH, MAX_SERIAL_LENGTH as MAX_SERIAL_LENGTH, MAX_VERSION_LENGTH as MAX_VERSION_LENGTH, SERV_ACCESSORY_INFO as SERV_ACCESSORY_INFO, SERV_BATTERY_SERVICE as SERV_BATTERY_SERVICE, SIGNAL_RELOAD_ENTITIES as SIGNAL_RELOAD_ENTITIES, TYPE_FAUCET as TYPE_FAUCET, TYPE_OUTLET as TYPE_OUTLET, TYPE_SHOWER as TYPE_SHOWER, TYPE_SPRINKLER as TYPE_SPRINKLER, TYPE_SWITCH as TYPE_SWITCH, TYPE_VALVE as TYPE_VALVE
from .iidmanager import AccessoryIIDStorage as AccessoryIIDStorage
from .util import accessory_friendly_name as accessory_friendly_name, async_dismiss_setup_message as async_dismiss_setup_message, async_show_setup_message as async_show_setup_message, cleanup_name_for_homekit as cleanup_name_for_homekit, convert_to_float as convert_to_float, format_version as format_version, validate_media_player_features as validate_media_player_features
from _typeshed import Incomplete
from homeassistant.components.cover import CoverDeviceClass as CoverDeviceClass, CoverEntityFeature as CoverEntityFeature
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass
from homeassistant.components.remote import RemoteEntityFeature as RemoteEntityFeature
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass
from homeassistant.const import ATTR_BATTERY_CHARGING as ATTR_BATTERY_CHARGING, ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_HW_VERSION as ATTR_HW_VERSION, ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_MODEL as ATTR_MODEL, ATTR_SERVICE as ATTR_SERVICE, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, ATTR_SW_VERSION as ATTR_SW_VERSION, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfTemperature as UnitOfTemperature, __version__ as __version__
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Context as Context, Event as Event, EventStateChangedData as EventStateChangedData, HassJobType as HassJobType, HomeAssistant as HomeAssistant, State as State, callback as ha_callback, split_entity_id as split_entity_id
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.util.decorator import Registry as Registry
from pyhap.accessory import Accessory, Bridge
from pyhap.accessory_driver import AccessoryDriver
from pyhap.characteristic import Characteristic
from pyhap.iid_manager import IIDManager
from pyhap.service import Service as Service
from pyhap.util import callback as pyhap_callback
from typing import Any
from uuid import UUID

_LOGGER: Incomplete
SWITCH_TYPES: Incomplete
TYPES: Registry[str, type[HomeAccessory]]
RELOAD_ON_CHANGE_ATTRS: Incomplete

def get_accessory(hass: HomeAssistant, driver: HomeDriver, state: State, aid: int | None, config: dict) -> HomeAccessory | None: ...

class HomeAccessory(Accessory):
    driver: HomeDriver
    _reload_on_change_attrs: Incomplete
    config: Incomplete
    device_id: str | None
    category: Incomplete
    entity_id: Incomplete
    hass: Incomplete
    _subscriptions: list[CALLBACK_TYPE]
    _char_battery: Incomplete
    _char_charging: Incomplete
    _char_low_battery: Incomplete
    linked_battery_sensor: Incomplete
    linked_battery_charging_sensor: Incomplete
    low_battery_threshold: Incomplete
    def __init__(self, hass: HomeAssistant, driver: HomeDriver, name: str, entity_id: str, aid: int, config: dict[str, Any], *args: Any, category: int = ..., device_id: str | None = None, **kwargs: Any) -> None: ...
    _available: Incomplete
    def _update_available_from_state(self, new_state: State | None) -> None: ...
    @property
    def available(self) -> bool: ...
    @ha_callback
    @pyhap_callback
    def run(self) -> None: ...
    @ha_callback
    def async_update_event_state_callback(self, event: Event[EventStateChangedData]) -> None: ...
    @ha_callback
    def async_update_state_callback(self, new_state: State | None) -> None: ...
    @ha_callback
    def async_update_linked_battery_callback(self, event: Event[EventStateChangedData]) -> None: ...
    @ha_callback
    def async_update_linked_battery_charging_callback(self, event: Event[EventStateChangedData]) -> None: ...
    @ha_callback
    def async_update_battery(self, battery_level: Any, battery_charging: Any) -> None: ...
    @ha_callback
    def async_update_state(self, new_state: State) -> None: ...
    @ha_callback
    def async_call_service(self, domain: str, service: str, service_data: dict[str, Any] | None, value: Any | None = None) -> None: ...
    @ha_callback
    def async_reload(self) -> None: ...
    @ha_callback
    def async_stop(self) -> None: ...
    async def stop(self) -> None: ...

class HomeBridge(Bridge):
    hass: Incomplete
    def __init__(self, hass: HomeAssistant, driver: HomeDriver, name: str) -> None: ...
    def setup_message(self) -> None: ...
    async def async_get_snapshot(self, info: dict) -> bytes: ...

class HomeDriver(AccessoryDriver):
    hass: Incomplete
    entry_id: Incomplete
    _bridge_name: Incomplete
    _entry_title: Incomplete
    iid_storage: Incomplete
    def __init__(self, hass: HomeAssistant, entry_id: str, bridge_name: str, entry_title: str, iid_storage: AccessoryIIDStorage, **kwargs: Any) -> None: ...
    @pyhap_callback
    def pair(self, client_username_bytes: bytes, client_public: str, client_permissions: int) -> bool: ...
    @pyhap_callback
    def unpair(self, client_uuid: UUID) -> None: ...

class HomeIIDManager(IIDManager):
    _iid_storage: Incomplete
    def __init__(self, iid_storage: AccessoryIIDStorage) -> None: ...
    def get_iid_for_obj(self, obj: Characteristic | Service) -> int: ...
